# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False)),
                ('descripcion', models.TextField()),
                ('fecha_creación', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
