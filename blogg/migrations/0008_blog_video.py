# Generated by Django 3.2 on 2021-04-23 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0007_alter_blog_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(blank=True, upload_to='videos/%Y'),
        ),
    ]
