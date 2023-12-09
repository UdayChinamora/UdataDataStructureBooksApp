from django import forms
from .models import Book


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','published_date', 'price','status',]


class BookForm(forms.Form):
    book_title = forms.CharField(max_length=100)


class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=100)
