# Generated by Django 4.0.4 on 2022-05-18 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0010_alter_extrainfo_celiac_alter_extrainfo_child_seat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='extra_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager_app.extrainfo', verbose_name='Dodatkowe informacje'),
        ),
    ]