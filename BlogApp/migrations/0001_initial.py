# Generated by Django 2.2 on 2019-05-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]