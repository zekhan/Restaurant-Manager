# Generated by Django 4.0.4 on 2022-05-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0003_rename_date_hour_reservation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='celiac',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='child_seat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='dairy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='peanut_allergy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='vegan',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]
