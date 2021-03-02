# Generated by Django 3.1.3 on 2021-03-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('pub_date', models.DateTimeField()),
                ('reply', models.PositiveIntegerField()),
            ],
        ),
    ]
