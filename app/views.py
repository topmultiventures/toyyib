from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "app/home.html")

def adamson(request, person):
    print(request.method)
    context = {"name": person}
    return render(request, "app/adamson.html", context)
def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        registrationnumber = request.POST.get("registrationnumber")
        # name=request.POST["name"]
        if not name or not registrationnumber:
            # print("you are mad")
            messages.error(request,"All field are required")
            return redirect(form)
        # print(name,registrationnumber)
    print("hello")
    return render(request, "app/form.html" )