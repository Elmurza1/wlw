# Generated by Django 5.0.7 on 2024-07-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.TextField()),
                ('blog', models.TextField()),
                ('skills', models.TextField()),
                ('project', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('imgs', models.ImageField(upload_to='')),
                ('data', models.DateField()),
            ],
        ),
    ]
