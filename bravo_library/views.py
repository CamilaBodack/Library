from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client, Book
from django.shortcuts import get_object_or_404
from .serializers import ClientSerializer, BookSerializer
from datetime import date, timedelta


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @api_view(['GET'])
    def book_tax(request, pk):
        client_id = pk
        book = get_object_or_404(Book, pk=client_id)
        delivery_date = Book.objects.filter(client_id=book.pk).filter(status="emprestado")

        for item in delivery_date:
            books_list = []
            day = (date.today() - item.delivery_date).days
            if(day < 1):
                books_list.append({"title": item.title, "tax": 0})
            elif(day >= 1 and day < 3):
                books_list.append({"title": item.title, "tax":  0.03 + (day * 0.002)})
            elif(day >= 3 and day < 5):
                books_list.append({"title": item.title, "tax":  0.05 + (day * 0.004)})
            else:
                books_list.append({"title": item.title, "tax":  0.07 + (day * 0.006)})
        return Response({"books": books_list})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @api_view(['GET'])
    def reserve(request, pk):
        book = get_object_or_404(Book, pk=pk)
        Book.objects.filter(pk=book.pk).update(reserve=True)
        return Response("Book reserved")
