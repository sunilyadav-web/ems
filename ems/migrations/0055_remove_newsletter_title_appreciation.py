# Generated by Django 4.1 on 2022-09-30 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0054_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='title',
        ),
        migrations.CreateModel(
            name='Appreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems.employee')),
            ],
        ),
    ]
