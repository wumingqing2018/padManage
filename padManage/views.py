from django.shortcuts import render
from django.shortcuts import redirect

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
        addlog = server.addLog(request, pad_id=addPad.pad_id)
        return redirect(allPad)
    else:
        return render(request, 'addPad.html')

def addLog(request, pad_id):
    if request.POST:
        addlog = server.addLog(request, pad_id)
        return redirect('padLog', pad_id=pad_id)
    else:
        return render(request, 'addLog.html', {'pad_id': pad_id})
