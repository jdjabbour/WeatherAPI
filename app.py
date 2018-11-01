###########################################################################################
# This app calls the weather api openweathermap.org
# We will call it by zip and have the app return the current points of weather for that
# location.
###########################################################################################
import urllib.request
import json

def lookup(zip):
    '''
    This section of the function sets up the variables to call the API.
    This API request calls the weather by the zip code.
    http://api.openweathermap.org/data/2.5/weather?q=14522,us&&APPID=9b2c7c7f226d3ca9f0b2e55b07f0df22&units=imperial
    '''
    api_key = '&&APPID='
    url = 'http://api.openweathermap.org/data/2.5/weather?zip='
    units = '&units=imperial'
    country = 'us'
    finalURL = url + zip + ',' + country + api_key + units

    # This calls the url from above and loads the response into a variable
    response = urllib.request.urlopen(finalURL).read()
    # This takes the response variable and loads it into a Json format
    jsonResponse = json.loads(response.decode('utf-8'))
    y = jsonResponse  # This just makes it easier to use/type

    try:
        x = []
        # This starts parsing the json file and returning the output
        #print('The city of ' + y['name'] + ', ' + country)
        x.append(y['name'])
        #print(x)
        print('Temp: ' + str(y['main']['temp']))
        x.append(str(y['main']['temp']))

        return x
        '''
        print('Humidity: ' + str(y['main']['humidity']))
        print('Wind Speed: ' + str(y['wind']['speed']) + ' mph')

        for i in y['weather']:
            print('Cloud coverage: ' + i['description'])
           ''' 
    except ValueError:
        # This doesn't quite work as it returns a 404 error instead of a value error
        print('City does not exist')
        #return 'City does not exist'
        quit()


# = input('Enter zip. ')

#lookup(zip)
