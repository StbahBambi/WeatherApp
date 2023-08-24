import json
import requests

location=input("Enter current location:")
params = {
  'access_key': 'dc2d2f4409088f1463e06d0cbfb96953',
  'query': location,

}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()
# print(api_response)
if 'success' in api_response and api_response['success'] == False:
    print("\n	API request has failed.")
else:
    print("\n")
    print(u'Current temperature in \033[31m%s\033[0m, \033[1m%s\033[0m is \033[1m%d℃\033[0m' % (api_response['location']['name'],api_response['location']['region'], api_response['current']['temperature']) )
    print(f"The Weather is \033[1m{api_response['current']['weather_descriptions'][0]}\033[0m")
    print(f"The Wind speed is \033[1m{api_response['current']['wind_speed']} km/h\033[0m")
    print(f"The Humidity is \033[1m{api_response['current']['humidity']}%\033[0m")
    print(f"At  \033[1m{api_response['location']['localtime']}\033[0m")
