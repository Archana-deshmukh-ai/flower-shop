# core/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def splitlines(value):
    """Split a string into a list of lines."""
    if isinstance(value, str):
        return value.splitlines()
    return []
