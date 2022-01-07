# Generated by Django 4.0.1 on 2022-01-07 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.users')),
            ],
        ),
    ]
