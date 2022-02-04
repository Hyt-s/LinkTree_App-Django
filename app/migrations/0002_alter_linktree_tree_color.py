# Generated by Django 4.0.1 on 2022-02-04 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linktree',
            name='tree_color',
            field=models.CharField(choices=[('AQ', 'aqua'), ('BL', 'blue'), ('BR', 'brown'), ('GO', 'gold'), ('GE', 'green'), ('OR', 'orange'), ('PI', 'pink'), ('PU', 'purple'), ('RE', 'red'), ('VI', 'violet')], default='BL', max_length=30),
        ),
    ]