from django.shortcuts import render

# Create your views here.

def createnote(request):
    return render(request,"index.html")

def viewdata(request):
    return render(request,"view.html")

def newrecord(request):
    return render(request,"newrecord.html")