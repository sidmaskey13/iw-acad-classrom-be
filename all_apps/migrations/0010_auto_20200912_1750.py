# Generated by Django 3.0.2 on 2020-09-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_apps', '0009_auto_20200912_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizscoredata',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quizscoredata',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
