# Generated by Django 2.0.1 on 2018-08-18 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_courseorg_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='teachers',
            field=models.IntegerField(default=0, verbose_name='教师数'),
        ),
    ]