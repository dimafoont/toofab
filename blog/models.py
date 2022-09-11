from django.db import models
from django.urls import reverse_lazy

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at:')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['created_at']

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={"slug": self.slug})

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at:')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated', null=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='Views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']
