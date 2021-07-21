from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Table(models.Model):
    table_number = models.CharField(max_length=3, verbose_name=_('table number'), help_text=_('enter table number'),
                                    null=False, blank=False)
    cafe_space_position = models.CharField(max_length=25, verbose_name=_('position in cafe'), help_text=
                                           _('table position in cafe'), null=False, blank=False,
                                           choices=[('NE', _('north-east')), ('NW', _('north-west')),
                                                    ('ME', _('mid-east')), ('MW', _('mid-west')),
                                                    ('SE', _('south-east')), ('SW', _('south-west'))])
    table_status = models.CharField(max_length=25, verbose_name=_('table status'), help_text=
                                    _('specify status of table'), null=False, blank=False, default=_('free'),
                                    choices=[('FR', _('free')), ('FL', _('full')), ('RS', _('reserve'))])

    def __str__(self):
        return f"{self.table_number}# {self.cafe_space_position} : {self.table_status}"


class Category(models.Model):
    name_en = models.CharField(max_length=20, verbose_name=_('english category'), help_text=_('enter category'),
                               null=True, blank=True, default=_('category'))
    name_fa = models.CharField(max_length=20, verbose_name=_('farsi category'), help_text=_('enter category'),
                               null=True, blank=True, default='نوع دسته غذا و نوشیدنی')

    def __str__(self):
        return f"{self.id}# {self.name_en}"


class MenuItem(models.Model):
    name_en = models.CharField(max_length=30, verbose_name=_('menu item name in english'), default=_('menu'),
                               help_text=_('enter menu item name'), null=False, blank=False)
    name_fa = models.CharField(max_length=30, verbose_name=_('menu item name in farsi'), default='منو',
                               help_text=_('enter menu item name'), null=False, blank=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('menu item category'),
                                    help_text=_('define category'), null=False, blank=False)
    discount = models.IntegerField(verbose_name=_('discount'), help_text=_('enter item discount(%)'), null=True,
                                   blank=True, default=0)
    price = models.FloatField(verbose_name=_('price'), help_text=_('enter item price'), null=False, blank=False)
    image = models.FileField(verbose_name=_('item image'), help_text=_('upload image of item'), null=True, blank=True,
                             upload_to='cafe5/menu_items/images/')
    create_timestamp = models.DateTimeField(verbose_name=_('time of adding item'),
                                            help_text=_('time of creation of item'),
                                            auto_now_add=True, null=False, blank=False)
    modify_timestamp = models.DateTimeField(verbose_name=_('time of update item'), help_text=_('time of modify of item')
                                            , auto_now=True, null=False, blank=False)

    def __str__(self):
        return f"{self.id}# {self.category_id.name_en}: {self.name_en} : {self.price}"


class Order(models.Model):
    order_number = models.CharField(max_length=5, verbose_name=_('order number'), help_text=_('enter order number'),
                                    null=False, blank=False)
    status = models.CharField(max_length=30, verbose_name=_('status'), help_text=_('specify state of order'),
                              null=False, blank=False, default=_('new'),
                              choices=[('NW', _('new')), ('PR', _('preparing')), ('DV', _('delivered')),
                                       ('PO', _('pay off'))])
    time_stamp = models.DateTimeField(verbose_name=_('time of adding order'), help_text=_('specify time of adding order')
                                      , auto_now_add=True)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name=_('table'),
                                 help_text=_('specify table for order'))
    menu_item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name=_('menu item id'),
                                     help_text=_('specify menu item in order'))
    menu_item_number = models.IntegerField(verbose_name=_('number of item'),
                                           help_text=_('enter number of item that you want'), default=1)

    def __str__(self):
        return f"{self.order_number}# : {self.status}"


class Receipt(models.Model):
    order_id = models.ManyToManyField(Order, verbose_name=_('order'), help_text=_('specify order'))
    total_price = 'total_price_func()'
    final_price = 'final_price_func()'
    time_stamp = models.DateTimeField(verbose_name=_('time of export bill'), help_text=_('specify time of export bill'),
                                      auto_now_add=True)

    def total_price_func(self):
        item_price = self.order_id.menu_item.price
        item_number = self.order_id.menu_item_number
        total = item_price * item_number
        return total

    def final_price_func(self):
        item_price = self.order_id.menu_item_id.price
        item_number = self.order_id.menu_item_number
        item_discount = self.order_id.menu_item_id.discount
        final = item_price * item_number * (100 - item_discount)
        return final

    def __str__(self):
        return f"_(final price): {self.final_price}"





