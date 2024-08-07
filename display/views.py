from django.shortcuts import render
import requests
import json

#from .forms import OpForms  
def display_weather(request):
    
    if request.method=='POST':
        city=request.POST.get('city')
        #form=OpForms(request.POST)
        #if form.is_valid():
            #form.save()
    
        key='c562d3ad892c6f396960a304f1fac429'
    
        base=(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}')
        res=requests.get(base)
        data=res.json()

        context={
            'des':str(data['main']['temp']),
            'pres':str(data['main']['pressure']),
            'hum':str(data['main']['humidity'])
            }
        print(context)
    else:
        context={}
    return render(request,'weather.html',context)
