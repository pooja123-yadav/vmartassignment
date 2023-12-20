# Generated by Django 5.0 on 2023-12-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.PositiveIntegerField(db_index=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=1, null=True)),
                ('country_code', models.CharField(default='91', max_length=3)),
                ('phone_number', models.CharField(db_index=True, max_length=20)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=150, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
                ('updated_by', models.IntegerField(db_index=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField(db_index=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('expiry_date', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(db_index=True, null=True)),
                ('updated_by', models.IntegerField(db_index=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User Password',
                'verbose_name_plural': 'User Password',
                'db_table': 'user_password',
            },
        ),
    ]
