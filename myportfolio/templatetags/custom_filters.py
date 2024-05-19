# myapp/templatetags/custom_filters.py
from myportfolio.libs.converter import formatGerNumberStr

from django import template
import locale

register = template.Library()

@register.filter
def german_number_format(value):
    return formatGerNumberStr(str(value))