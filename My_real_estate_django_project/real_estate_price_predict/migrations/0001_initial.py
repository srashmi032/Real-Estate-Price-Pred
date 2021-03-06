# Generated by Django 2.0 on 2022-06-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CRIM', models.FloatField()),
                ('ZN', models.FloatField()),
                ('INDUS', models.FloatField()),
                ('CHAS', models.FloatField()),
                ('NOX', models.FloatField()),
                ('RM', models.FloatField()),
                ('AGE', models.FloatField()),
                ('DIS', models.FloatField()),
                ('RAD', models.FloatField()),
                ('TAX', models.FloatField()),
                ('PTRATIO', models.FloatField()),
                ('B', models.FloatField()),
                ('LSTAT', models.FloatField()),
            ],
        ),
    ]
