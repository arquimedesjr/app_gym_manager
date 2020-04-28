from django import template
register = template.Library()

@register.filter
def filter_date(value):
    return value.strftime("%d/%m/%Y")
