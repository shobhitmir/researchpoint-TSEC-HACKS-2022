# Generated by Django 3.2.12 on 2022-03-10 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0012_user_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='file',
            field=models.FileField(upload_to='upload/'),
        ),
    ]
