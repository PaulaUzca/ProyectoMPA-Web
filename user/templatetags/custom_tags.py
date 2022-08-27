from django import template
from django.urls import reverse

register = template.Library()

# Tag para ir a una sección en especifico de una página
@register.simple_tag
def anchor(url_name, section_id):
    return reverse(url_name) + '#' + section_id