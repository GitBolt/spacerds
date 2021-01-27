from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from notis.models import Notification


class Questions(models.Model):
    title = models.CharField(max_length=90)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("qdetail", kwargs={"pk": self.pk})


class Answer(models.Model):
    question = models.ForeignKey(
        Questions, related_name="answers", on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.question.title, 'click to see answer')

    def get_success_url(self):
        return redirect("qhome")


def answered(sender, instance, **kwargs):
    answer = instance
    question = answer.question
    sender = answer.owner
    body = answer.body
    notify = Notification(
        myquestion=question, to_user=question.author, created_by=sender, preview=body)
    notify.save()


post_save.connect(answered, sender=Answer)
