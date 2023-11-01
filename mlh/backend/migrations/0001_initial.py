# Generated by Django 4.2.4 on 2023-11-01 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=20)),
                ('partner_phone', models.CharField(max_length=10)),
                ('partner_country', models.CharField(choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(max_length=10)),
                ('Country', models.CharField(choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')], max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Purpose', models.IntegerField(choices=[(1, 'Babycare'), (2, 'Cooking'), (3, 'Elderlycare'), (4, 'Others')])),
                ('Area', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=10)),
                ('user_lon', models.FloatField()),
                ('user_lat', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerBio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_purpose', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Babycare'), (2, 'Cooking'), (3, 'Elderlycare'), (4, 'Others')], max_length=9)),
                ('partner_area', models.CharField(max_length=10)),
                ('partner_city', models.CharField(max_length=10)),
                ('partner_state', models.CharField(max_length=10)),
                ('partner_lon', models.FloatField()),
                ('partner_lat', models.FloatField()),
                ('partner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.partnerinfo')),
            ],
        ),
    ]
