# Generated by Django 4.1.5 on 2024-05-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0016_attrnames_attrnumber_attrnames_attrvalue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attrnames',
            name='attrDatum',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='attrnames',
            name='attrNumber',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='attrnames',
            name='attrValue',
            field=models.CharField(max_length=32),
        ),
    ]
