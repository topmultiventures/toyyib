# Generated by Django 5.0.6 on 2024-07-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reg_number', models.CharField(max_length=20, unique=True)),
                ('dept', models.CharField(choices=[('APH', 'Animal Science'), ('CSC', 'Computer Science'), ('MTH', 'Mathematics')], default='APH', max_length=30)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
