from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    # template_name = 'reprint_label/reprint_label_value.html'
    # context = {}
    # context.update({                
    #     'object_type': "Hello World! This is a finance application about quantitative trading and stock!"
    # })
    # return render(request, template_name, context)
    return HttpResponse ("Hello World! This is a finance application about quantitative trading and stock!")