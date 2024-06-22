from django.views.generic import ListView, DetailView, TemplateView
from products.models import ProductsModels, CommentsProductsModle, AuthorProducstModels
from django.shortcuts import render, redirect

class ProductsView(ListView):
    template_name = "products.html"
    context_object_name = "products"
    model = ProductsModels
    
    def get_context_data(self, **kwargs):
        context = {
            "products": ProductsModels.objects.all(),
            "author": AuthorProducstModels.objects.all()
        }
        return context
    


class PageProductsDetailView(DetailView):
    
    template_name = "single-product.html"
    context_object_name = 'product_detail'
    model = ProductsModels
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_detail_serch = self.get_object()
        context.update({
            "all_products":ProductsModels.objects.all(),
            "categories": product_detail_serch.category.name,
        })
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # self.get_object() ni chaqirib o'zgaruvchiga saqlash
        
        comment = request.POST.get('comment')
        
        if comment:
            CommentsProductsModle.objects.create(comment=comment, user=request.user, products=self.object)
        
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    
def add_cart_remove_cart(request, pk):
    products_cart = request.session.get('cart', [])
    if pk in products_cart:
        products_cart.remove(pk)
    else:
        products_cart.append(pk)
        
    print(products_cart)
    request.session['cart'] = products_cart
    return redirect('products:single-products', pk)


class ShopingCratView(TemplateView):
    template_name = "shopping-cart.html"
    
    
    