from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Digite um gênero de livro')

    def __str__(self):
        return self.name

class Language(models.Model):
    nome = models.CharField(max_length = 200, help_text = "Digite a linguagem do livro")

    def __str__(self):
        return self.nome

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Morreu', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        permissions = (('can_handle_author', "Handle author record."),)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Book(models.Model): 
    title = models.CharField(max_length = 200)
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
    summary = models.TextField(max_length = 1000, help_text = 'Digite uma pequena descrição do livro')
    isbn = models.CharField('ISBN', max_length = 13)
    genre = models.ManyToManyField(Genre, help_text = 'Selecione um gênero para este livro')
    Language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args = [str(self.id)])
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID do livro')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)

    LOAN_STATUS = (
        ('m', 'Manutenção'),
        ('o', 'Emprestado'),
        ('a', 'Disponível'),
        ('r', 'Reservado'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Avaliabilidade do livro',
    )

    @property
    def late(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    class Meta:
        ordering = ['due_back']
        permissions = (('can_reloan', 'You can renew this book loan.'), )

    def __str__(self):
        return f'{self.id} ({self.book.title})'

