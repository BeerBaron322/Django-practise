from django.contrib import admin
from .models import Post, Tag


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Функция которое возвращает все теги для поста
    def display_tag(self):
        return ', '.join([tag.title for tag in self.tag.all()][:3])
    # Список полей которые видно в админке при просмотре всех постов
    list_display = ['title', 'slug', display_tag, 'pub_date']
    # Список полей которые можно видно при создании/редактировании модели
    fields = ['title', 'body', 'tag', 'img']
    # Фильтр для поиска постов
    list_filter = ['pub_date']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
