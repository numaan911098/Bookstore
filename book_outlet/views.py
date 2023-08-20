from django.shortcuts import get_object_or_404 ,render
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    number_of_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'index.html',{'books':books,
                                         'number_of_books':number_of_books,
                                         'avg_rating':avg_rating
                                         })

def bookdetails(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book-details.html',{
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
    })