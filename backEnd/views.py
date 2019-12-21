from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.utils.six import BytesIO

from backEnd import services

import qrcode

# Create your views here.

def all_pad(request):
    padList = services.all_pad()
    return render(request, 'padList.html', {'padList': padList})

def pad_log(request, pad_id):
    pad_id = str(pad_id)
    url = 'http://127.0.0.1:8000/padLog/' + pad_id
    padList = services.pad_list(pad_id)
    logList = services.log_list(pad_id)
    return render(request, 'logList.html', {'padList': padList, 'logList': logList, 'url': url})

def add_pad(request):
    if request.POST:
        addPad = services.add_pad(request)
        return redirect(all_pad)
    else:
        return render(request, 'addPad.html')

def add_log(request, pad_id):
    if request.POST:
        addlog = services.add_log(request, pad_id)
        return redirect('padLog', pad_id=pad_id)
    else:
        return render(request, 'addLog.html', {'pad_id': pad_id})

def download_qrcode(request, pad_id):
    pad_id = str(pad_id)
    url = 'http://127.0.0.1:8000/padLog/' + pad_id
    picture_name = 'picture/' + pad_id + '.png'
    img = qrcode.make(url)
    buf = BytesIO()
    with open(picture_name, 'wb')as f:
        img.save(f)
    return HttpResponse(picture_name, content_type='image/png')
