from django.shortcuts import render
from django.views.generic import  ListView, TemplateView
from products.models import ProductsModels, CommentsProductsModle
from django.shortcuts import redirect
# Create your views here.
class HomePageView(ListView):
    template_name = 'index.html'
    model = ProductsModels
    def get_context_data(self, **kwargs):
        tv_audio = ProductsModels.objects.filter(category__name='TV & Audio')
        laptop = ProductsModels.objects.filter(category__name='Laptop')
        new_arrival = ProductsModels.objects.filter(category__name='New Arrival')
        bestseller = ProductsModels.objects.filter(category__name='Bestsellers')
        featured_products = ProductsModels.objects.filter(category__name='Featured Products')
        trendding_products = ProductsModels.objects.filter(category__name='Trendding Products')
        
        
        context = {
            'tv_audio': tv_audio,
            'laptop': laptop,
            'new_arrival': new_arrival,
            'bestseller': bestseller,
            'featured_products': featured_products,
            'trendding_products': trendding_products
        }
        return context
 
    
def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = ProductsModels.objects.filter(name__icontains=query)

    return render(request, 'index.html', {'results': results, 'query': query})



            
class About(TemplateView):
    template_name = 'about-us.html'