# Generated by Django 5.0.4 on 2024-06-03 20:33

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('readed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('number_of_words', models.PositiveIntegerField()),
                ('start', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TournamentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('completion_time', models.DateTimeField(blank=True, null=True)),
                ('place', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('round_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TournamentWordStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.PositiveIntegerField()),
                ('entered_words', models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('guessed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TournmentParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
