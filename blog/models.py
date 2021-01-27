from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Blog(models.Model):
    heading = models.CharField(max_length=90)
    main = RichTextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    dummy = models.ImageField(default='default.png', upload_to='blogimages')
    bg = models.ImageField(default='default.png', upload_to='blogimages')

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("qdetail", kwargs={"pk": self.pk})

