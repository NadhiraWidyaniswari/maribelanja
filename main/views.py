from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        'name': 'Nadhira Widyaniswari',
        'class': 'PBP E',
        'product_name': 'skintipic',
        'date_added' : '09/09/2023',
        'amount': 50000,
        'description' : 'pelembab wajah',
        'rating' : "4.9/5.0"

    }
    return render(request, "main.html", context)

skintipic = Product(name="skintipic", date_added =10/12/2023, price=5000, description ="Produk kecantikan", rating="4.0/5.0")
