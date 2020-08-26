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
        delivery_date = Book.objects.filter(client_id=pk).filter(status="emprestado")

        for item in delivery_date:
            day = (date.today() - item.delivery_date).days
            if(day < 1):
                return Response("No tax")
            if(day >= 1 and day < 3):
                return Response("Tax = 3 % + (day * 0.2 %)")
            elif(day >= 3 and day < 5):
                return Response("Tax = 5 % + (day * 0.4 %)")
            else:
                return Response("Tax = 7 % + (day * 0.6 %)")


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @api_view(['GET'])
    def reserve(request, pk):
        book = get_object_or_404(Book, pk=pk)
        Book.objects.filter(pk=book.pk).update(reserve=True)
        return Response("Book reserved")
