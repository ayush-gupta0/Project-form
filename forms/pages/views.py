from os import name
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from pages.models import Form


def home(request):
    if request.method == "POST":
        print("this is post")
        name = request.POST.get('name')
        eid = request.POST.get('eid')
        print(name, eid)

        ins = Form(name=name, eid=eid)
        ins.save()
    return render(request, "index.html")
