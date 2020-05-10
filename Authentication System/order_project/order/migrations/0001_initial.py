# Generated by Django 3.0.5 on 2020-05-08 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('show_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_num', models.PositiveSmallIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('show_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Starter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starter_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('show_date', models.DateField(null=True)),
                ('tags', models.ManyToManyField(to='order.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.PositiveSmallIntegerField(unique=True)),
                ('num_guest', models.PositiveSmallIntegerField(default=1)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Floor')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('delivery_time', models.DateTimeField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('delivered', 'delivered')], max_length=20, null=True)),
                ('dessert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Dessert')),
                ('main', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Main')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Room')),
                ('starter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Starter')),
            ],
        ),
        migrations.AddField(
            model_name='main',
            name='tags',
            field=models.ManyToManyField(to='order.Tag'),
        ),
        migrations.AddField(
            model_name='dessert',
            name='tags',
            field=models.ManyToManyField(to='order.Tag'),
        ),
    ]
