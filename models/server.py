from models.models import Pingbanleibiao
from models.models import Padlog
import uuid

def allPad():
    return Pingbanleibiao.objects.all()

def logList(id):
    return Padlog.objects.filter(padid=id)

def padList(id):
    return Pingbanleibiao.objects.filter(id=id)

def random_id():
    res = str(uuid.uuid4())
    res = res.replace('-', '')
    return res[:16]
