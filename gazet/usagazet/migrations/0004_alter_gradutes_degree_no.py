# Generated by Django 4.2.3 on 2023-08-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usagazet", "0003_alter_gradutes_session_completion_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gradutes",
            name="degree_no",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
