# Generated by Django 4.1.5 on 2024-05-17 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0007_strategy_strategyshares_alter_attrnames_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='strategy',
            options={'verbose_name_plural': 'My Strategies'},
        ),
        migrations.AlterModelOptions(
            name='strategyshares',
            options={'verbose_name_plural': 'Shares for Strategy'},
        ),
        migrations.AddField(
            model_name='strategyshares',
            name='shares_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myportfolio.shareids'),
        ),
        migrations.AddField(
            model_name='strategyshares',
            name='strategy_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myportfolio.strategy'),
        ),
    ]