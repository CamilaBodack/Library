from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client, Book
from django.shortcuts import get_object_or_404
from .serializers import ClientSerializer, BookSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @api_view(['GET'])
    def reserve(request, pk):
        book = get_object_or_404(Book, pk=pk)
        Book.objects.filter(pk=book.pk).update(reserve=True)
        return Response("Book reserved")
