"""
snippet to checkout sample rows
```SQL
(
SELECT * FROM options_rawdata WHERE exchange = 'CME' LIMIT 1
) UNION ALL (
SELECT * FROM options_rawdata WHERE exchange = 'ICE' LIMIT 1
) UNION ALL (
SELECT * FROM options_rawdata WHERE exchange = 'EUREX' LIMIT 1
) UNION ALL (
SELECT * FROM options_rawdata WHERE exchange = 'USETF' LIMIT 1
)
```
"""
from django.db import models


class OptionRawDataModel(models.Model):
    """
    command to get the table schema `\d+ schema.table_name`
    """
    id = models.CharField(db_column='pk', max_length=65, blank=False, primary_key=True)
    security_type = models.CharField(max_length=3, blank=False)
    exchange = models.CharField(max_length=6, blank=False)
    symbol = models.CharField(max_length=6, blank=False)
    option_symbol = models.CharField(max_length=6, blank=False)
    option_maturity = models.CharField(max_length=6,  blank=False)
    underlying_maturity = models.CharField(max_length=6, blank=False)
    last_trading_day = models.DateField(blank=False)
    bizdt = models.DateField(blank=False)
    undprice = models.FloatField(blank=True, null=True)
    putcall = models.IntegerField(blank=True, null=True)
    strkpx = models.FloatField(blank=True, null=True)
    bid = models.FloatField(blank=True, null=True)
    ask = models.FloatField(blank=True, null=True)
    settleprice = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    oi = models.IntegerField(blank=True, null=True)
    yte = models.FloatField(blank=True, null=True)
    moneyness = models.FloatField(blank=True, null=True)
    divyield = models.FloatField(blank=True, null=True)
    rfr = models.FloatField(blank=True, null=True)
    rawiv = models.FloatField(blank=True, null=True)
    delta = models.FloatField(blank=True, null=True)
    tv = models.FloatField(blank=True, null=True)

    class Meta:
        """
        https://docs.djangoproject.com/en/1.11/ref/models/options/#db-table
        """
        db_table = 'options_rawdata'
        ordering = ['id']  # order by sth so pagination doesn't get confused


class CmeDataSetsModel(OptionRawDataModel):
    CME_SYMBOL_CHOICES = [('AD', 'AD'), ('BO', 'BO'), ('BP', 'BP'), ('BZ', 'BZ'), ('C', 'C'), ('CD', 'CD'), ('CL', 'CL'), ('EC', 'EC'), ('ES', 'ES'), ('FV', 'FV'), ('GC', 'GC'), ('HG', 'HG'), ('HO', 'HO'), ('JY', 'JY'), ('KW', 'KW'), ('LC', 'LC'), ('LN', 'LN'), ('NG', 'NG'), ('NQ', 'NQ'), ('RB', 'RB'), ('S', 'S'), ('SI', 'SI'), ('SM', 'SM'), ('TU', 'TU'), ('TY', 'TY'), ('US', 'US'), ('W', 'W')]
    CME_EXCHANGE = [('CME', 'CME')]

    class Meta:
        proxy = True

    def apply_choices(self):
        pass

    '''
class CmeDataSetsModel(OptionRawDataModel):
    CME_SYMBOL_CHOICES = [('AD', 'AD'), ('BO', 'BO'), ('BP', 'BP'), ('BZ', 'BZ'), ('C', 'C'), ('CD', 'CD'), ('CL', 'CL'), ('EC', 'EC'), ('ES', 'ES'), ('FV', 'FV'), ('GC', 'GC'), ('HG', 'HG'), ('HO', 'HO'), ('JY', 'JY'), ('KW', 'KW'), ('LC', 'LC'), ('LN', 'LN'), ('NG', 'NG'), ('NQ', 'NQ'), ('RB', 'RB'), ('S', 'S'), ('SI', 'SI'), ('SM', 'SM'), ('TU', 'TU'), ('TY', 'TY'), ('US', 'US'), ('W', 'W')]
    exchange = models.CharField(max_length=6, blank=False, choices=[('CME', 'CME')])
    symbol = models.CharField(max_length=6, blank=False, choices=CME_SYMBOL_CHOICES)

above doesn't work because you can't override a parent fields in djanago.

Instead, we use a method to restrict the possible symbols and exchange to the choices we want
Also, We will use an proxy class. 
https://docs.djangoproject.com/en/1.11/topics/db/models/#proxy-models


'''