# Generated by Django 3.2.5 on 2022-08-12 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0005_courseviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseviews',
            name='courseid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseviewers', to='webapi.category'),
        ),
    ]