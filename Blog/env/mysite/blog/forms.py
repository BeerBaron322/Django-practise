from django import forms
from django.core.exceptions import ValidationError

from .models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slag may not be "create"')
        if Tag.objects.filter(slug=new_slug).exists():
            raise ValidationError('We already have "{}"'.format(new_slug))
        return new_slug
