from models.models import Pingbanleibiao
from models.models import Padlog

def allPad():
    return Pingbanleibiao.objects.all().order_by('-time')

def logList(pad_id):
<<<<<<< HEAD
    return Padlog.objects.filter(pad_id=pad_id)

def padList(pad_id):
    return Pingbanleibiao.objects.filter(pad_id=pad_id)

def addpad(requeset):
    return Pingbanleibiao.objects.create(brand=requeset.POST[''])

=======
    return Padlog.objects.filter(pad_id=pad_id).order_by('-time')

def padList(pad_id):
    return Pingbanleibiao.objects.filter(pad_id=pad_id)

def addPad(requeset):
    return Pingbanleibiao.objects.create(brand=requeset.POST['brand'],
                                         model=requeset.POST['model'],
                                         encode=requeset.POST['encode'],
                                         time=requeset.POST['time'],
                                         source=requeset.POST['source'],
                                         state=requeset.POST['state'],
                                         remarks=requeset.POST['remarks'],)

def addLog(requeset, pad_id):
    return Padlog.objects.create(pad_id=pad_id,
                                 name=requeset.POST['name'],
                                 state=requeset.POST['state'],
                                 time=requeset.POST['time'],)
>>>>>>> 1.12
