# Generated by Django 2.2.3 on 2019-07-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_mymodel_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='image3',
            field=models.CharField(default=1, max_length=1140),
            preserve_default=False,
        ),
    ]
