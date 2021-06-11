# Generated by Django 3.2.4 on 2021-06-11 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=15, unique=True)),
                ('bill_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('p_username', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('p_first_name', models.CharField(max_length=50)),
                ('p_last_name', models.CharField(max_length=50)),
                ('p_email', models.EmailField(max_length=100, unique=True)),
                ('p_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph_id', models.CharField(max_length=15, unique=True)),
                ('ph_first_name', models.CharField(max_length=50)),
                ('ph_last_name', models.CharField(max_length=50)),
                ('ph_speciality', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reseptionist',
            fields=[
                ('r_username', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('r_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brightside.physician')),
            ],
        ),
        migrations.CreateModel(
            name='Ph_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brightside.physician')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brightside.service')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_id', models.CharField(max_length=15, unique=True)),
                ('total_pay', models.CharField(max_length=15)),
                ('payment_date', models.DateTimeField(null=True)),
                ('status', models.IntegerField(choices=[(0, 'Paid'), (1, 'Unpaid')], default=1)),
                ('payment_method', models.IntegerField(choices=[(0, 'Paid'), (1, 'Unpaid')], default=0)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brightside.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.CharField(max_length=15, unique=True)),
                ('appointment_date', models.DateField(null=True)),
                ('appointment_time', models.TimeField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brightside.patient')),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brightside.physician')),
                ('reseptionist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brightside.reseptionist')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brightside.service')),
            ],
        ),
    ]
