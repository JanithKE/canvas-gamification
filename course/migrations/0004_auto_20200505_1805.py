# Generated by Django 3.0.3 on 2020-05-06 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_question_max_submission_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('EASY', 'EASY'), ('NORMAL', 'NORMAL'), ('HARD', 'HARD')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tokenvalue',
            name='difficulty',
            field=models.CharField(choices=[('EASY', 'EASY'), ('NORMAL', 'NORMAL'), ('HARD', 'HARD')], max_length=100),
        ),
    ]
