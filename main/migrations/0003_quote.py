# Generated by Django 5.2 on 2025-04-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_footprint_delete_footprintrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(choices=[('motivational', 'Motivational'), ('fact', 'Fact'), ('warning', 'Warning')], default='fact', max_length=50)),
            ],
        ),
    ]
