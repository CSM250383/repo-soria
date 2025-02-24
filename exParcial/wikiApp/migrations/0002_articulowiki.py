# Generated by Django 5.1.3 on 2024-12-09 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='articuloWiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=128, null=True)),
                ('contenido', models.CharField(blank=True, max_length=1024, null=True)),
                ('temaRelacionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='wikiApp.temawiki')),
            ],
        ),
    ]
