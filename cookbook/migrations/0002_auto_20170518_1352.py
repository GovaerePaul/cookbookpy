# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField(verbose_name='Texte')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date du commentaire')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Etapes_Recette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte_etapes', models.TextField(verbose_name='Etapes de la recette')),
                ('ordre', models.IntegerField(verbose_name='ordre des étapes')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, verbose_name="Nom de l'ingrédient")),
            ],
        ),
        migrations.CreateModel(
            name='Liste_Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_ingredient', to='cookbook.Ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(verbose_name='Note de la recette')),
            ],
        ),
        migrations.AlterField(
            model_name='recette',
            name='type',
            field=models.CharField(choices=[('E', 'Entrée'), ('P', 'Plat principal'), ('D', 'Dessert')], max_length=1, verbose_name='type de plat'),
        ),
        migrations.AddField(
            model_name='note',
            name='recette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_recette', to='cookbook.Recette'),
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='liste_ingredients',
            name='recette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inredient_recette', to='cookbook.Recette'),
        ),
        migrations.AddField(
            model_name='etapes_recette',
            name='recette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etape_recette', to='cookbook.Recette'),
        ),
    ]
