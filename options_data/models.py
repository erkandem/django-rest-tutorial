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
CME_SYMBOL_CHOICES = [('AD', 'AD'), ('BO', 'BO'), ('BP', 'BP'), ('BZ', 'BZ'), ('C', 'C'), ('CD', 'CD'), ('CL', 'CL'), ('EC', 'EC'), ('ES', 'ES'), ('FV', 'FV'), ('GC', 'GC'), ('HG', 'HG'), ('HO', 'HO'), ('JY', 'JY'), ('KW', 'KW'), ('LC', 'LC'), ('LN', 'LN'), ('NG', 'NG'), ('NQ', 'NQ'), ('RB', 'RB'), ('S', 'S'), ('SI', 'SI'), ('SM', 'SM'), ('TU', 'TU'), ('TY', 'TY'), ('US', 'US'), ('W', 'W')]
CME_EXCHANGE = [('CME', 'CME')]


class OptionRawDataModel(models.Model):
    """
    command to get the table schema `\d+ schema.table_name`
    """
    id = models.CharField(db_column='pk', max_length=65, primary_key=True)
    security_type = models.CharField(max_length=3)
    exchange = models.CharField(max_length=6)
    symbol = models.CharField(max_length=6)
    option_symbol = models.CharField(max_length=6)
    option_maturity = models.CharField(max_length=6,  blank=False)
    underlying_maturity = models.CharField(max_length=6)
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

