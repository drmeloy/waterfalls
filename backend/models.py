from django.db import models

class Waterfall(models.Model):
  name = models.CharField(max_length=100)
  height = models.CharField(max_length=10)
  longitude = models.CharField(max_length=10)
  latitude = models.CharField(max_length=10)
  description = models.TextField(blank=True)
  created_at = models.DateField(auto_now_add=True)
