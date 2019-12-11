from models.models import Pingbanleibiao
from models.models import Padlog

def allPad():
    return Pingbanleibiao.objects.all()

def logList(id):
    return Padlog.objects.filter(padid=id)

def padList(id):
    return Pingbanleibiao.objects.filter(id=id)
