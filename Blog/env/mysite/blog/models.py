from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
import itertools


# Create your models here.

# Модель отвечающая за посты
class Post(models.Model):
    title = models.CharField(max_length=100)  # Название поста
    body = models.TextField()  # Тело поста (его содержание)
    slug = models.SlugField(max_length=100, unique=True)  # Уникальный слаг для каждого поста
    pub_date = models.DateField(auto_now_add=True)  # Дата публикации (устанвливается при создании поста)
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts')  # Теги к посту (связь многие ко многим)
    img = models.ImageField(upload_to='post_images', blank=True, default='static\images\logo.jpg')

    # Переопределение метода __str__ который возвращает названеи поста
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Для того чтобы избежать переопределенния слага при каждом сохранении,
        # мы проверяем есть ли уже у этой можели id
        if not self.id:
            # Двум переменным присваиваем значение self.title, но все пробелы замененны на "-" (см. slugify)
            slug_candidate = slugify(self.title)
            slug_original = slugify(self.title)
            # Проверка в цикле не существует ли уже такой слаг
            for i in itertools.count(1, 1):
                # Если такого слага нет то мы выходим из цикла
                if not Post.objects.filter(slug=slug_candidate).exists():
                    break
                # Если такой слаг есть, то мы к нему в конец добавляем i, который увеличивается на 1 на каджом шаге
                slug_candidate = '{}-{}'.format(slug_original, i)
            self.slug = slug_candidate
        super().save(*args, **kwargs)


# Модель отвечающая за теги
class Tag(models.Model):
    title = models.CharField(max_length=50)  # Название тега
    slug = models.SlugField(max_length=50, unique=True)  # Уникальный слаг для каждого тега

    # Переопределение метода __str__ который возвращает названеи тега
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})
