from django.test import TestCase
from bravo_library.models import Client, Book


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(username='Gomes Oliver', email='gomes@gomes.com',
                              phone='48-90102-0304', password='12345678')

    def test_username_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('username').max_length
        self.assertEquals(max_length, 50)

    def test_phone_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('phone').max_length
        self.assertEquals(max_length, 50)

    def test_password_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('password').max_length
        self.assertEquals(max_length, 50)


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(username='Gomes Oliver', email='gomes@gomes.com',
                                       phone='48-90102-0304', password='12345678')
        client.save()

        Book.objects.create(title='Historias de historias', author='Arari Hardh',
                            summay='Teste teste teste teste', genre='Historia do teste',
                            isbn='1236545648', date_movement='01-08-2020',
                            delivery_date='04-08-2020', client_id=client,
                            reserve=False, status="emprestado")


        def test_title_length(self):
            book = Book.objects.get(id=1)
            max_length = book._meta.get_field('title').max_length
            self.assertEquals(max_length, 200)

        def test_author_length(self):
            book = Book.objects.get(id=1)
            max_length = book._meta.get_field('author').max_length
            self.assertEquals(max_length, 100)

        def test_summary_length(self):
            book = Book.objects.get(id=1)
            max_length = book._meta.get_field('summary').max_length
            self.assertEquals(max_length, 1000)

        def test_genre_length(self):
            book = Book.objects.get(id=1)
            max_length = book._meta.get_field('genre').max_length
            self.assertEquals(max_length, 50)

        def test_isbn_length(self):
            book = Book.objects.get(id=1)
            max_length = book._meta.get_field('isbn').max_length
            self.assertEquals(max_length, 13)

        def test_status_length(self):
            book = Book.objects.get(id=1)
            max_length = book._meta.get_field('status').max_length
            self.assertEquals(max_length, 30)
