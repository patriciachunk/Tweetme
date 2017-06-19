from django.shortcuts import render

# GET -- template home.html
def home(request):
    return render(request, "home.html", {})
