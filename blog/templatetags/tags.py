from django import template
from blog.models import Tag

register = template.Library()

@register.inclusion_tag('blog/tags_tpl.html')
def get_tags(cnt=6):
    tags = Tag.objects.all()[:cnt]
    return {"tags": tags}