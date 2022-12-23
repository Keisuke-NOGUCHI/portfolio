# Generated by Django 4.0.5 on 2022-11-09 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30, null=True)),
                ('t_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fri1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('fri2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('fri3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('fri4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('fri5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('fri6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('mon1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='月1')),
                ('mon2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='月2')),
                ('mon3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('mon4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('mon5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('mon6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('thu1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('thu2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('thu3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('thu4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('thu5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('thu6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('tue1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('tue2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('tue3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('tue4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('tue5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('tue6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('wed1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('wed2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('wed3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('wed4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('wed5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
                ('wed6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.subject', verbose_name='科目名')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='media/icon_images')),
                ('timetable', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.timetable', verbose_name='時間割')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userinfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]