# Generated by Django 3.2.16 on 2023-01-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_filter',
            field=models.CharField(choices=[('funny', 'Funny'), ('awesome', 'Awesome'), ('inspiration', 'Inspiration'), ('health', 'Health'), ('beautiful', 'Beautiful'), ('amazing', 'Amazing')], default='normal', max_length=32),
        ),
    ]
