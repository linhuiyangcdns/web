# Generated by Django 2.0.1 on 2018-08-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='国内名校', max_length=20, verbose_name='机构标签'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
    ]