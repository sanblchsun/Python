# Generated by Django 3.0.5 on 2020-05-09 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]