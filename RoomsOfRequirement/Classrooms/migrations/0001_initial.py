# Generated by Django 2.1.7 on 2019-03-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('class_id', models.IntegerField(
                    primary_key=True, serialize=False)),
                ('classroom', models.TextField()),
                ('weekday', models.TextField()),
                ('start_time', models.TextField()),
                ('end_time', models.TextField()),
            ],
            options={
                'db_table': 'CLASSROOM',
                'managed': False,
            },
        ),
    ]
