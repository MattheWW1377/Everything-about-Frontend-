# Generated by Django 4.1.5 on 2023-01-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('picture', models.ImageField(upload_to='geo/')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('pic1', models.ImageField(upload_to='main/')),
                ('pic2', models.ImageField(upload_to='main/')),
                ('pic3', models.ImageField(upload_to='main/')),
            ],
        ),
        migrations.CreateModel(
            name='Vos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('picture', models.ImageField(upload_to='vos/')),
            ],
        ),
    ]
