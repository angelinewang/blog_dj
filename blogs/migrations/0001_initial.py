# Generated by Django 4.1.3 on 2022-11-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('content', models.CharField(max_length=5000)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
