# Generated by Django 4.1.5 on 2024-05-17 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0009_alter_strategyshares_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategyshares',
            name='strategy_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myportfolio.strategy'),
        ),
    ]
