from django.db import models
from django.utils import timezone #to use timezone as default 
from django.contrib.auth.models import User #to use user model as the author will be user only
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #we didn't put paranthesis after timezone.now() as we just want to pass the actual functio ass a default value
    author = models.ForeignKey(User,on_delete=models.CASCADE) #on_delete indicates if user get deleted then delete the post as well 
    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'pk' : self.pk})    



