from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import urlsearch
from .code import get_xml
# from . import "voice.mp3"
# rss={}
def search(request):
    if request.method == 'POST':
        form = urlsearch(request.POST)
        rss = get_xml(form["url"].value())
        # print(rss)
        if form.is_valid():
            return render(request,"viewer/viewer.html",rss)
    else:
        form = urlsearch()

    # say(
    # language='en-us', # language to convert text to
    # text='say hi')

    return render(request, "home/home.html", {'form': form, "audio": "voice.mp3"})
    # return render(request, "post.html")


# from django.views.decorators.csrf import csrf_exempt #This is to exclude the token authentication for the post request. 
#                                                      #should be resolved if needed   

# @csrf_exempt
# def audio_data(request):
#     if request.method == 'POST':
        
#         #Authenticating API
#         gmaps = googlemaps.Client(key='YOUR_API_KEY')
        
#         #Calling google geocode API with query as a Address
#         geocode_result = gmaps.geocode(request.POST['send'])

#         #geocode_result will return a JSON, contents can be extracted 
#         #for example 
#         x = geocode_result[0]['geometry']['location']['lat'] #get latitute for the query 
#         y = geocode_result[0]['geometry']['location']['lng'] #get longitude for the query 
        
#     else: 
#         message = "Please check the POST call"
#     return HttpResponse(message)