# Generated by Django 4.2.4 on 2023-08-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='altura',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casa',
            name='horario',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='casa',
            name='piso',
            field=models.IntegerField(null=True),
        ),
    ]