# Generated by Django 4.1.5 on 2024-04-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_remove_blog_shares_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareids',
            name='isin',
            field=models.CharField(blank=True, default='None', max_length=12),
        ),
        migrations.AlterField(
            model_name='shareids',
            name='wkn',
            field=models.CharField(blank=True, default='None', max_length=6),
        ),
    ]