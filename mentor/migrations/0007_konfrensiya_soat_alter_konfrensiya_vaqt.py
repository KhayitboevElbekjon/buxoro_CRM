# Generated by Django 4.1.9 on 2023-07-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0006_remove_konfrensiya_guruh_konfrensiya_guruh'),
    ]

    operations = [
        migrations.AddField(
            model_name='konfrensiya',
            name='soat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='konfrensiya',
            name='vaqt',
            field=models.DateField(blank=True, null=True),
        ),
    ]