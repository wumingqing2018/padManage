from backEnd.models import Pingbanleibiao
from backEnd.models import Padlog

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
                                         remarks=requeset.POST['remarks'],)


def add_log(requeset, pad_id):
    pad=Pingbanleibiao.objects.get(pad_id=pad_id)
    pad.use_name = requeset.POST['name']
    pad.use_state = requeset.POST['state']
    pad.use_time = requeset.POST['time']
    pad.save()

    log = Padlog.objects.create(pad_id=pad_id,
                                name=requeset.POST['name'],
                                state=requeset.POST['state'],
                                time=requeset.POST['time'],)