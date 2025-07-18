from django.db import models


class Author(models.Model):
     name = models.CharField(max_length=100)

     def __str__(self):
         return self.name

class Book(models.Model):
    title = models.charField(max_length = 200)
    author = models.ForeighKey(Author, on_delete-models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
     name = models.CharField(max_length = 100)
     books = models.ManyToManyField(Book)

     def __str__(self):
         return self.name

class Librarien(models.Model):
      name = models.CharField(max_length = 100)
      library = models.OneToOneField(Library, on_delete=models.CASCADE)

      def __str__(self):
          return self.name
# Create your models here.
