from django.shortcuts import render
from models import server

# Create your views here.

def allPad(request):
    padList = server.allPad()
    return render(request, 'padList.html', {'padList': padList})

def padLog(request, id):
    padList = server.padList(id)
    logList = server.logList(id)
    return render(request, 'logList.html', {'padList': padList, 'logList': logList})

def addPad(request):
    if request.POST:
        server.addPad(request)
    return render(request, 'addPad.html')

def test(request):
    id = server.random_id()
    return render(request, 'test.html', {id: id})