# Generated by Django 4.2.7 on 2023-11-26 17:34

import uuid

import common.utils.file_upload_paths
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True, verbose_name="Email")),
                ("full_name", models.CharField(max_length=255, verbose_name="Full Name")),
                ("is_active", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False, verbose_name="Is Admin")),
                ("is_supplier", models.BooleanField(default=False, verbose_name="Is Supplier")),
                ("is_buyer", models.BooleanField(default=False, verbose_name="Is Buyer")),
                ("phone", models.CharField(max_length=20, verbose_name="Phone Number")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Added On")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Edited On")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("country", models.CharField(max_length=50, verbose_name="Country")),
                (
                    "state",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="State"
                    ),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="City"),
                ),
                ("postal_code", models.CharField(max_length=15, verbose_name="Postal Code")),
                ("address_1", models.CharField(max_length=255, verbose_name="Address Line 1")),
                (
                    "address_2",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Address Line 2"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SupplierProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=common.utils.file_upload_paths.suppliers_profile_pictures_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=[
                                    "jpg",
                                    "jpeg",
                                    "png",
                                    "webp",
                                    "gif",
                                    "tiff",
                                    "svg",
                                ]
                            )
                        ],
                        verbose_name="Profile Picture",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supplier_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BuyerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=common.utils.file_upload_paths.buyers_profile_pictures_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=[
                                    "jpg",
                                    "jpeg",
                                    "png",
                                    "webp",
                                    "gif",
                                    "tiff",
                                    "svg",
                                ]
                            )
                        ],
                        verbose_name="Profile Picture",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buyer_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="billing_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user_billing",
                to="account.address",
                verbose_name="Billing Address",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="shipping_address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user_shipping",
                to="account.address",
                verbose_name="Shipping Address",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]