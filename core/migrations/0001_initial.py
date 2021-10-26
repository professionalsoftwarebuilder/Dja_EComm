# Generated by Django 2.2 on 2020-04-09 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_extensions.db.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brd_Name', models.CharField(max_length=85)),
                ('brd_Name_Long', models.CharField(blank=True, max_length=250, null=True)),
                ('brd_Ctrl', models.CharField(blank=True, max_length=30, null=True)),
                ('brd_Is_Show', models.BooleanField(default=True)),
                ('brd_ImagePath', models.ImageField(blank=True, max_length=250, null=True, upload_to='')),
                ('brd_Descr', models.TextField(blank=True, null=True)),
                ('brd_IndexNr', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctg_Title', models.CharField(max_length=85, unique=True)),
                ('ctg_Name_Long', models.TextField(blank=True, null=True)),
                ('ctg_Slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=('ctg_Title',))),
                ('lft', models.PositiveIntegerField(default=0)),
                ('rght', models.PositiveIntegerField(default=0)),
                ('level', models.PositiveIntegerField(default=0)),
                ('tree_id', models.PositiveIntegerField(default=0)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.Category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(verbose_name='Prijs')),
                ('discount_price', models.FloatField(blank=True, null=True, verbose_name='Discount Prijs')),
                ('label', models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('description', models.TextField(blank=True, default='', verbose_name='Omschrijving')),
                ('image', models.ImageField(blank=True, max_length=250, null=True, upload_to='')),
                ('itm_KeyWords', models.TextField(blank=True, default='', help_text='Woorden waarmee zoekopdrachten worden vergemakkelijkt', verbose_name='Sleutelwoorden')),
                ('itm_Name_Long', models.CharField(blank=True, default='', max_length=250)),
                ('itm_Pitch', models.TextField(blank=True, default='', help_text='Verkoop pitch bij dit artikel', verbose_name='Pitch')),
                ('itm_IndexNr', models.IntegerField(blank=True, default=0)),
                ('itm_Ctrl', models.CharField(blank=True, default='', max_length=30)),
                ('itm_Is_Show', models.BooleanField(blank=True, default=True)),
                ('itm_Is_Frontpage', models.BooleanField(blank=True, default=True)),
                ('itm_Is_Sale', models.BooleanField(blank=True, default=True)),
                ('itm_Is_Newasset', models.BooleanField(blank=True, default=True)),
                ('itm_Brand_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Brand')),
                ('itm_Categories', models.ManyToManyField(to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('being_delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_granted', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='core.Address')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Coupon')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ty_Nm', models.CharField(blank=True, max_length=85, null=True)),
                ('ty_Descr', models.CharField(blank=True, max_length=85, null=True)),
                ('ty_Ctrl', models.CharField(blank=True, max_length=30, null=True)),
                ('ty_Is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('one_click_purchasing', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ti_Nm', models.CharField(blank=True, max_length=85, null=True)),
                ('ti_TextVal', models.CharField(default='text value', max_length=85)),
                ('ti_Ctrl', models.CharField(blank=True, max_length=30, null=True)),
                ('ti_Is_active', models.BooleanField(default=True)),
                ('ti_Descr', models.CharField(blank=True, max_length=85, null=True)),
                ('ti_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Type')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='core.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='core.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FotoSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fst_Title', models.CharField(default='', max_length=100, verbose_name='Titel')),
                ('fst_Name_Plural', models.CharField(blank=True, default='', help_text='Om event te gebruiken in text genarator', max_length=100, verbose_name='Meervoudsnaam')),
                ('fst_Slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='Speciale itemcode, dit veld niet aanpassen', populate_from='fst_Title', verbose_name='Slug code')),
                ('fst_Description', models.TextField(blank=True, default='', verbose_name='Omschrijving')),
                ('fst_Is_Feature', models.BooleanField(blank=True, default=False, help_text='Gebruik deze foto in de catalogus', verbose_name='Is hoofdfoto')),
                ('fst_Is_Show', models.BooleanField(blank=True, default=True, help_text='Foto al dan niet tonen in de fotoset', verbose_name='Tonen')),
                ('fst_Image', models.ImageField(blank=True, max_length=250, null=True, upload_to='', verbose_name='Afbeelding')),
                ('fst_Name_Long', models.CharField(blank=True, default='', max_length=250, verbose_name='Naam uitgebreid')),
                ('fst_IndexNr', models.IntegerField(blank=True, default=0, verbose_name='Volgnummer')),
                ('fst_Ctrl', models.CharField(blank=True, default='', help_text='Dit veld alleen door de administrator te gebruiken', max_length=30, verbose_name='Beheercodes')),
                ('itm_Fk_Item_id', models.ForeignKey(blank=True, help_text='Artikel waarbij deze foto hoort', null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='item_fotos', to='core.Item', verbose_name='Bij artikel')),
            ],
            options={
                'verbose_name_plural': 'FotoSets',
            },
        ),
    ]
