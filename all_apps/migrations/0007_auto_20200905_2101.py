# Generated by Django 3.1 on 2020-09-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_apps', '0006_auto_20200905_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentquestion',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assignmentsubmit',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]