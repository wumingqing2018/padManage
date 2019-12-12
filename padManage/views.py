from django.shortcuts import render
from models import server

# Create your views here.

def allPad(request):
    padList = server.allPad()
    return render(request, 'padList.html', {'padList': padList})

def padLog(request, pad_id):
    padList = server.padList(pad_id)
    logList = server.logList(pad_id)
    return render(request, 'logList.html', {'padList': padList, 'logList': logList})

def addPad(request):
    if request.POST:
        server.addpad(request)
    else:
        return render(request, 'addPad.html')