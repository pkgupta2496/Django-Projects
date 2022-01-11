from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
  #  print(product.id)
  #  print(keys)
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='quantity_counter')
def quantity_counter(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='total_price')
def total_price(item, cart):
    print(item)
    return int(item.product_price)*quantity_counter(item, cart)



@register.filter(name='total_cart_price')
def total_cart_price(item,cart):
    sum=0
    for p in item:
        sum=sum+total_price(p,cart)
    return sum
