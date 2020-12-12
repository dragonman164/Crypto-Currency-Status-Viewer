from django.shortcuts import render,HttpResponse
import requests,datetime
from django.utils.timezone import utc

# Create your views here.


def index(request):
    data = requests.get('https://api.coingecko.com/api/v3/exchanges').json()
    countries = set()
    total_normalised_trade_volume = 0
    for elem in data:
        countries.add(elem['country'])
        total_normalised_trade_volume += elem['trade_volume_24h_btc_normalized']

    params = {
        'no_of_cryptocurrencies': len(data),
        'no_of_countries' : len(countries),
        'total_normalised_trade_volume': total_normalised_trade_volume,
        
    }
    # for elem in data:
    #     print(elem['trust_score_rank'])

    return render(request,'crypto/index.html',params)

def crypto_table(request):
    data = requests.get('https://api.coingecko.com/api/v3/exchanges').json()
    params = {
        'Data':data,
        'time': datetime.datetime.utcnow().replace(tzinfo=utc)
    }
    return render(request,"crypto/crypto_tables.html",params)

def currency_details(request):
    name = request.GET.get('name')
    data = requests.get('https://api.coingecko.com/api/v3/exchanges').json()
    required_data = None
    for elem in data:
        if elem['name'] == name:
            required_data = elem
    params = {
        'Current_Crypto': required_data
    }
    
    return render(request,"crypto/currency_details.html",params)

def exchange_rates(request):
    data = requests.get('https://api.coingecko.com/api/v3/exchange_rates').json()
    details = []
    for elem in data['rates'].values():
        details.append(elem)
    params = {
        'Details' : details
    }
    return render(request,"crypto/exchange_rates.html",params)

def license(request):
    return render(request,"crypto/liscense.html")