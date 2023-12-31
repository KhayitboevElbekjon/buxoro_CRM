# Generated by Django 4.1.9 on 2023-07-13 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mavzu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100000)),
                ('description', models.TextField()),
                ('vaqt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Konfrensiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batafsil', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=100000)),
                ('vaqt', models.DateTimeField()),
                ('guruh', models.ManyToManyField(to='asosiy.guruh')),
            ],
        ),
        migrations.CreateModel(
            name='Davomat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('darsga_qatnashdi', models.BooleanField(default=False)),
                ('vaqt', models.DateTimeField()),
                ('asosiy_talabalar_safi_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.asosiy_talabalar_safi')),
                ('guruh_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.guruh')),
                ('mavzu_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.mavzu')),
            ],
        ),
        migrations.CreateModel(
            name='Baholash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_ball', models.SmallIntegerField()),
                ('max_ball', models.SmallIntegerField()),
                ('asosiy_talabalar_safi_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.asosiy_talabalar_safi')),
                ('guruh_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.guruh')),
                ('mavzu_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.mavzu')),
            ],
        ),
    ]
