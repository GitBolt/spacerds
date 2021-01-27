from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

from qapp.models import Questions, Answer


class QuestionlistView(ListView):
    model = Questions
    template_name = 'questions.html'
    context_object_name = 'questions'
    ordering = ['-date_posted']


class QuestiondetailView(DetailView):
    model = Questions
    template_name = 'qdetail.html'


class QuestioncreateView(LoginRequiredMixin, CreateView):
    model = Questions
    fields = ['title', 'content', ]
    template_name = 'qcreate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionupdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Questions
    fields = ['title', 'content']
    template_name = 'qcreate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        questions = self.get_object()
        if self.request.user == questions.author:
            return True
        return False


class QuestiondeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Questions
    success_url = '/questions/'
    template_name = 'qdelete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AddAnswerView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['body', 'date_added']
    template_name = 'ans.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('qdetail', kwargs={'pk': self.kwargs['pk']})


class AnswerdeleteView(DeleteView):
    model = Answer
    success_url = '/questions/'
    template_name = 'ansdel.html'

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.owner:
            return True
        return False
