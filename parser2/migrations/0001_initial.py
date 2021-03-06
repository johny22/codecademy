# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateTimeField(verbose_name='Data da conquista')),
                ('imgUrl', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('melhorP', models.IntegerField()),
                ('hoje', models.IntegerField()),
                ('dias_seg', models.IntegerField()),
                ('total_ponts', models.IntegerField()),
                ('data_extract', models.DateTimeField(verbose_name='Data de extração')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('melhorP', models.IntegerField()),
                ('hoje', models.IntegerField()),
                ('dias_seg', models.IntegerField()),
                ('total_ponts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('percent', models.IntegerField()),
                ('data', models.CharField(max_length=100)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser2.Perfil')),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser2.Perfil'),
        ),
        migrations.AddField(
            model_name='achievements',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser2.Perfil'),
        ),
    ]
