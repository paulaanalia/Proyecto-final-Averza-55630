# Generated by Django 4.2.4 on 2023-09-01 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0003_review_delete_anfitrion_delete_categoria_delete_menu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='puntaje',
            new_name='valoracion',
        ),
    ]
