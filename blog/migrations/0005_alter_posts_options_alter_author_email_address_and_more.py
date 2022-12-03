# Generated by Django 4.0.6 on 2022-11-02 06:33

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_posts_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts Entity'},
        ),
        migrations.AlterField(
            model_name='author',
            name='Email_address',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.author'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 2, 6, 33, 15, 900163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]
