# Generated by Django 4.2.6 on 2023-10-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_user_write", "0007_remove_userwritestage_can_create_users_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userwritestage",
            name="user_type",
            field=models.TextField(
                choices=[
                    ("internal", "Internal"),
                    ("external", "External"),
                    ("service_account", "Service Account"),
                    ("internal_service_account", "Internal Service Account"),
                ],
                default="external",
            ),
        ),
    ]