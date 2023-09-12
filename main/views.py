from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Nadhira Widyaniswari',
        'class': 'PBP E',
        'product_name': 'skintipic',
        'date_added' : '09/09/2023',
        'amount': 50000,
        'description' : 'pelembab wajah',

    }
    return render(request, "main.html", context)

