from django import template

register = template.Library()


@register.filter
def sub(value, arg):  # value는 자동으로 받아오는가?
    return value - arg