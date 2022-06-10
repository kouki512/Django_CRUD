from django.shortcuts import render
from django.views.generic import( ListView, DetailView,CreateView,DeleteView,UpdateView,) #テンプレートの利用する際はここも追加する必要あり。
from django.urls import reverse_lazy
from .models import  Book 

class ListBookView(ListView):
    template_name = 'book/book_list.html'
    model = Book 

class DetailBookView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book
# Create your views here.

class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = {'title','text','category'}
    success_url = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
    templete_name = 'book/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')

class UpdateBookView(UpdateView):
    model = Book
    fields = {'title','text','category'}
    template_name = 'book/book_update.html'
    success_url = reverse_lazy('list-book')