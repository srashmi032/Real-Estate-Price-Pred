# Generated by Django 2.0 on 2022-06-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20220623_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='B',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='CHAS',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='CRIM',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='DIS',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='INDUS',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='LSTAT',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='NOX',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='PTRATIO',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='RAD',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='RM',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='TAX',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='price',
            name='ZN',
            field=models.FloatField(default=0.0),
        ),
    ]
