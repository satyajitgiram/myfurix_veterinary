# Generated by Django 4.2.11 on 2024-03-19 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('content', models.TextField()),
            ],
        ),
    ]
