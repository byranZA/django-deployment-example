from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    cuts out all vlaues of arg from the string
    """
    return value.replace(arg,'')
