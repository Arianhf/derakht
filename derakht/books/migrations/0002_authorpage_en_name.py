# Generated by Django 4.2.5 on 2023-10-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorpage',
            name='en_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='english name'),
        ),
    ]