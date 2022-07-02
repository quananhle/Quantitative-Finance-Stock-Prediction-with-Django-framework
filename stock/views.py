from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic

from django.http import HttpResponse
from srv.database.db_actions import *


# Create your views here.
class StockPriceCalculator (View):
    template_name = 'stock.html'

    def dispatch(self, request) -> HttpResponse:
        if request.method == 'GET':
            get_data = request.GET
            if get_data.get('function') == 'populate()':
                return self.populate()
            else:
                return self.get()
        if request.method == 'POST':
            post_data = request.POST
            if post_data.get('function'):
                if post_data.get('function') == 'confirm()':
                    return self.confirm()
                elif post_data.get('function') == 'approval()':
                    return self.approval()
                else:
                    return self.get()
            else:
                return self.get()

    def get(self, *args, **kwargs):
        context = {}
        db_obj = DataLayer()
        db_conn = db_obj.connect()

        if db_conn is None:
            context.update(
                { 'errorMsg': 'There is a problem with Database connection, Call IT' } 
            ) 
            return render(self.request, self.template_name, context) 

        sp_params = DataLayer().createparams(f"{('APPL','GOOG','TSLA','AMD','NVDA')}")
        model_manager_info = DataLayer().runfunction(db_conn,'mfg_model_manager_update_fn', sp_params)

        context.update({                
            'object_type': "Hello World! This is a finance application about quantitative trading and stock! Test Version Control"
        })
        return render(self.request, self.template_name, context)
