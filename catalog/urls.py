from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('books/', views.BookListView.as_view(), name = 'books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name = 'book-detail'),
    path('myloans/', views.LoanedBooksByUserListView.as_view(), name = 'my-loans'),
    path('book/<uuid:pk>/renew/', views.renew_book, name = 'renew-book'),
    path('authors/', views.AuthorListView.as_view(), name = 'authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name = 'author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name = 'author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name = 'author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name = 'author-delete'),
]