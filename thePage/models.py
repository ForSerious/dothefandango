from __future__ import unicode_literals
import time
from django.db import models

# Create your models here.
def aNumber():
    sTime = time.strftime("%c")
    iNum = int(sTime[15:])
    return str(iNum * 3)