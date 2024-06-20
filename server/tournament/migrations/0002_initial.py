# Generated by Django 5.0.6 on 2024-06-18 16:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournament', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournamentresult',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentword',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='tournament.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentwordstatistic',
            name='tournament_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentwordstatistic',
            name='tournament_word_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournamentword'),
        ),
        migrations.AddField(
            model_name='tournmentparticipant',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournamentwordstatistic',
            name='participant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournmentparticipant'),
        ),
        migrations.AddField(
            model_name='tournamentresult',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournmentparticipant'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='participants',
            field=models.ManyToManyField(related_name='tournaments', to='tournament.tournmentparticipant'),
        ),
    ]
