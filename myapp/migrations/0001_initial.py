# Generated by Django 4.1.5 on 2023-03-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.FileField(blank=True, max_length=300, null=True, upload_to='')),
                ('Details', models.CharField(max_length=20)),
                ('Model', models.CharField(max_length=20)),
                ('Color', models.CharField(max_length=20)),
                ('CarNumber', models.CharField(max_length=20)),
                ('Seats', models.IntegerField()),
                ('DriverCharge', models.CharField(max_length=20)),
                ('OnroadCharge', models.CharField(max_length=20)),
                ('ACCharge', models.CharField(max_length=20)),
                ('offer', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'addcars',
            },
        ),
        migrations.CreateModel(
            name='adminlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'adminlog',
            },
        ),
        migrations.CreateModel(
            name='bkdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=20)),
                ('Lastname', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('Mobnum', models.CharField(max_length=20)),
                ('Pickuploc', models.CharField(max_length=20)),
                ('Droploc', models.CharField(max_length=20)),
                ('Pickdate', models.CharField(max_length=20)),
                ('Picktime', models.CharField(max_length=20)),
                ('NumofPersons', models.CharField(max_length=20)),
                ('Ac', models.CharField(max_length=20)),
                ('Request', models.CharField(max_length=300)),
                ('Payment', models.CharField(max_length=50)),
                ('carno', models.CharField(max_length=50)),
                ('offer', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='customerreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tblcustreg',
            },
        ),
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=100)),
                ('Cusfeedback', models.CharField(max_length=200)),
                ('Answer', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carid', models.CharField(max_length=200)),
                ('carnumber', models.CharField(max_length=200)),
                ('offer', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tblcaroffer',
            },
        ),
        migrations.CreateModel(
            name='triparea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tbltriparea',
            },
        ),
    ]
