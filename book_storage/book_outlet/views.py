from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from book_outlet.models import Book
from django.urls import reverse
from django.db.models import Avg


# Create your views here.

def index(request):
    books = Book.objects.all()

    books_count = books.count()
    avg_rating = books.aggregate(Avg('rating'))

    return render(request, 'book_outlet/index.html', {
        'books': books,
        'books_count': books_count,
        'avg_rating': avg_rating,
    })

def detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    print(book)
    return HttpResponseRedirect(reverse('book-page-slug', kwargs={'book_slug': book.slug}))

def detail_slug(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    return render(request, 'book_outlet/book-detail.html', {'book': book})