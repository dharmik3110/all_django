# Generated by Django 3.2.5 on 2022-04-04 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'address1',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('city_name', models.CharField(max_length=30)),
                ('city_code', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('room_availability', models.BooleanField(default=True)),
                ('room_type', models.CharField(max_length=30, null=True)),
                ('room_sharing', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'roomcat',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('state_name', models.CharField(max_length=30)),
                ('state_code', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'State',
            },
        ),
        migrations.CreateModel(
            name='Pg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('pg_name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.city')),
                ('pg_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.address')),
                ('pg_rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.rooms')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.state')),
            ],
            options={
                'db_table': 'pg',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.city'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.state'),
        ),
    ]
