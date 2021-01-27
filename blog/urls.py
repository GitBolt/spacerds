from django.urls import include, path

from blog import views
from blog.views import BloglistView, BlogdetailView

urlpatterns = [
    path('', BloglistView.as_view(), name='bhome'),
    path('<int:pk>/', BlogdetailView.as_view(), name='bdetail'),
]
