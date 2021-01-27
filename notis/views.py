from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView

from qapp.models import Questions
from .models import Notification


def shownoti(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user)
    Notification.objects.filter(
        to_user=user, is_read=False).update(is_read=True)
    context_object_name = 'notifications'
    template = loader.get_template('notifications.html')

    context = {
        'notifications': notifications,
    }
    return HttpResponse(template.render(context, request))


def countnoti(request):
    count_noti = 0
    if request.user.is_authenticated:
        count_noti = Notification.objects.filter(is_read=False).count()

        return {'count_noti': count_noti}


def Countnotis(request):
    count_notis = 0
    if request.user.is_authenticated:
        count_notis = Notification.objects.filter(
            to_user=request.user, is_read=False).count()

    return {'count_notis': count_notis}


class NotidetailView(DetailView):
    model = Questions
    template_name = 'qdetail.html'
