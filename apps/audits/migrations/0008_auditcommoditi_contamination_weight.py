# Generated by Django 5.2 on 2025-05-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0007_audit_is_waiver_applied_audit_waiver_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditcommoditi',
            name='contamination_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
