# Generated by Django 4.2.4 on 2023-10-24 18:56

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerBio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_purpose', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Babycare'), (2, 'Cooking'), (3, 'Elderlycare'), (4, 'Others')], max_length=9)),
                ('partner_area', models.CharField(max_length=15)),
                ('partner_city', models.CharField(max_length=15)),
                ('partner_state', models.CharField(max_length=15)),
                ('partner_lon', models.DecimalField(decimal_places=4, default=0.0, max_digits=4)),
                ('partner_lat', models.DecimalField(decimal_places=4, default=0.0, max_digits=4)),
            ],
        ),
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
            name='UserBio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Purpose', models.IntegerField(choices=[(1, 'Babycare'), (2, 'Cooking'), (3, 'Elderlycare'), (4, 'Others')], max_length=1)),
                ('Area', models.CharField(max_length=15)),
                ('City', models.CharField(max_length=15)),
                ('State', models.CharField(max_length=15)),
                ('user_lon', models.DecimalField(decimal_places=4, default=0.0, max_digits=4)),
                ('user_lat', models.DecimalField(decimal_places=4, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=10)),
                ('Country', models.CharField(choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')], max_length=2)),
            ],
        ),
    ]
