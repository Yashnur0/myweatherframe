from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
  
  
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API
  
        source = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
 
                    + city + "weathar.txt").read()
  
        # converting JSON data to a dictionary
        jason_data = json.loads(source)
        temp_inkelv = int(jason_data['main']['temp']),
        temp_inc = temp_inkelv - 273.15 
        temp_inf = (temp_inkelv * 9/5) - 459.67
  
        # data for variable list_of_data
        data = {

            
            "country" : str(jason_data['sys']['country']),

            "cel" : '{:.1f}°C, {:.1f}°F'.format(temp_inc, temp_inf),
            "weather_situation" : str(jason_data['weather'][0]['description']),
            "show_weather": str(jason_data['weather'][0]['main']),
            "humid" : str(jason_data['main']['humidity'])
        }
        print(data)
    else:
        data ={}
    return render(request, "myweather/index.html", data)