# Generated by Django 3.1.4 on 2020-12-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0008_auto_20201222_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='card_status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
