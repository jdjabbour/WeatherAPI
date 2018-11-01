#####################################################################
# Python 3
# Created a new backend for the weather api
# Converted the code from a functional only to a more module OOP style code.
# Also used a more secure importable module for the Auth Key
#####################################################################

try:
    import urllib.request
except:
    print('Python version 3 is needed.')
import json
import Cred


class Authorization():
    
    def __init__(self):
        self.key = Cred.api_key

    # Establishing the Authorization method
    def auth(self):
        return self.key



class Get_weather_data():

    def __init__(self, zip):
        self.appid = Authorization()
        self.appid = self.appid.auth()
        self.zip = str(zip) 
        
    def lookup(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?zip='
        units = '&units=imperial'
        country = 'us&&APPID='
        finalURL = url + self.zip + ',' + country + self.appid + units
        try:
            response = urllib.request.urlopen(finalURL).read()
            jsonResponse = json.loads(response.decode('utf-8'))
            output = jsonResponse  # This just makes it easier to use/type
            return output
        except:
            return 'Try: python3 ***.py'



class Parse_output():

    def __init__(self, input_json):
        self.input_json = input_json

    def printed_output(self):
        #x = []
        try:
            x = []
            x.append(self.input_json['name'])
            x.append(str(self.input_json['main']['temp']))
            x.append(str(self.input_json['main']['humidity']))
            x.append(str(self.input_json['wind']['speed']))
            for i in self.input_json['weather']:
                x.append(i['description'])
            return x
        except:
            '''
            x = []
            x.append(self.input_json['cod'])
            x.append(self.input_json['message'])
            '''
            return 'Try another zip.'



if __name__ == "__main__":
    zipcode = input("whats your zip? ")
    y = Get_weather_data(zipcode)
    y = y.lookup()
    #print(y)
    x = Parse_output(y)
    print(x.printed_output())