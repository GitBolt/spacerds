from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Notification(models.Model):
    myquestion = models.ForeignKey('qapp.Questions', on_delete=models.CASCADE, blank=True, null=True)
    to_user = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    preview = models.TextField(default="")
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
       return '%s - %s' % (self.created_by, self.myquestion)







