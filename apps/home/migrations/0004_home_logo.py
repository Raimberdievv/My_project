# Generated by Django 3.2.7 on 2022-02-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_home_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo/'),
            preserve_default=False,
        ),
    ]
