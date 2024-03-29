# Generated by Django 5.0.2 on 2024-02-09 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, help_text="Ajouter l'image de l'auteur", null=True, upload_to='authorsImage')),
                ('biographie', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField(help_text='Ajouter un bref résumé du livre')),
                ('image', models.ImageField(blank=True, help_text='Ajouter une image', null=True, upload_to='images/')),
                ('en_stock', models.BooleanField(default=True)),
                ('date_d_ajout', models.DateField(auto_now_add=True)),
                ('date_publication', models.DateField(help_text='Entrer la date de la publication')),
                ('date_update', models.DateField(auto_now=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.auteur')),
                ('categorie', models.ManyToManyField(help_text='Choisissez la catégorie du livre', to='catalogue.categorie')),
            ],
        ),
    ]
