from django.db import models

class Author(models.Model):
    """
    Author model:
    - name: authour's full name
    - Relationship: an Author can have many Books (one-to-many).
    """
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """ 
    Book model:
     - title; title of the book.
     - publication_year: integer year the book was published.
     - authour: ForeignKey to Author (related_name = 'books').
     """
    title = models.CharField(max_length = 500)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name = 'books', #lets us access author.books.all(0)
                               on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"

# Create your models here.
