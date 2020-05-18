from imp import IndustryMarketplace
import random
import pprint
import pickle


class ServiceProvider(IndustryMarketplace):
    name = 'DronesRus'
    service_provider = True
    fund_wallet = False
    gps_coords = '54.123, 4.321'
    
    endpoint = 'http://192.168.3.5:4000'

    def load_model(self, filename):
        try:
            self.loaded_model = pickle.load(open(filename, 'rb'))
        except Exception as e:
            self.log('Loading model failed', e)

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
            #self.log("submodels.values", submodels.values)
            #self.log("data", data)
            result = loaded_model.predict(data)
            if result[0] == 1:
                ret = self.proposal(data, price_in_iota=price)
            else:
                self.log('proposal did not send')
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
    imp.load_model('../saved_model/finalized_model.sav');
    imp.listen()
