# Generated by Django 3.1.3 on 2020-11-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201116_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycle',
            name='is_locked',
            field=models.BooleanField(),
        ),
    ]
