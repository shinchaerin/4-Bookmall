from decimal import Decimal

from django.conf import settings

from mall.models import Product

# ----------------------------------------------------------------------

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)

        if not cart:
            cart = self.session[settings.CART_ID] = {}

        self.cart = cart

# ----------------------------------------------------------------------

    def __str__(self):
        pass

# ---------------------------------------------------------------------

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

# ---------------------------------------------------------------------

    def __iter__(self): # for 문에서 하나씩 요소를 꺼낼 때 return 값
        products_ids = self.cart.keys()

        products = Product.objects.filter(id__in=products_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

# ---------------------------------------------------------------------

    def add(self, product, quantity=1): # cart에 product 추가하자
        pass

# ----------------------------------------------------------------------

    def remove(self, product): # cart에서 product 삭제하자
        pass

# ----------------------------------------------------------------------

    def save(self): # cart를 session에 저장하자
        pass

# ----------------------------------------------------------------------

    def clear(self): # cart를 비우자
        pass
# ----------------------------------------------------------------------

    def get_product_total(self): # cart의 product 가격 합계를 내자
        pass

# ----------------------------------------------------------------------