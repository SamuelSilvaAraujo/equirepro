# Generated by Django 2.1.5 on 2019-01-28 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ancillary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('tipo', models.CharField(choices=[('GANHARAO', 'Ganharão'), ('DOADORA', 'Égua Doadora'), ('RECEPTORA', 'Égua Receptora')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CicloEstral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('egua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Haras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('observation', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Address')),
                ('proprietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='allocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Haras'),
        ),
        migrations.AddField(
            model_name='animal',
            name='ancillary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ancillary'),
        ),
        migrations.AddField(
            model_name='animal',
            name='proprietary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client'),
        ),
        migrations.AddField(
            model_name='animal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ancillary',
            name='haras',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Haras'),
        ),
        migrations.AddField(
            model_name='ancillary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
