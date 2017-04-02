from __future__ import unicode_literals
import time
from django.db import models

# Create your models here.
def aNumber():
    sTime = time.strftime("%S")
    iNum = int(sTime)
    return str(iNum * 3)