import requests
def getWeather(location) :
    params = {
        'access_key': 'dc2d2f4409088f1463e06d0cbfb96953',
        'query': location,
        'forecast_days' : 7
    }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return api_response

location=input("Enter current location:")
result=getWeather(location)
# print(result)
if 'success' in result and result['success'] == False:
    print("\n	API request has failed.")
else:
    print("\n")
    print(u'Current temperature in \033[31m%s\033[0m, \033[34m%s\033[0m, \033[32m%s\033[0m is \033[33m%d℃\033[0m' % (result['location']['name'],result['location']['region'], result['location']['country'],result['current']['temperature']) )
    print(f"The Weather is {result['current']['weather_descriptions'][0]}")
    print(f"The Wind speed is {result['current']['wind_speed']} km/h")
    print(f"The Humidity is {result['current']['humidity']}%")
    print(f"At  {result['location']['localtime']}")
