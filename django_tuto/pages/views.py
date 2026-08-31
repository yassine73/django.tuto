from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"page": "index", "text": "", "test": "we are testing!!!", "filesize": 33333333}
    return render(request, "pages/index.html", context)

def about(request):
    context = {"page": "about"}
    return render(request, "pages/about.html", context)