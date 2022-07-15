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
            if get_data.get('function') == 'submit()':
                return self.submit()
            else:
                return self.get()
        if request.method == 'POST':
            post_data = request.POST
            if post_data.get('function'):
                if post_data.get('function') == 'submit()':
                    return self.submit()
                elif post_data.get('function') == 'approval()':
                    return self.approval()
                else:
                    return self.get()
            else:
                return self.get()

    def get(self, *args, **kwargs):
        error = {}
        context = {}
        db_obj = DataLayer()
        db_conn = db_obj.connect()

        if db_conn is None:
            error.update(
                { 'errorMsg': 'There is a problem with Database connection, Call IT' } 
            ) 
            return render(self.request, self.template_name, error) 

        sp_params = DataLayer().createparams(f"{''}")
        stock_get_info_result = DataLayer().runfunction(db_conn,'main_stock_get_info_fn', sp_params)
        #stock detailed info
        '''
        stock_list = list()
        for i in range (len(stock_get_info_result[0])):
            stock_list.append([])
        '''
        '''
        # dynamic list size, easier for maintenance process, not ideal for operating time used
        for i in range(len(stock_get_info_result)):
            for j in range(len(stock_get_info_result[i])):
                stock_list[j].append(stock_get_info_result[i][j])
        '''
        '''
        # static index values, shorter running time, harder for maintenance when database function's return table changes, 
        # hence taking more time for maitenance as backend and database adjustments are both required
        for i in range (len(stock_get_info_result)):
            stock_list[0].append(stock_get_info_result[i][0])
            stock_list[1].append(stock_get_info_result[i][1])
            stock_list[2].append(stock_get_info_result[i][2])
            stock_list[3].append(stock_get_info_result[i][3])
        '''

        stock_dict = {'company':[], 'id':[], 'symbol':[], 'business_type':[]}
        for i in range (len(stock_get_info_result)):
            stock_dict['company'].append(stock_get_info_result[i][0])
            stock_dict['id'].append(stock_get_info_result[i][1])
            stock_dict['symbol'].append(stock_get_info_result[i][2])
            stock_dict['business_type'].append(stock_get_info_result[i][3])

        context.update({
            'stock_info' : stock_get_info_result,
            'company' : stock_dict['company'],
            'id' : stock_dict['id'],
            'symbol' : stock_dict['symbol'],
            'business' : stock_dict['business_type']
        })
        return render(self.request, self.template_name, context)

    def submit(self, *args, **kwargs):
        data = self.request.POST
        error = {}
        context = {}
        db_obj = DataLayer()
        db_conn = db_obj.connect()

        if db_conn is None:
            error.update(
                { 'errorMsg': 'There is a problem with Database connection, Call IT' } 
            ) 
            return render(self.request, self.template_name, error)

        symbol = data.get('stock_symbol').strip().upper()
        sdate  = data.get('start_date').strip().upper()  
        edate  = data.get('end_date').strip().upper()

        print (symbol, sdate, edate)

        sp_params = DataLayer().createparams(f"{symbol},{sdate},{edate}")
        stock_get_prices_result = DataLayer().runfunction(db_conn,'main_stock_get_price_fn', sp_params)
        print (stock_get_prices_result)

        context.update({
            'stock_prices' : stock_get_prices_result
        })

        return render(self.request, self.template_name, context)

