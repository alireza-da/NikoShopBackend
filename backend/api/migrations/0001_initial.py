# Generated by Django 4.1.2 on 2022-10-18 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tr_offer', to='api.offer')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tr_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tr_seender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
