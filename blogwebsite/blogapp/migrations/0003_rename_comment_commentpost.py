# Generated by Django 5.0.2 on 2024-03-25 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blogpost_category_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentPost',
        ),
    ]
