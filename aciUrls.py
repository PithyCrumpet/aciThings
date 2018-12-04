from login import *
import json
import requests

class urlList:
    #returns the mac address of a given endpoint IP address
    #def getMacUrl(self, apic, ip):
        #return 'https://' + apic + '/api/node/class/fvCEp.json?rsp-subtree=full&rsp-subtree-include=required&rsp-subtree-filter=eq(fvIp.addr,"' + ip + '")'
	
    #returns the switchport that an endpoint is learnt from
    #def getSwitchportUrl(self, apic, tenancy, ap, epg, mac):
        #return 'https://' + apic + '/api/node/mo/uni/' + tenancy + '/ap-' + ap + '/' + epg + '/cep-' + mac + '.json?query-target=subtree&target-subtree-class=fvCEp,fvRsCEpToPathEp,fvRsHyper,fvRsToNic,fvRsToVm'

    #returns the switchport details of a given switchport
    def getSwitchportDetailsUrl(self, apic, pod, node, port):
        return 'https://' + apic + '/api/node/mo/topology/pod-' + pod + '/node-' + node + '/sys/phys-[' + port + '].json'
    
    #returns the allowed vlans on switchport
    #def getSwitchportVlansUrl(self, apic, pod, port, node):
        #return 'https://' + apic + '/api/node/mo/topology/' + pod + '/node-' + node + '/sys/phys-[' + port + '].json?&query-target=children&target-subtree-class=ethpmPhysIf'
    
    #returns the allowed vlans on switchport
    #def getSwitchportIpAddressesUrl(self, apic, pod, port, node):
        #return 'https://' + apic + '/api/node/mo/topology/' + pod + '/node-' + node + '/sys.json?query-target=subtree&target-subtree-class=epmIpEp&query-target-filter=eq(epmIpEp.ifId,"' + port + '")'
    
    #returns the allowed vlans on switchport
    #def getSwitchportMacAddressesUrl(self, apic, pod, port, node):
        #return 'https://' + apic + '/api/node/mo/topology/' + pod + '/node-' + node + '/sys.json?query-target=subtree&target-subtree-class=epmMacEp&query-target-filter=eq(epmMacEp.ifId,"' + port + '")'
	
    #This method will send out the GET/POST request to ACI 
    def getRequest(self, url, cookies):
        try:
            response = requests.get(url, cookies=cookies, verify=False)
            return response.json()
        except requests.exceptions.RequestException as error:
            print("Http error: ", error)



#Tests
#urls = urlList()
#token = login('sandboxapicdc.cisco.com', 'admin', 'ciscopsdt')
#testData = urls.getRequest(urls.getSwitchportDetailsUrl('sandboxapicdc.cisco.com', '1', '101', 'eth1/1'), token)
#print(testData)



