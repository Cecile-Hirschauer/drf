from rest_framework import generics
from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# We also need to add two new read-only views for a list of all users 
# and a detail view of individual users. Note that we use the generic 
# class-based RetrieveAPIView for the read-only detail view. 
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # Currently there is no way to automatically associate the logged-in user 
    # that created a snippet with the snippet instance. We can set this 
    # automatically by overriding .perform_create() method on our snippet 
    # views that lets us modify how an instance is saved.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    