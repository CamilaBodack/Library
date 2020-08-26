from django.test import TestCase
from bravo_library.models import Client, Book


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(username='Gomes Oliver', email='gomes@gomes.com',
                              phone='48-90102-0304', password='12345678')

    def test_username_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_email_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Email')

    def test_phone_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Phone Number')

    def test_password_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'Password')

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
        # Set up non-modified objects used by all test methods
        client = Client.objects.create(username='Gomes Oliver', email='gomes@gomes.com',
                                       phone='48-90102-0304', password='12345678')
        client.save()

        Book.objects.create(title='Historias de historias', author='Arari Hardh',
                            summay='Teste teste teste teste', genre='Historia do teste',
                            isbn='1236545648', date_movement='01-08-2020',
                            delivery_date='04-08-2020', client_id=client,
                            reserve=False, status="emprestado")

        def test_title_label(self):
            book = Book.objects.get(id=1)
            field_label = book._meta.get_field('title').verbose_name
            self.assertEquals(field_label, 'Title')

        def test_author_label(self):
            book = Book.objects.get(id=1)
            field_label = book._meta.get_field('author').verbose_name
            self.assertEquals(field_label, 'Author')

        def test_summary_label(self):
            book = Book.objects.get(id=1)
            field_label = book._meta.get_field('summary').verbose_name
            self.assertEquals(field_label, 'Book summary')

        def test_genre_label(self):
            book = Book.objects.get(id=1)
            field_label = book._meta.get_field('genre').verbose_name
            self.assertEquals(field_label, 'Genre')

        def test_isbn_label(self):
            book = Book.objects.get(id=1)
            field_label = book._meta.get_field('isbn').verbose_name
            self.assertEquals(field_label, 'ISBN')

        def test_date_movement_label(self):
            book = Book.objects.get(id=1)
            field_label = book._meta.get_field('date_movement').verbose_name
            self.assertEquals(field_label, 'Withdrawal date')

        def test_delivery_date_label(self):
            book = Book.objects.get(id=1)
            field_label = book._meta.get_field('delivery_date').verbose_name
            self.assertEquals(field_label, 'Delivery Date')

        def test_reserve_label(self):
            book = Book.objects.get(id=1)
            field_label = book._meta.get_field('reserve').verbose_name
            self.assertEquals(field_label, 'is reserved')

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
