from django.shortcuts import render

def cart_summary(request):
    return render(request, 'cart_summary.html', {})

def cart_add(request_):
    pass

def cart_delete(request_):
    pass

def cart_update(request_):
    pass
