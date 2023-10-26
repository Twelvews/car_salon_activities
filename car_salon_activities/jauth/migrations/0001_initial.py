# Generated by Django 4.1.3 on 2023-10-26 21:33


import django.core.validators
from django.db import models, migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        db_index=True,
                        max_length=32,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(8)],
                        verbose_name='username',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        db_index=True,
                        max_length=320,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name='email',
                    ),
                ),
                (
                    'password',
                    models.CharField(
                        max_length=128,
                        validators=[django.core.validators.MinLengthValidator(8)],
                        verbose_name='password',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name='first name'
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name='last name'
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
                ),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                (
                    'last_login',
                    models.DateTimeField(blank=True, null=True, verbose_name='last login'),
                ),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('is_verified', models.BooleanField(default=False, verbose_name='is verified')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'User',
            },
        ),
    ]
