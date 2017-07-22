import re
from django import template
from django.conf import settings

register = template.Library()

@register.filter
def addstr(arg1):
    """concatenate arg1 & arg2"""
    return arg1+1