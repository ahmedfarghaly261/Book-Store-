# Generated by Django 5.1.1 on 2024-09-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('romantic', 'romantic'), ('action', 'action'), ('drama', 'drama'), ('comedy', 'comedy')], default='romantic', max_length=50),
        ),
    ]
