# Generated by Django 2.1.5 on 2019-04-01 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190228_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cicloestral',
            name='date',
            field=models.DateField(default='01/04/2019', verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='haras',
            name='proprietary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client', verbose_name='Proprietário'),
        ),
    ]
