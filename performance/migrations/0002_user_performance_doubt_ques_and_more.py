# Generated by Django 4.2.4 on 2024-04-21 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_performance',
            name='doubt_ques',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_performance',
            name='important_ques',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_performance',
            name='star_ques',
            field=models.TextField(null=True),
        ),
    ]