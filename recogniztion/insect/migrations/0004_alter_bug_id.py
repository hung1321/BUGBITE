# Generated by Django 4.2.7 on 2023-11-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insect', '0003_bug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
