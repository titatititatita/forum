# Generated by Django 3.1.3 on 2021-03-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='reply',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
