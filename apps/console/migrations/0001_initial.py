# Generated by Django 5.0.6 on 2024-05-19 15:20

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (1, 'Active'), (3, 'Pending')], default=1)),
                ('timezone', models.CharField(default='America/New_York', max_length=64)),
                ('street_1', models.CharField(blank=True, max_length=1024, null=True)),
                ('street_2', models.CharField(blank=True, max_length=1024, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(default='US', max_length=50)),
                ('stripe_customer_id', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('password_reset_token', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'db_table': 'core_member',
            },
        ),
        migrations.CreateModel(
            name='CoreNotificationEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=256)),
                ('status', models.IntegerField(choices=[(0, 'Un-Verified'), (1, 'Verified'), (2, 'Hard bounce'), (3, 'Spam complaint')], default=0)),
                ('verify_code', models.CharField(max_length=256, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_email', to='console.coremember')),
            ],
            options={
                'db_table': 'core_notification_email',
            },
        ),
        migrations.CreateModel(
            name='CoreNotificationLogEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(editable=False, max_length=254)),
                ('text_body', models.TextField(editable=False, null=True)),
                ('html_body', models.TextField(editable=False, null=True)),
                ('subject', models.TextField(editable=False, null=True)),
                ('context', models.JSONField(editable=False, null=True)),
                ('template', models.CharField(max_length=1024, null=True)),
                ('message_id', models.CharField(max_length=1024, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_log_email', to='console.coremember')),
            ],
            options={
                'db_table': 'core_notification_log_email',
            },
        ),
        migrations.AddConstraint(
            model_name='corenotificationemail',
            constraint=models.UniqueConstraint(fields=('member', 'email'), name='unique_account_notification'),
        ),
    ]
