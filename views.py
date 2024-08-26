from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
# Create your views here.
from bookapp.models import Book
from bookapp.forms import BookForm

class AddBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'addbook.html'
    success_url = '/booklist'

class BookList(ListView):
    model = Book
    template_name = 'booklist.html'

class BookDetails(DetailView):
    model = Book
    template_name='bookdetails.html'

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'update_book.html'
    success_url = '/booklist'

class BookDelete(DeleteView):
    model = Book
    template_name = 'book_delete_confirm.html'
    success_url = '/booklist'

class Details(DetailView):
    model = Book
    slug_field='slug'
    template_name='bookdetails.html'
    