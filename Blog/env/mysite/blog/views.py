from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', context={'posts': posts})


class PostDitail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})
