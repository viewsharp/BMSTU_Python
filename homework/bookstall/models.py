from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('first_name', 'last_name')


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author)
    image = models.ImageField(upload_to='static/books')
    year = models.IntegerField(default= None)
    count = models.IntegerField(default= 0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', 'image', 'year', 'count')