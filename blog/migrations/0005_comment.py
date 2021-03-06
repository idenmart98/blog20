# Generated by Django 3.2.8 on 2021-11-17 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
