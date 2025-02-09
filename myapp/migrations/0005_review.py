# Generated by Django 3.2.23 on 2023-11-11 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField()),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.consumer')),
            ],
        ),
    ]
