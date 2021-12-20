from django.test import TestCase
from django.contrib.auth.models import User
from offers.models import *
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='owoc', ordering=100)
        test_offer = Offer.objects.create(title='banan', description='opis', price=65, category_id_id=1)

    def test_category_content(self):
        cat = Category.objects.get(id=1)
        offer = Offer.objects.get(id=1)
        name = f'{cat.name}'
        ordering = f'{cat.ordering}'
        title = f'{offer.title}'
        description = f'{offer.description}'
        price = f'{offer.price}'
        cat_id = f'{offer.category_id_id}'

        self.assertEqual(name, 'owoc')
        self.assertEqual(ordering, '100')
        self.assertEqual(str(cat), 'owoc')

        self.assertEqual(title, 'banan')
        self.assertEqual(description, 'opis')
        self.assertEqual(price, '65.00')
        self.assertEqual(cat_id, '1')
        self.assertEqual(str(offer), 'banan')


class TestEndpoints(APITestCase):

    def test_offers_get(self):

        url = reverse('offers:offers')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offers_post(self):

        self.test_category = Category.objects.create(name='owoc', ordering=100)
        data = {"title" : "oferta", "description": "opis", "price": "100", "category_id": "1"}
        url = reverse('offers:offers')

        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


