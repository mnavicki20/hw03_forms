from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        verbose_name = 'Публикация пользователя'
        verbose_name_plural = 'Публикации пользователей'
