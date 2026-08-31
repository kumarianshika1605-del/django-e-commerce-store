from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, Order, OrderItem


def home(request):
    products = Product.objects.all().order_by('-created_at')

    return render(
        request,
        'store/home.html',
        {'products': products}
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        'store/product_detail.html',
        {'product': product}
    )


def add_to_cart(request, product_id):
    if request.method != 'POST':
        return redirect('home')

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id_string = str(product.id)

    current_quantity = cart.get(product_id_string, 0)

    if current_quantity < product.stock:
        cart[product_id_string] = current_quantity + 1
        request.session['cart'] = cart
        messages.success(request, f'{product.name} added to cart.')
    else:
        messages.error(request, 'Not enough stock available.')

    return redirect('cart')


def cart(request):
    cart_data = request.session.get('cart', {})

    items = []
    total = Decimal('0.00')

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(Product, id=product_id)

        subtotal = product.price * quantity

        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

        total += subtotal

    return render(
        request,
        'store/cart.html',
        {
            'items': items,
            'total': total,
        }
    )


def update_cart(request, product_id):
    if request.method != 'POST':
        return redirect('cart')

    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get('quantity', 1))

    if quantity < 1:
        quantity = 1

    if quantity > product.stock:
        quantity = product.stock

    cart = request.session.get('cart', {})

    cart[str(product.id)] = quantity

    request.session['cart'] = cart

    return redirect('cart')


def remove_from_cart(request, product_id):
    if request.method != 'POST':
        return redirect('cart')

    cart = request.session.get('cart', {})

    product_id_string = str(product_id)

    if product_id_string in cart:
        del cart[product_id_string]

    request.session['cart'] = cart

    return redirect('cart')


@login_required
def checkout(request):

    cart_data = request.session.get('cart', {})

    if not cart_data:
        messages.error(request, 'Your cart is empty.')
        return redirect('home')

    items = []
    total = Decimal('0.00')

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(Product, id=product_id)

        if quantity > product.stock:
            messages.error(
                request,
                f'Only {product.stock} units of {product.name} are available.'
            )
            return redirect('cart')

        subtotal = product.price * quantity

        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

        total += subtotal

    if request.method == 'POST':

        shipping_address = request.POST.get('shipping_address', '').strip()

        if not shipping_address:
            messages.error(request, 'Please enter your shipping address.')
            return render(
                request,
                'store/checkout.html',
                {
                    'items': items,
                    'total': total,
                }
            )

        with transaction.atomic():

            order = Order.objects.create(
                user=request.user,
                total_amount=total,
                shipping_address=shipping_address,
                status='Pending'
            )

            for item in items:

                product = item['product']

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price
                )

                product.stock -= item['quantity']
                product.save()

        request.session['cart'] = {}

        return redirect(
            'order_success',
            order_id=order.id
        )

    return render(
        request,
        'store/checkout.html',
        {
            'items': items,
            'total': total,
        }
    )


@login_required
def order_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        'store/order_success.html',
        {'order': order}
    )


def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )