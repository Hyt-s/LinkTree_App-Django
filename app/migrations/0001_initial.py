# Generated by Django 4.0.1 on 2022-01-30 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkTree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_title', models.CharField(max_length=50)),
                ('tree_description', models.TextField()),
                ('tree_color', models.CharField(choices=[('BL', 'black'), ('BU', 'blue'), ('BR', 'brown'), ('GR', 'gray'), ('GE', 'green'), ('OR', 'orange'), ('PI', 'pink'), ('PU', 'purple'), ('RE', 'red'), ('YE', 'yellow')], default='BU', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=50)),
                ('link_url', models.TextField()),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trees', to='app.linktree')),
            ],
        ),
    ]
