# Generated by Django 4.2.7 on 2023-11-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_alter_section_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='priority',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]