# Generated by Django 3.2.2 on 2021-05-08 21:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='project'),
            preserve_default=False,
        ),
    ]