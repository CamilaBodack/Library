from rest_framework import serializers
from .models import Client,  Book


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("username", "email", "phone")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "client_id", "title", "author", "summary", "genre", "isbn", "date_movement", "delivery_date", "reserve", "status")
