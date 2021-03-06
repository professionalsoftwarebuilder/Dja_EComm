# Generated by Django 3.0.5 on 2020-06-04 17:21

import core.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200417_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Adres', 'verbose_name_plural': 'adressen'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Merk', 'verbose_name_plural': 'Merken'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categorie', 'verbose_name_plural': 'categorien'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Producten'},
        ),
        migrations.AddField(
            model_name='item',
            name='itm_Afmetingen',
            field=models.CharField(blank=True, default='', help_text='Afmetingen van het product (lxhxb)', max_length=85, verbose_name='Afmetingen lxhxb'),
        ),
        migrations.AddField(
            model_name='item',
            name='itm_Materiaal',
            field=models.CharField(blank=True, default='', help_text='Materiaal waaruit het product is vervaardigd', max_length=120, verbose_name='Materiaal'),
        ),
        migrations.AlterField(
            model_name='fotoset',
            name='fst_Title',
            field=models.CharField(blank=True, default='', help_text='Bijvoorbeeld: Vooraanzicht, zijkant, enz.', max_length=100, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Product omschrijving', verbose_name='Omschrijving'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=core.fields.ImageThumbsField(blank=True, help_text='Afbeelding die in catalogus gebruikt wordt', max_length=250, null=True, sizes=({'code': 'thumb', 'resize': 'crop', 'wxh': '69x100'}, {'code': 'galry', 'resize': 'crop', 'wxh': '400x580'}, {'code': 'detail', 'wxh': '552x800'}), upload_to='', verbose_name='Hoofd afbeelding'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_Brand_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Brand', verbose_name='Merk'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_Categories',
            field=models.ManyToManyField(to='core.Category', verbose_name='Categorie'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_Ctrl',
            field=models.CharField(blank=True, default='', help_text='Systeemveld, Dit veld niet wijzigen', max_length=30, verbose_name='Controlfield'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_IndexNr',
            field=models.IntegerField(blank=True, default=0, help_text='Volgorde van weergave', verbose_name='Volgorde'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_Is_Frontpage',
            field=models.BooleanField(blank=True, default=True, verbose_name='Voorpagina J/N (Featured)'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_Is_Newasset',
            field=models.BooleanField(blank=True, default=True, verbose_name='Nieuw binnen J/N'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_Is_Sale',
            field=models.BooleanField(blank=True, default=True, verbose_name='Sale J/N'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_Is_Show',
            field=models.BooleanField(blank=True, default=True, help_text='Door uit te zetten wordt dit product niet meer getoond (gedeactiveerd)', verbose_name='Tonen J/N'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itm_Name_Long',
            field=models.CharField(blank=True, default='', help_text="Naam/aanduiding, korter dan titel, voor in menu's en lijsten", max_length=250, verbose_name='Korte naam'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(help_text='Titel waarmee u het product in de catelogus wilt weergeven', max_length=100, verbose_name='Titel'),
        ),
    ]
