from django.shortcuts import render
from django.views import generic
from catalog.models import Genre, Language, Author, Book, BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin

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

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/user_loaned_books.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(user = self.request.user).filter(status__exact = 'o').order_by('due_back')
