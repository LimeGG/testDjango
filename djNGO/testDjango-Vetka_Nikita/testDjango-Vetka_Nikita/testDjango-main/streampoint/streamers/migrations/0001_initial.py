# Generated by Django 4.1.6 on 2023-02-02 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lkusers', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllStreamers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя стримера')),
                ('photo', models.ImageField(upload_to='photostream/', verbose_name='Фото')),
                ('urltwitch', models.URLField(verbose_name='Ссылка на твич')),
                ('shop', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.shopstreamers')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lkusers.contribusers')),
            ],
            options={
                'verbose_name': 'Все стримеры',
                'verbose_name_plural': 'Все стримеры',
            },
        ),
    ]
