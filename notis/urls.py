from django.urls import include, path

from notis import views
from notis.views import shownoti, NotidetailView


urlpatterns = [
    path('', shownoti, name="notis"),
    path('<int:pk>/', NotidetailView.as_view(), name='ndetail'),
]
