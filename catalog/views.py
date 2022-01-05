from django.shortcuts import render
from django.views import generic
from catalog.models import Genre, Language, Author, Book, BookInstance

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visitors = request.session.get('num_visitors', 0)
    request.session['num_visitors'] = num_visitors + 1

    context = {
      'num_books': num_books,
      'num_instances': num_instances,
      'num_instances_available': num_instances_available,
      'num_authors': num_authors, 
      'num_visitors': num_visitors,
    }

    return render(request, 'index.html', context = context)

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book