# Generated by Django 4.1.5 on 2024-04-24 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headLine', models.CharField(max_length=96)),
                ('source', models.CharField(blank=True, max_length=96)),
                ('url', models.URLField()),
                ('picture_url', models.URLField(blank=True)),
                ('referencedStocks', models.TextField(blank=True, help_text='Use this Colab https://colab.research.google.com/drive/1yhgrlksevpURUSeDHN9RnU-lqWELjeCi?usp=sharing', verbose_name='References to Stocks:')),
                ('stocksProcessed', models.BooleanField(default=False, verbose_name='Stocks already processed:')),
                ('summary', models.TextField(blank=True)),
                ('plannedAction', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Blog Entry',
                'verbose_name_plural': 'Blog Entries',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('priority', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Link Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=12)),
                ('sell', models.IntegerField(default=0)),
                ('neutral', models.IntegerField(default=0)),
                ('buy', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('searched_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Search History',
                'verbose_name_plural': 'Search History Entries',
            },
        ),
        migrations.CreateModel(
            name='shareIds',
            fields=[
                ('name', models.CharField(default='None', max_length=32, primary_key=True, serialize=False)),
                ('symbol', models.CharField(blank=True, max_length=12)),
                ('wkn', models.CharField(blank=True, default='None', max_length=6, unique=True)),
                ('isin', models.CharField(blank=True, default='None', max_length=12, unique=True)),
                ('isMainShare', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Share/Stock IDs',
                'verbose_name_plural': 'Share/Stock IDs',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myportfolio.category')),
            ],
        ),
        migrations.CreateModel(
            name='blog_shares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, default='xyz', max_length=96)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myportfolio.blogentry')),
                ('shares_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myportfolio.shareids')),
            ],
            options={
                'verbose_name': 'In Blog referenced Stocks',
                'verbose_name_plural': 'In Blog referenced Stocks',
                'unique_together': {('blog_id', 'shares_name')},
            },
        ),
    ]
