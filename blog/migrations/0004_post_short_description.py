# Generated by Django 3.2.8 on 2021-11-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211115_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]