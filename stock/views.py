from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    template_name = 'stock.html'
    context = {}
    context.update({                
        'object_type': "Hello World! This is a finance application about quantitative trading and stock! Test Version Control"
    })
    return render(request, template_name, context)
    # return HttpResponse ("Hello World! This is a financial application about quantitative trading and stock!")