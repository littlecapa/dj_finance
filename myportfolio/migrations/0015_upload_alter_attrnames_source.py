# Generated by Django 4.1.5 on 2024-05-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0014_rename_transactions_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('uploadData', models.CharField(choices=[('comdirect', 'Comdirect'), ('comdirect portfolio', 'Comdirect Portfolio'), ('es', 'Effektenspiegel'), ('scalable', 'Scalable')], max_length=32, primary_key=True, serialize=False)),
                ('info', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='attrnames',
            name='source',
            field=models.CharField(choices=[('comdirect', 'Comdirect'), ('comdirect portfolio', 'Comdirect Portfolio'), ('es', 'Effektenspiegel'), ('scalable', 'Scalable')], max_length=32, primary_key=True, serialize=False),
        ),
    ]