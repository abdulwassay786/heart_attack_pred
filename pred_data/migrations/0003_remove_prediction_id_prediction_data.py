# Generated by Django 5.0.1 on 2024-01-03 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred_data', '0002_prediction_rename_cholestrol_data_cholesterol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='id',
        ),
        migrations.AddField(
            model_name='prediction',
            name='data',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pred_data.data'),
            preserve_default=False,
        ),
    ]
