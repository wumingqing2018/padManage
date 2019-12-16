from models.models import Pingbanleibiao
from models.models import Padlog

def all_pad():
    return Pingbanleibiao.objects.all().order_by('-time')

def log_list(pad_id):
    return Padlog.objects.filter(pad_id=pad_id).order_by('-time')

def pad_list(pad_id):
    return Pingbanleibiao.objects.filter(pad_id=pad_id)

def add_pad(requeset):
    return Pingbanleibiao.objects.create(brand=requeset.POST['brand'],
                                         model=requeset.POST['model'],
                                         encode=requeset.POST['encode'],
                                         time=requeset.POST['time'],
                                         source=requeset.POST['source'],
                                         state=requeset.POST['state'],
                                         remarks=requeset.POST['remarks'],)

def add_log(requeset, pad_id):
    return Padlog.objects.create(pad_id=pad_id,
                                 name=requeset.POST['name'],
                                 state=requeset.POST['state'],
                                 time=requeset.POST['time'],)
