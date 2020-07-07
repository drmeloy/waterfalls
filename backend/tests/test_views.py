import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Waterfall
from ..serializers import WaterfallSerializer

client = Client()
