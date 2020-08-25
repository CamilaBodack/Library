from rest_framework import serializers
from .models import Client, Author, Book, BookInstance, Genre


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("username", "email", "phone")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("first_name", "last_name")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "author", "summary", "isbn", "genre")


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ("id", "client", "book", "imprint", "due_back")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name")
