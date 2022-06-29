from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    template_name = 'stock.html'

    def get(self, *args, **kwargs):
        context = {}
        context.update({                
            'object_type': "Hello World! This is a finance application about quantitative trading and stock! Test Version Control"
        })
        return render(self.request, self.template_name, context)
        # return HttpResponse (context['object_type'])