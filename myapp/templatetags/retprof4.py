import re
from django import template
from django.conf import settings
from myapp.models import Student,Others,Proffesor

register = template.Library()

@register.filter
def retprof4(arg1):
    prof=Proffesor.objects.get(colName=arg1)
    return prof.webmail