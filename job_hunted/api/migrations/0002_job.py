# Generated by Django 2.0.6 on 2018-06-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=75)),
                ('company_name', models.CharField(max_length=120)),
                ('company_address', models.TextField()),
                ('job_description', models.TextField()),
            ],
        ),
    ]
