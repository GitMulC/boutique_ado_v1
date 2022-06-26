from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LErv5H5L4JuwG5ZPORGqhsv6obxec59vil5FE0AIjAx3PHOfxNlnNE9ebpqZtiilmZ1H2Ona9TbdpoDKORt6faO008jM71t5G',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
