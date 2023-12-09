import os

from django.db import models

# from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.myproject.settings')

from django.db import connection


def get_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM boards_user")
        users = cursor.fetchall()
    return users


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.ManyToManyField(Genre)
    image_url = models.ImageField(upload_to='books /', max_length=255, blank=True, null=True)
    # Add the status field with choices
    STATUS_CHOICES = [
        ("available", "Available"),
        ("borrowed", "Borrowed"),
        ("reserved", "Reserved"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="available")

    # Define a comparison method to compare books by title
    def __lt__(self, other):
        return self.title < other.title

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(default='Your comment here')


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name


class BookStore(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowing_date = models.DateField()
    return_date = models.DateField()


class Borrower(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    borrowed_books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


