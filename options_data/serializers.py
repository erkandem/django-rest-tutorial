from rest_framework import serializers
from .models import OptionRawDataModel


class OptionRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionRawDataModel
        fields = [
            'id', 'security_type', 'exchange', 'symbol', 'option_symbol',
            'option_maturity', 'underlying_maturity', 'last_trading_day', 'bizdt',
            'undprice', 'putcall', 'strkpx', 'bid', 'ask', 'settleprice', 'volume',
            'oi', 'yte', 'moneyness', 'divyield', 'rfr', 'rawiv', 'delta', 'tv'
        ]
