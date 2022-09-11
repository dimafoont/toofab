from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_right_menu():
    categories = Category.objects.all()[3:6]
    return {"categories": categories}