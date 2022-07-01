from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic

from django.http import HttpResponse
from srv.database.db_actions import *


# Create your views here.
class StockPriceCalculator (LoginRequiredMixin, View):
    template_name = 'stock.html'

    def get(self, *args, **kwargs):
        context = {}
        db_obj = DataLayer()
        db_conn = db_obj.connect()

        if db_conn is None:
            context.update(
                { 'errorMsg': 'There is a problem with Database connection, Call IT' } 
            ) 
            return render(self.request, self.template_name, context)

        context.update({                
            'object_type': "Hello World! This is a finance application about quantitative trading and stock! Test Version Control"
        })
        return render(self.request, self.template_name, context)
        # return HttpResponse (context['object_type'])

    return render(request, template_name)