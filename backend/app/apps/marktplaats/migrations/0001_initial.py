# Generated by Django 3.2 on 2021-11-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarListingModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('brand_model', models.CharField(max_length=50)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('fuel_type', models.CharField(max_length=50)),
                ('year_of_construction', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(max_length=50)),
                ('apk_till', models.CharField(max_length=50)),
                ('wheel_base', models.CharField(max_length=50)),
                ('engine_capacity', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'CarListings',
                'managed': True,
            },
        ),
    ]
