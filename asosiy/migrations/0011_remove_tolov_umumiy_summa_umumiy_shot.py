# Generated by Django 4.1.9 on 2023-09-18 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0010_alter_tolov_umumiy_summa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tolov',
            name='umumiy_summa',
        ),
        migrations.CreateModel(
            name='Umumiy_shot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umumiy_summa', models.IntegerField()),
                ('asosiy_talabalar_safi_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.asosiy_talabalar_safi')),
            ],
        ),
    ]
