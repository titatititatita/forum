# Generated by Django 3.1.3 on 2021-03-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20210302_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='text',
            field=models.TextField(default='Forgot to write smth'),
        ),
    ]