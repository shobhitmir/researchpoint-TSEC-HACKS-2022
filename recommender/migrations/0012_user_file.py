# Generated by Django 3.2.12 on 2022-03-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0011_auto_20220310_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file',
            field=models.FileField(default=1234, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
