import re
from django import template
from django.conf import settings
from myapp.models import Student,Others,Proffesor

register = template.Library()

@register.filter
def retprof3(arg1):
    prof=Proffesor.objects.get(hostel=arg1)
    return prof.name