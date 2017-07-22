import re
from django import template
from django.conf import settings
from myapp.models import Student,Others,Proffesor

register = template.Library()

@register.filter
def retprof2(arg1):
    other=Others.objects.get(colName=arg1)
    return other.name