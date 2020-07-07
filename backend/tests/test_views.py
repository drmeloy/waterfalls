import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Waterfall
from ..serializers import WaterfallSerializer

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

  # def test_get_waterfalls(self):
  #   response = self.client.get('/api/waterfalls/')
  #   self.assertEqual(json.loads(response.content), [{"id": 1, "name": "Super Falls", "height": "555 ft.", "longitude": "123 N", "latitude": "321 W", "description": "Super cool falls"}])