# Generated by Django 5.0.7 on 2024-08-06 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transactions_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]