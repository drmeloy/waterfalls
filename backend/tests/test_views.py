import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Waterfall
from ..serializers import WaterfallSerializer

class WaterfallApiGetTests(APITestCase):
  def setUp(self):
    Waterfall.objects.create(
      name='Super Falls', height='555 ft.', longitude='123 N', latitude='321 W', description='Super cool falls')
    Waterfall.objects.create(
      name='Lame Falls', height='7 ft.', longitude='987 S', latitude='789 E', description='Pretty lame falls')

  def test_get_all_waterfalls(self):
    response = self.client.get('/api/waterfalls/')
    waterfalls = Waterfall.objects.all()
    serializer = WaterfallSerializer(waterfalls, many=True)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_single_waterfall_valid(self):
    response = self.client.get('/api/waterfalls/1/')
    waterfall = Waterfall.objects.get(pk=1)
    serializer = WaterfallSerializer(waterfall)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_single_waterfall_invalid(self):
    response = self.client.get('/api/waterfalls/999/')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class WaterfallApiPostTests(APITestCase):
  def test_post_waterfall_valid_data(self):
    valid_data = {"name": "Super Falls", "height": "555 ft.", "longitude": "123 N", "latitude": "321 W", "description": "Super cool falls"}
    response = self.client.post('/api/waterfalls/', valid_data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_post_waterfall_invalid_data_no_name(self):
    invalid_data = {"name": "", "height": "555 ft.", "longitude": "123 N", "latitude": "321 W", "description": "Super cool falls"}
    response = self.client.post('/api/waterfalls/', invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_post_waterfall_invalid_data_no_height(self):
    invalid_data = {"name": "Super Falls", "height": "", "longitude": "123 N", "latitude": "321 W", "description": "Super cool falls"}
    response = self.client.post('/api/waterfalls/', invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_post_waterfall_invalid_data_no_longitude(self):
    invalid_data = {"name": "Super Falls", "height": "555 ft.", "longitude": "", "latitude": "321 W", "description": "Super cool falls"}
    response = self.client.post('/api/waterfalls/', invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_post_waterfall_invalid_data_no_latitude(self):
    invalid_data = {"name": "Super Falls", "height": "555 ft.", "longitude": "123 N", "latitude": "", "description": "Super cool falls"}
    response = self.client.post('/api/waterfalls/', invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class WaterfallApiPutTests(APITestCase):
  def setUp(self):
    Waterfall.objects.create(
      name='Super Falls', height='555 ft.', longitude='123 N', latitude='321 W', description='Super cool falls')

  def test_update_waterfall_valid(self):
    valid_data = {"name": "Mega Falls", "height": "1000 ft.", "longitude": "999 N", "latitude": "999 W", "description": "Mega awesome falls"}
    response = self.client.put('/api/waterfalls/1/', valid_data)
    waterfall = Waterfall.objects.get(pk=1)
    serializer = WaterfallSerializer(waterfall)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_update_waterfall_invalid_no_name(self):
    invalid_data = {"name": "", "height": "1000 ft.", "longitude": "999 N", "latitude": "999 W", "description": "Mega awesome falls"}
    response = self.client.put('/api/waterfalls/1/', invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_update_waterfall_invalid_no_height(self):
    invalid_data = {"name": "Mega Falls", "height": "", "longitude": "999 N", "latitude": "999 W", "description": "Mega awesome falls"}
    response = self.client.put('/api/waterfalls/1/', invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_update_waterfall_invalid_no_longitude(self):
    invalid_data = {"name": "Mega Falls", "height": "1000 ft.", "longitude": "", "latitude": "999 W", "description": "Mega awesome falls"}
    response = self.client.put('/api/waterfalls/1/', invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_update_waterfall_invalid_no_latitude(self):
    invalid_data = {"name": "Mega Falls", "height": "1000 ft.", "longitude": "999 N", "latitude": "", "description": "Mega awesome falls"}
    response = self.client.put('/api/waterfalls/1/', invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    