from imp import IndustryMarketplace
import pprint
import sys

class ServiceRequester(IndustryMarketplace):
    name = 'Requester100'
    service_provider = False
    fund_wallet = True
    gps_coords = '54.000, 4.000'

    endpoint = 'http://192.168.3.5:4001'
    
    def on_proposal(self, data, irdi, submodels):
        '''
        Accept only if the price is between 5 and 15
        '''
        self.log('on proposal called!')
        try:
            price = self.get_price(irdi, submodels)
            self.log('Received proposal for %si for irdi %s' % (price, irdi))
            if not price:
                self.log('Price not found, submodels: %s' % submodels)

            if price >= 5 and price <= 15:
                self.log('Accepting proposal')
                self.accept_proposal(data)
            else:
                self.log('Rejecting proposal')
                self.reject_proposal(data)
        except Exception as e:
            self.log('Error on accepting: %s' % e)

    def on_inform_confirm(self, data, irdi, submodels):
        self.log('Offer confirmed, time to pay')
        self.inform_payment(data)


if __name__ == '__main__':

    imp = ServiceRequester()
    
    # Either run it as a listeing service
    if len(sys.argv) == 1:
        imp.listen()
    
    # Or as a one time command provisioning drone connectivity!
    if len(sys.argv) == 2 and sys.argv[1] == 'drone_connectivity_provision':

        values = {
            "0173-1#02-AAA818#006" : 32,
            "0173-1#02-AAB919#007" : 23,
            "0173-1#02-AAI957#004" : 95,
            "0173-1#07-ABA076#001" : 1,
            "0173-1#07-ABA075#001" : 0,
            "0173-1#02-AAF090#005" : 9.39,
            "0173-1#02-BAF163#002" : "50.0960212, 9.3479825" 
        }

        ret = imp.cfp(irdi='0173-1#01-BAF577#004"', values=values, location='54.321, 4.123')
        #pprint.pprint(ret)
    
