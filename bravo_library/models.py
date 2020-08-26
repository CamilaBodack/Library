from django.db import models
from django.core.validators import MinLengthValidator


class Client(models.Model):
    username = models.CharField("Name", max_length=50)
    email = models.EmailField("Email")
    phone = models.CharField("Phone Number", default=0,  max_length=50)
    password = models.CharField("Password", max_length=50,
                                validators=[MinLengthValidator])

    def __str__(self):
        return self.id, self.username


class Book(models.Model):
    title = models.CharField("Title", default=0, max_length=200)
    author = models.CharField('Author', default=0,  max_length=100)
    summary = models.TextField("Book summary", default=0,  max_length=1000)
    genre = models.CharField("Genre", default=0, max_length=50)
    isbn = models.CharField('ISBN', default=0, max_length=13)
    date_movement = models.DateField("Withdrawal date", auto_now=True)
    delivery_date = models.DateField("Delivery Date", auto_now=False)
    client_id = models.ForeignKey(Client, on_delete=models.SET_NULL,
                                  null=True)
    reserve = models.BooleanField("is reserved", default=False)
    STATUS = (
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS,
        blank=True,
        default='disponivel',
    )

    def __str__(self):
        return self.id, self.title, self.status
