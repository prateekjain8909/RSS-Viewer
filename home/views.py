from django.http import HttpResponseRedirect
from django.shortcuts import render
from playsound import playsound
from .form import urlsearch
from .code import get_xml
def search(request):
    form = urlsearch()
    # playsound("home/hello.mp3")
    return render(request,"home/home.html", {'form': form})

def process(request):

    if request.method == 'POST':
        print(request.POST)
        form = urlsearch(request.POST)
        rss = get_xml(form["url"].value())
        if form.is_valid():
            return render(request,"viewer/viewer.html",rss)