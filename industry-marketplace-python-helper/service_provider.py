from imp import IndustryMarketplace
import random
import pprint
import pickle


class ServiceProvider(IndustryMarketplace):
    name = 'ServiceProvider:4001'
    service_provider = True
    fund_wallet = False
    gps_coords = '54.123, 4.321'
    
    endpoint = 'http://192.168.3.5:4001'

    def load_model(self, filename):
        '''
         Load the saved model. Take care while loading saved model from
         different CPU architecture, they might not work. 
         This model was created using Raspberry Pi 4
        '''
        try:
            self.loaded_model = pickle.load(open(filename, 'rb'))
            self.log('Loaded model: %s' % filename)
        except Exception as e:
            self.log('Loading model failed')

    def on_cfp(self, data, irdi, submodels):
        '''
        As soon as this service provider receives a CfP this function is called
        You can use the supplied irdi and submodels to define a price if you like
        '''

        self.log('Call for Proposal received for irdi %s!' % irdi)
        #self.log('Submodels: ')
        #pprint.pprint(submodels)
        

        # Drone connectivity provision
        if irdi == '0173-1#01-BAF577#004':
            price = random.randint(10, 20)
        else:
            self.log('We only do Drone connectivity provision", ignore this one!')
            return

        try:
            #self.log("submodels.values")
            #pprint.pprint(submodels.values())
            # prepare model input, order matters
            lng, lat = submodels['0173-1#02-BAF163#002']['value'].split(', ')
            model_input = [
               submodels['0173-1#02-AAA818#006']['value'],
               submodels['0173-1#02-AAB919#007']['value'],
               submodels['0173-1#02-AAI957#004']['value'],
               int(submodels['0173-1#07-ABA076#001']['value']),
               int(submodels['0173-1#07-ABA075#001']['value']),
               submodels['0173-1#02-AAF090#005']['value'],
               float(lng),
               float(lat)
            ]
            
            self.log("model input:")
            pprint.pprint(model_input)

            # do inferencing
            prediction = self.loaded_model.predict([model_input])
            self.log('prediction:')
            self.log(prediction[0])

            # decision time
            if prediction[0] == 1:
                ret = self.proposal(data, price_in_iota=price)
            else:
                self.log('model decision: do not sent proposal!')
        except Exception as e:
            self.log('Unable to send proposal', e)

        
        self.log('proposal sent! Requesting %si for this service' % price)

    def on_accept_proposal(self, data, irdi, submodels):
        self.log('Proposal accepted! Start fulfilling')
        self.log('Sending inform confirm')
        ret = self.inform_confirm(data)
        #self.log(ret)

    def on_reject_proposal(self, data, irdi, submodels):
        self.log('Proposal rejected! Either do nothing or offer a Discount?')
        #pprint.pprint(data)

    def on_inform_payment(self, data, irdi, submodels):
        self.log('Payment received! IMP transaction done!')
        #pprint.pprint(data)


if __name__ == '__main__':
    imp = ServiceProvider()
    # load model from file
    imp.load_model('../saved_model/finalized_model.sav');
    imp.listen()
