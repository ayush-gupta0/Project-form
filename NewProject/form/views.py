from django.shortcuts import render, redirect
from .models import Data


# Create your views here.

def InsertPage(request):
    return render(request, 'create.html')


def InserData(request):
    # Data come from HTML to view
    fname = request.POST['f_name']
    uname = request.POST['f_username']
    cname = request.POST['C_name']

    # Inserting data into table
    new_user = Data.objects.create(Name=fname, UserName=uname, CompanyName=cname)

    # After Insert redirect on showpage
    return redirect('showpage')


def ShowPage(request):
    # select all data from table
    all_data = Data.objects.all()
    return render(request, 'display.html', {'key1': all_data})


# Edit Page View
def EditPage(request, pk):
    # Fetching the Data of particular ID
    get_data = Data.objects.get(id=pk)
    return render(request, 'edit.html', {'key2': get_data})


# Update data View
def UpdateData(request, pk):
    udata = Data.objects.get(id=pk)
    udata.Name = request.POST['f_name']
    udata.UserName = request.POST['f_username']
    udata.CompanyName = request.POST['C_name']
    # Query for update
    udata.save()
    return redirect('showpage')

# Delete data view
def DeleteData(request, pk):
    ddata = Data.objects.get(id=pk)
    # Delete Query
    ddata.delete()
    return redirect('showpage')
