from django.db import models
from django.contrib.contenttypes.models import ContentType
# from django.urls import reverse


class Topic(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'


class News(models.Model):

    category = models.ForeignKey(Topic, verbose_name='Категория (тема) статьи', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    image = models.ImageField(verbose_name='Изображение статьи')
    description = models.TextField(verbose_name='Краткое содержание статьи')
    full_text = models.TextField(verbose_name='Полный текст статьи')
    author = models.TextField(verbose_name='Автор', default='BGMT')
    author_avatar = models.ImageField(verbose_name='Фото автора', default='bgmt-logo-minimal.png')
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    keywords = models.TextField(verbose_name='Теги, ключевые слова', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.category}/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

