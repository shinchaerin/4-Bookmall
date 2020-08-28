from django.db import models
from django.shortcuts import resolve_url


class Category(models.Model):
    # 속성 : 판타지 만화책, 스포츠 만화책, 아이돌 만화책, 로맨스 만화책, 사극 만화책
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)

class Meta:
    ordering = ['name']
    verbose_name = 'category'
    verbose_name_plural = 'categories'

# __str__()
def __str__(self):
    return self.name

#get_absolute_url()
def get_absolute_url(self):
    return resolve_url('mall:category_detail', self.slug)

class Product(models.Model):
    name = models.CharField(max_length=100) #상품 이름
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products') #상품 종류
    image = models.ImageField(upload_to='products/%Y/%m/%d', default='products/no_image.jpg') #상품 이미지
    price = models.DecimalField(max_digits=10, decimal_places=2) #가격  100원, $9.99
    stock = models.PositiveIntegerField() #재고수량
    description = models.TextField(blank=True) #상품 설명

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-created']


def __str__(self):
    return self.name

def get_absolute_url(self):
    return resolve_url('mall:product_detail', self.id, self.slug)




