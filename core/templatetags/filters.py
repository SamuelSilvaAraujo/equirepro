from django import template

register = template.Library()

@register.filter(name='remove_mask')
def remove_mask(value):
    phone = ''.join(x for x in value if x not in "()- ")
    return phone