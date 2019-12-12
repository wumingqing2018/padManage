from models.models import Pingbanleibiao
from models.models import Padlog

def allPad():
    return Pingbanleibiao.objects.all()

def logList(pad_id):
    return Padlog.objects.filter(pad_id=pad_id)

def padList(pad_id):
    return Pingbanleibiao.objects.filter(pad_id=pad_id)

def addpad(requeset):
    return Pingbanleibiao.objects.create(brand=requeset.POST[''])

