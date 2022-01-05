from django.shortcuts import render
from django.views import generic
from catalog.models import Genre, Language, Author, Book, BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from catalog.forms import RenewBookForm
import datetime

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

@permission_required('catalog.can_reloan')
def renew_book(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renew_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('my-loans'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks = 3)
        form = RenewBookForm(initial = {'renew_date': proposed_renewal_date})
    
    context = {
      'form': form,
      'book_instance': book_instance,
    }

    return render(request, 'catalog/renew_book.html', context)