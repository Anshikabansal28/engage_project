# Generated by Django 2.1.2 on 2018-10-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('headshot', models.ImageField(upload_to='author_headshots')),
            ],
            options={
                'ordering': ['email'],
            },
        ),
    ]
