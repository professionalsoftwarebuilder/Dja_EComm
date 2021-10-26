from django_extensions.db.fields import AutoSlugField
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum

from django.shortcuts import reverse
from django_countries.fields import CountryField
# from django.db.models.constraints import UniqueConstraint

from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from .fields import ImageThumbsField


LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

VOORRAADSTATUS = (
    ('V', 'op voorraad'),
    ('I', 'in bestelling'),
    ('T', 'tijdelijk niet leverbaar')
    )

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

SIZES = (
    {'code':'thumb','wxh':'69x100','resize':'crop'},
    {'code':'galry','wxh':'400x580','resize':'crop'},
    {'code':'detail','wxh':'552x800'},
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Category(MPTTModel):
    ctg_Title = models.CharField(max_length=85, unique=True)
    ctg_Name_Long = models.TextField(blank=True, null=True)
    ctg_Slug = AutoSlugField(populate_from=('ctg_Title',))
    parent = TreeForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)
    lft = models.PositiveIntegerField(default=0)
    rght = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    tree_id = models.PositiveIntegerField(default=0)

    class MPTTMeta:
        order_insertion_by = ['ctg_Title']

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categorien'

    def __str__(self):
        return self.ctg_Title


class Brand(models.Model):
    brd_Name = models.CharField(max_length=85)
    brd_Name_Long = models.CharField(max_length=250, blank=True, null=True)
    brd_Ctrl = models.CharField(max_length=30, blank=True, null=True)
    brd_Is_Show = models.BooleanField(default=True)
    brd_ImagePath = models.ImageField(max_length=250, blank=True, null=True)
    brd_Descr = models.TextField(blank=True, null=True)
    brd_IndexNr = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Merk'
        verbose_name_plural = 'Merken'

    def __str__(self):
        return self.brd_Name


class Item(models.Model):
    title = models.CharField('Titel', max_length=100, help_text='Titel waarmee u het product in de catelogus wilt weergeven')
    price = models.FloatField(verbose_name='Prijs')
    discount_price = models.FloatField(blank=True, null=True, verbose_name='Discount Prijs')
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, blank=True)
    slug = AutoSlugField(populate_from=('title'))
    itm_Categories = models.ManyToManyField(Category, verbose_name='Categorie')
    description = models.TextField(blank=True, default='', verbose_name='Omschrijving', help_text='Product omschrijving')
    image = ImageThumbsField(verbose_name='Hoofd afbeelding', max_length=250, blank=True, null=True, sizes=SIZES, help_text='Afbeelding die in catalogus gebruikt wordt')
    itm_KeyWords = models.TextField(blank=True, default='', verbose_name='Sleutelwoorden', help_text='Woorden waarmee zoekopdrachten worden vergemakkelijkt')
    itm_Name_Long = models.CharField('Korte naam', max_length=250, default='', blank=True, help_text='Naam/aanduiding, korter dan titel, voor in menu\'s en lijsten')
    itm_Pitch = models.TextField(
        blank=True, default='', verbose_name='Pitch', help_text='Verkoop pitch bij dit artikel')
    itm_Materiaal = models.CharField('Materiaal', max_length=120, default='', blank=True, help_text='Materiaal waaruit het product is vervaardigd')
    itm_Afmetingen = models.CharField('Afmetingen lxhxb', max_length=85, default='', blank=True, help_text='Afmetingen van het product (lxhxb)')
    itm_VoorraadStatus = models.CharField('Voorraad status', choices=VOORRAADSTATUS, max_length=1, default='V' )
    itm_LeverTijd = models.CharField('Levertijd (dagen)', max_length=45, default='', blank=True)
    itm_IndexNr = models.IntegerField('Volgorde', blank=True, default=0, help_text='Volgorde van weergave')
    itm_Ctrl = models.CharField('Controlfield', max_length=30, blank=True, default='', help_text='Systeemveld, Dit veld niet wijzigen')
    itm_Is_Show = models.BooleanField('Tonen J/N', blank=True, default=True, help_text='Door uit te zetten wordt dit product niet meer getoond (gedeactiveerd)')
    itm_Is_Frontpage = models.BooleanField('Voorpagina J/N (Featured)' , blank=True, default=True)
    itm_Is_Sale = models.BooleanField('Sale J/N', blank=True, default=True)
    itm_Is_Newasset = models.BooleanField('Nieuw binnen J/N', blank=True, default=True)
    itm_Brand_id = models.ForeignKey(
        Brand, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Merk')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Producten'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class FotoSet(models.Model):
    fst_Title = models.CharField(
        default='', max_length=100, verbose_name='Titel', blank=True, help_text='Bijvoorbeeld: Vooraanzicht, zijkant, enz.')
    fst_Name_Plural = models.CharField(
        default='', max_length=100, blank=True, verbose_name='Meervoudsnaam', help_text='Om event te gebruiken in text genarator')
    itm_Fk_Item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Bij artikel', help_text='Artikel waarbij deze foto hoort')
    fst_Slug = AutoSlugField(populate_from=(
        'fst_Title'), editable=False, verbose_name='Slug code', help_text='Speciale itemcode, dit veld niet aanpassen')
    fst_Description = models.TextField(
        blank=True, default='', verbose_name='Omschrijving')
    fst_Is_Feature = models.BooleanField(default=False, blank=True, verbose_name='Is hoofdfoto', help_text='Gebruik deze foto in de catalogus')
    fst_Is_Show = models.BooleanField(blank=True, default=True, verbose_name='Tonen', help_text='Foto al dan niet tonen in de fotoset')
    fst_Image = models.ImageField(
        max_length=250, blank=True, null=True, verbose_name='Afbeelding')
    fst_Name_Long = models.CharField(
        max_length=250, blank=True, default='', verbose_name='Naam uitgebreid')
    fst_IndexNr = models.IntegerField(
        blank=True, default=0, verbose_name='Volgnummer')
    fst_Ctrl = models.CharField(max_length=30, default='', blank=True, verbose_name='Beheercodes',
                                help_text='Dit veld alleen door de administrator te gebruiken')

    class Meta:
        verbose_name_plural = 'FotoSets'

    def __str__(self):
        return self.fst_Title


class Type(models.Model):
    ty_Nm = models.CharField(max_length=85, blank=True, null=True)
    ty_Descr = models.CharField(max_length=85, blank=True, null=True)
    ty_Ctrl = models.CharField(max_length=30, blank=True, null=True)
    ty_Is_active = models.BooleanField(default=True)


class Type_Item(models.Model):
    ti_Nm = models.CharField(max_length=85, blank=True, null=True)
    ti_TextVal = models.CharField(max_length=85, default='text value')
    ti_Ctrl = models.CharField(max_length=30, blank=True, null=True)
    ti_Is_active = models.BooleanField(default=True)
    ti_Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    ti_Descr = models.CharField(max_length=85, blank=True, null=True)


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name='Adres'
        verbose_name_plural='adressen'

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
