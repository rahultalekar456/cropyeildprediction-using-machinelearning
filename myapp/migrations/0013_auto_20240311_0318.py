# Generated by Django 3.1.7 on 2024-03-10 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20240311_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='consumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.consumer'),
        ),
    ]