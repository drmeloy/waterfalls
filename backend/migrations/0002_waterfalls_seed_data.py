# Generated by Django 3.0.8 on 2020-07-07 18:47

from django.db import migrations

def seed_data(apps, schema_editor):
    Waterfall = apps.get_model('backend', 'Waterfall')
    Waterfall(
        name='Silver Falls (South Falls)',
        height='177 ft',
        latitude='44.87883',
        longitude='-122.65887',
        description="South Falls is THE waterfall in Silver Falls State Park. At 177 feet, it is the second tallest waterfall in the park, and it's the tallest single drop. It's easily accessed by a paved trail from the South Falls Lodge. A number of educational and historic markers dot the area, along with stone walls and benches carved from logs.").save()

class Migration(migrations.Migration):
    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
