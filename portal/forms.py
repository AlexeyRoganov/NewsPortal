from django.forms import ModelForm, BooleanField
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

# Создаём модельную форму
class ProductForm(ModelForm):
    check_box = BooleanField(label='Подтвердить')
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'cats', 'check_box']


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user