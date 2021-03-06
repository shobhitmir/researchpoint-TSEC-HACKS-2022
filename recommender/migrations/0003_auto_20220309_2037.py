# Generated by Django 3.2.12 on 2022-03-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0002_paper_upvote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='paper_title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='paper_abstract',
            new_name='abstracts',
        ),
        migrations.AddField(
            model_name='paper',
            name='Year',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='categories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='cleaned_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
