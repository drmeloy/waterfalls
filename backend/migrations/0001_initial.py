# Generated by Django 3.0.8 on 2020-07-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waterfall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=10)),
                ('longitude', models.CharField(max_length=10)),
                ('latitude', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]