from django import template

register = template.Library()


@register.simple_tag
def my_sort_by(queryset, field):
    return queryset.order_by(field)
