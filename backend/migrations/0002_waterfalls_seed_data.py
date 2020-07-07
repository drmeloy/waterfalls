# Generated by Django 3.0.8 on 2020-07-07 18:47

from django.db import migrations

def seed_data(apps, schema_editor):
  Waterfall = apps.get_model('backend', 'Waterfall')
  Waterfall(name='Silver Falls', height='178 ft', longitude='44.89 N', latitude='122.6461 W', description='Cool waterfall that you can hike behind!').save()

class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
      migrations.RunPython(seed_data),
    ]