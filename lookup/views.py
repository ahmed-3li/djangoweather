from django.shortcuts import render


def home(request):
	import json
	import requests
	
	if request.method == 'POST':
		zipcode = request.POST['zipcode']
		
		api = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=25&API_KEY=CF464AE6-F07E-406D-A5F8-59320C065759")
		try:
			api = json.loads(api.content)
		except Exception as e:
			api = 'error'
		return render(request, 'home.html', {'api' : api})
	else:
		api = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=CF464AE6-F07E-406D-A5F8-59320C065759")
		try:
			api = json.loads(api.content)
		except Exception as e:
			api = 'error'
		return render(request, 'home.html', {'api' : api})

def about(request):
	return render(request, 'about.html', {})
