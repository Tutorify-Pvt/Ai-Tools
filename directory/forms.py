from django.forms import ModelForm

from .models import *


class Directory_form(ModelForm):
    class Meta:
        model = Directory
        fields = ['author','title', 'description', 'features', 'source_link', 'tag', 'types']
        # fields = '__all__'


class Tag_form(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class Type_form(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'
