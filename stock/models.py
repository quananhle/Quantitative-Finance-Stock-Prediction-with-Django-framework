from django.db import models

# Create your models here.

class StockMarket(models.Model):
    HOLD_TYPE = (
        (0, 'Not hold'),
        (1, 'Hold'),
    )
    CANCELLED_TYPE = (
        (0, 'Not cancelled'),
        (1, 'Cancelled'),
    )
    COMPLETED_TYPE = (
        (0, 'Not completed'),
        (1, 'Completed'),
    )
    salesorder_id = models.CharField(max_length=50, primary_key=True)
    plant_code = models.CharField('Plant Code', max_length=100)
    customer_shipto = models.CharField(max_length=100)
    customer_soldto = models.CharField(max_length=100)
    salesorder_type = models.CharField(max_length=255)
    customer_po = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_name_alt = models.CharField(max_length=255)
    ship_priority = models.CharField(max_length=100)
    sap_create_date = models.DateTimeField('SAP Create Date', null=True, blank=True)
    sap_change_date = models.DateTimeField('SAP Change Date', null=True, blank=True)
    customer_reference = models.CharField(max_length=255)
    completed_date = models.DateTimeField('Completed Date', null=True, blank=True)
    completed = models.IntegerField(choices=COMPLETED_TYPE, null=True, blank=True, help_text='completed')
    ship_hold = models.IntegerField(choices=HOLD_TYPE, null=True, blank=True, help_text='hold')
    ship_cancelled = models.IntegerField(choices=CANCELLED_TYPE, null=True, blank=True, help_text='cancel')
    purchase_order_date = models.DateTimeField(null=True, blank=True)
    ship_date = models.DateTimeField(null=True, blank=True)
    ship_method = models.CharField(max_length=255, null=True, blank=True)
    creator = models.CharField('Creator', max_length=100, null=True, blank=True)
    create_date = models.DateTimeField('Create Date', null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.CharField(max_length=50, null=True, blank=True) 
    ship_to_street = models.CharField(max_length=255, null=True, blank=True)
    ship_to_city = models.CharField(max_length=255, null=True, blank=True)
    ship_to_region = models.CharField(max_length=255, null=True, blank=True)
    ship_to_country = models.CharField(max_length=255, null=True, blank=True)
    ship_to_zipcode = models.CharField(max_length=255, null=True, blank=True)
    incoterm = models.CharField(max_length=10, null=True, blank=True)
    bill_to_name = models.CharField(max_length=255, null=True, blank=True)
    bill_to_address = models.CharField(max_length=255, null=True, blank=True)
    bill_to_city = models.CharField(max_length=255, null=True, blank=True)
    bill_to_region = models.CharField(max_length=255, null=True, blank=True)
    bill_to_country = models.CharField(max_length=255, null=True, blank=True)
    bill_to_zipcode = models.CharField(max_length=255, null=True, blank=True)
    carrier = models.CharField(max_length=255, null=True, blank=True)
    ship_to_name = models.CharField(max_length=255, null=True, blank=True)
    service_level = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.salesorder_id

class Company(models.Model):
    row_id = models.AutoField(auto_created=True, primary_key=True)
    company_id = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.company_name)

class Quote(models.Model):
    row_id = models.AutoField(auto_created=True, primary_key=True)
    quote = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    def __str__(self):
        return str(self.quote)

class FinancialStatement(models.Model):
    row_id = models.AutoField(auto_created=True, primary_key=True)
    company_id = models.ForeignKey('Company', db_column='company_id', on_delete=models.CASCADE, null=False, related_name="cid")
    company_name = models.ForeignKey('Company', db_column='company_name', on_delete=models.CASCADE, null=False, related_name="cname", default='')
    financial_statement = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.financial_statement)