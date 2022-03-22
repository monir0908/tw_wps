# Generated by Django 3.2.12 on 2022-03-22 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shift_title', models.CharField(max_length=250)),
                ('shift_start', models.TimeField(blank=True)),
                ('shift_end', models.TimeField(blank=True)),
                ('shift_session', models.CharField(max_length=250)),
                ('shift_short_code', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'ACTIVE'), (0, 'DEACTIVE')], default=1)),
                ('added_by', models.ForeignKey(db_column='added_by', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shifts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='WorkerShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shift.shift')),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'worker_shifts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='workershift',
            index=models.Index(fields=['-created_at'], name='worker_shif_created_c83976_idx'),
        ),
        migrations.AddIndex(
            model_name='shift',
            index=models.Index(fields=['shift_title'], name='shifts_shift_t_b7a0bb_idx'),
        ),
        migrations.AddIndex(
            model_name='shift',
            index=models.Index(fields=['shift_session'], name='shifts_shift_s_9f39f0_idx'),
        ),
        migrations.AddIndex(
            model_name='shift',
            index=models.Index(fields=['-created_at'], name='shifts_created_1b152b_idx'),
        ),
    ]
