# Generated by Django 4.0.4 on 2022-05-12 19:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0006_alter_reservation_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Utworzono'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='extra_info',
            field=models.ManyToManyField(through='manager_app.ReservationExtraInfo', to='manager_app.extrainfo', verbose_name='Dodatkowe informacje'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_number',
            field=models.PositiveIntegerField(verbose_name='Ilość gości'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='hour',
            field=models.TimeField(choices=[(datetime.time(10, 0), datetime.time(10, 0)), (datetime.time(10, 15), datetime.time(10, 15)), (datetime.time(10, 30), datetime.time(10, 30)), (datetime.time(10, 45), datetime.time(10, 45)), (datetime.time(11, 0), datetime.time(11, 0)), (datetime.time(11, 15), datetime.time(11, 15)), (datetime.time(11, 30), datetime.time(11, 30)), (datetime.time(11, 45), datetime.time(11, 45)), (datetime.time(12, 0), datetime.time(12, 0)), (datetime.time(12, 15), datetime.time(12, 15)), (datetime.time(12, 30), datetime.time(12, 30)), (datetime.time(12, 45), datetime.time(12, 45)), (datetime.time(13, 0), datetime.time(13, 0)), (datetime.time(13, 15), datetime.time(13, 15)), (datetime.time(13, 30), datetime.time(13, 30)), (datetime.time(13, 45), datetime.time(13, 45)), (datetime.time(14, 0), datetime.time(14, 0)), (datetime.time(14, 15), datetime.time(14, 15)), (datetime.time(14, 30), datetime.time(14, 30)), (datetime.time(14, 45), datetime.time(14, 45)), (datetime.time(15, 0), datetime.time(15, 0)), (datetime.time(15, 15), datetime.time(15, 15)), (datetime.time(15, 30), datetime.time(15, 30)), (datetime.time(15, 45), datetime.time(15, 45)), (datetime.time(16, 0), datetime.time(16, 0)), (datetime.time(16, 15), datetime.time(16, 15)), (datetime.time(16, 30), datetime.time(16, 30)), (datetime.time(16, 45), datetime.time(16, 45)), (datetime.time(17, 0), datetime.time(17, 0)), (datetime.time(17, 15), datetime.time(17, 15)), (datetime.time(17, 30), datetime.time(17, 30)), (datetime.time(17, 45), datetime.time(17, 45)), (datetime.time(18, 0), datetime.time(18, 0)), (datetime.time(18, 15), datetime.time(18, 15)), (datetime.time(18, 30), datetime.time(18, 30)), (datetime.time(18, 45), datetime.time(18, 45)), (datetime.time(19, 0), datetime.time(19, 0)), (datetime.time(19, 15), datetime.time(19, 15)), (datetime.time(19, 30), datetime.time(19, 30)), (datetime.time(19, 45), datetime.time(19, 45)), (datetime.time(20, 0), datetime.time(20, 0)), (datetime.time(20, 15), datetime.time(20, 15)), (datetime.time(20, 30), datetime.time(20, 30)), (datetime.time(20, 45), datetime.time(20, 45)), (datetime.time(21, 0), datetime.time(21, 0)), (datetime.time(21, 15), datetime.time(21, 15)), (datetime.time(21, 30), datetime.time(21, 30)), (datetime.time(21, 45), datetime.time(21, 45)), (datetime.time(22, 0), datetime.time(22, 0)), (datetime.time(22, 15), datetime.time(22, 15)), (datetime.time(22, 30), datetime.time(22, 30)), (datetime.time(22, 45), datetime.time(22, 45)), (datetime.time(23, 0), datetime.time(23, 0))], null=True, verbose_name='Godzina'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager_app.menu', verbose_name='Menu'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Nazwa rezerwacji'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager_app.table', verbose_name='Stół'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano'),
        ),
    ]
