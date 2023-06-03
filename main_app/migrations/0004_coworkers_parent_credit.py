# Generated by Django 4.1.7 on 2023-02-17 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_mount_sellhistory_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='coworkers',
            name='parent',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_sell', models.IntegerField(default=0)),
                ('cash_amount', models.BigIntegerField(default=0)),
                ('coworker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.coworkers')),
            ],
        ),
    ]