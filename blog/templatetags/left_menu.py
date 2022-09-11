from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_left_menu():
    categories = Category.objects.all()[0:3]
    return {"categories": categories}