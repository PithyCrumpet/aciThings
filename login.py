import requests
import json

def login(apicIp, username, password):
    #use the value of the apicIp argument for the POST URL
    loginUrl = 'https://' + apicIp + '/api/aaaLogin.json'

    #use the values of the username and password arguments to produce the payload to be sent with the POST
    payload = '{"aaaUser": {"attributes": {"name": "' + username + '", "pwd": "' + password + '"}}}'
    
    #try making the POST and include the payload
    try:
        apicResponse = requests.post(loginUrl, data=payload, verify=False)
    except Exception as error:
        apicResponse = requests.post(loginUrl, data=payload, verify=False)
        print('There was an issue posting credentials to APIC. The error was: \n' + repr(error))

    #retrieve the token
    #if the APIC responds with a HTTP 200 then pull out the token from the response
    if apicResponse.status_code == requests.codes.ok:
        try:
            apicResponse = apicResponse.json()
            apicResponse = apicResponse['imdata'][0]['aaaLogin']['attributes']['token']
            token = {'APIC-Cookie': apicResponse}
            return token
        except Exception as error:
            print('There was an issue retrieving the token from the APIC response. The error was: \n' + repr(error))
    #if the APIC responds with anything other than a HTTP 200 then print the error
    else:
        print('Login failed. The server responded with error: \n' + repr(apicResponse.status_code))

#Tests
#cookie = login('sandboxapicdc.cisco.com', 'admin', 'ciscopsdt')