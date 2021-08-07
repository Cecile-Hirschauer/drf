from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos',
                  'language', 'style', )
        
        
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all()    
    )
    
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
        # Because snippets is a reverse relationship on the default 
        # Django User model, it will not be included by default using 
        # the ModelSerializer class, we need to add an explicit field for it.