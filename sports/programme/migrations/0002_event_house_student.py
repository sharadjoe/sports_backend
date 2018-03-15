# Generated by Django 2.0.2 on 2018-03-14 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('typeOfEvent', models.CharField(choices=[('G', 'Games'), ('A', 'Athletics')], max_length=1)),
                ('typeOfGender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme.Programme')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('reg_no', models.CharField(max_length=10)),
                ('event', models.ManyToManyField(to='programme.Event')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme.House')),
            ],
        ),
    ]
