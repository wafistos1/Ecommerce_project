# Generated by Django 3.0.7 on 2020-06-17 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200617_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='discriptions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]