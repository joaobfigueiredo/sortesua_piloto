# Generated by Django 2.2.1 on 2019-05-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortesua', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aposta',
            name='validacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]