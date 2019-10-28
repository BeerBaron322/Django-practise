from django.urls import path

from .views import PostDitail, TagDetail
from .views import post_list, tag_list
from .views import TagCreate


urlpatterns = [
    path('', post_list, name="post_list_url"),
    path('post/<str:slug>/', PostDitail.as_view(), name='post_detail_url'),
    path('tags/', tag_list, name="tag_list_url"),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetail.as_view(), name='tag_detail_url')
]
