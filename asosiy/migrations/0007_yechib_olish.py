# Generated by Django 4.1.9 on 2023-09-13 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0006_kurs_summa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yechib_olish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oy_nomi', models.CharField(max_length=60)),
                ('kurs_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.kurs')),
                ('tolov_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.tolov')),
            ],
        ),
    ]
