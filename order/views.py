from django.views.generic import CreateView, ListView, TemplateView
from .forms import OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderModel, OrderProducts
from products.models import ProductsModels
from django.shortcuts import redirect, render
import requests
class CheackOutView(TemplateView):
    template_name = "checkout.html"



def orders_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = OrderModel.objects.create(user=request.user, status=False)
            cart = request.session.get("cart", None)
            if cart is None:
                return redirect("orders:cheackout")
            
            products = ProductsModels.objects.filter(pk__in=cart)
            for p in products:
                OrderProducts.objects.create(
                    order= new_order,
                    product=p, 
                    product_name= p.name,
                    count=1, 
                    price=23.00,
                    image=p.image)
            request.session['cart'] = []
            send_telegram_message(request.user, new_order, products)
            return redirect("products:products",)
        else:
            return render(request, 'orders:cheackout')


def send_telegram_message(user, order, products):
        try:
            message = f"New order created by {user.username}.\nOrder ID: {order.id}\nProducts:\n"
            for product in products:
                message += f"- {product.name}\n"

            bot_token = "7225811705:AAH8vhezqKy47PpMbcxP7e8GtlZTJiRAh7c"
            chat_id = "2143611445"
            send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    
            response = requests.get(send_text)
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle requests exceptions
            raise Exception(f"Failed to send message to Telegram bot: {e}")
        except Exception as e:
            # Handle any other exceptions
            raise Exception(f"An error occurred: {e}")