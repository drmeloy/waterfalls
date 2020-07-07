from django.db import models

class Waterfall(models.Model):
  name = models.CharField(max_length=100)
  height = models.CharField(max_length=10)
  longitude = models.CharField(max_length=10)
  latitude = models.CharField(max_length=10)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def describe_waterfall(self):
    return self.name + ' is ' + self.height + ' tall and is located at ' + self.longitude + ' and ' + self.latitude + '.'