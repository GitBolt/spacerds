from django.urls import include, path

from qapp.views import QuestionlistView, QuestiondetailView, QuestioncreateView, QuestionupdateView, QuestiondeleteView, AddAnswerView, AnswerdeleteView
from qapp import views

urlpatterns = [
    path('', QuestionlistView.as_view(), name='qhome'),
    path('<int:pk>/', QuestiondetailView.as_view(), name='qdetail'),
    path('new/', QuestioncreateView.as_view(), name='qcreate'),
    path('<int:pk>/answer', AddAnswerView.as_view(), name='ans'),
    path('<int:pk>/update', QuestionupdateView.as_view(), name='qupdate'),
    path('<int:pk>/delete', QuestiondeleteView.as_view(), name='qdelete'),
    path('<int:pk>/adelete', AnswerdeleteView.as_view(), name='adelete'),
]
