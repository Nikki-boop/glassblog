import requests
from django.shortcuts import render
from django.http import JsonResponse
from glassblog.models import BlogPost

def fetch_ebay_listings(keywords="pyrex"):
    print("Query", keywords)
    pageSize = 10
    url = f"https://api.ebay.com/buy/browse/v1/item_summary/search?q={keywords}&limit={pageSize}"
    token = "v^1.1#i^1#p^1#f^0#r^0#I^3#t^H4sIAAAAAAAA/+VYbWwURRjutVdqgRYSDWAx8VitPyB3N7u3t91be0evLdAL/b7rB02QzO3OXpfb21125iwHkZxNRCUg0sQoamOFKDGEP/DDmPgJRI3QSNAfKEFEA4GExI9gBImJe9tSrpXw1Uts4v25zDvvvPM8z7zvzOyA7KzypVubtv5Z4SgrHsmCbLHDQc8B5bNKl1WWFFeVFoE8B8dI9vGsc7DkYi2GKdUQOhE2dA0j18aUqmHBNgaptKkJOsQKFjSYQlggohANtzQLjAcIhqkTXdRVyhVpDFJcnJX9XAByIsPGuRq/ZdVuxIzpQUqGvI8L+FjE8oCtAVY3xmkU0TCBGglSDGD8buBzAz5G1wg0I9DAw7B0H+XqRiZWdM1y8QAqZKMV7LFmHtTbI4UYI5NYQahQJLwy2haONK5ojdV682KFxmWIEkjSeHKrQZeQqxuqaXT7abDtLUTToogwpryhsRkmBxXCN8DcB3xbaQaKAYaVRQny/gAPYEGkXKmbKUhujyNnUSS3bLsKSCMKydxJUUuN+HokkvFWqxUi0ujK/XWkoarICjKD1Ir68JpwezsValWsfEL1uhtDTYrr7vbORjctIZGGIlvj5vkAzfmAb3yasVjjIk+Zp0HXJCUnGXa16qQeWZjRVGVAnjKWU5vWZoZlksOT7xe4oaAP9OWWdGwN06Rfy60qSlkyuOzmnfWfGE2IqcTTBE1EmNphCxSkoGEoEjW1087E8eTZiINUPyGG4PUODAx4Bnwe3Ux4GQBob29Lc1TsRykrP2zfXK1b/sqdB7gVm4qIrJFYEUjGsLBstDLVAqAlqJCf9vv8YFz3ybBCU63/MuRx9k6uh0LVh8TxbFzkeIgYztpxpELUR2g8Rb05HCgOM+4UNJOIGCoUkVu08iydQqYiCT6/zPh4GbklLiC72YAsu+N+iXPTMkIAoXhcDPD/nzK520SPItFEpFCZXpgs71BT4qpNyxpbV3CBjt7UerltmRgjq2g1Eebre6OYU5k1pDPZy7Qmg3dbC7ck36AqljIxa/6CCZCr9YKI0KRjgqRp0YuKuoHadVURMzNrgX2m1A5NkokiVbUM0yIZNoxIwXbqwtC7p03i/lgX9Hz6L86mW7LCuYSdWaxy47EVABqKJ3f6eEQ95dWhde3wwlytG8o6G/W0eCvWnXVGsbZIjrFVpLHLpsem7MFPix4TYT1tWvdsT1vu9hXTk0izTjNi6qqKzG562tWcSqUJjKtoppV1ARJcgTPsqKVrWJr1+wK+6fES7YN03Uzbkgq4ETtD93ah9k7+tg8V2T960HEYDDo+LnY4QC2oph8DS2aVdDlL5lZhhSCPAmUPVhKa9c1qIk8SZQyomMUPFn1d2Sw929T8Rzaefr/nynK+qCLvaWFkLVg08bhQXkLPyXtpAI/c7Cml5y2sYPzAB3i6hmZo0Aceu9nrpBc4Hyr/q3Tp611r6coNP2r8R+8Zpy9EzoGKCSeHo7TIOego+vCL6wsXs5Wnz4927ZjfM3TooLhYr/1uf/oqqt1XdHXH6PPHf17+a92hTWziqZX1ZdzomTMfJPr2lD1T3nLt5Se3XHPO/nvPvOyLnf7jvx/YvW50eN7mbb3Jo6992Xal7IGubxZg7tv+ly6XDaXmPpwe3lXd+e6JyydP8a80rV5wQb7kP/HT51UXTtYFh3Z8duRAT08zM3p8m3/fwSirvnPt8qObq+nDiV2/bc+2OI/szPwwe8mpY5HnYht27v307Ehd8d6W1b0v7H4juYn+ZfDiV69eT57t6y6url/bN3R00dtPDDYcq6i7KJybfz480FF3avvmSxv6PomLlVXDDaXK8P4t5V79rTcd3bO/3zO2lv8AYqWj//QRAAA="
    headers = {
        "X-EBAY-SOA-OPERATION-NAME": "findItemsByKeywords",
        "X-EBAY-SOA-SECURITY-APPNAME": "NicoleBo-sandbo-PRD-1dec1ac47-88916303", # replace with your app id
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "JSON",
        "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
        "Authorization": "Bearer " + token
    }
    params = {
        "keywords": keywords,
        "paginationInput.entriesPerPage": pageSize,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
   
    # Check if there is an error
    errors = data.get('errors', [])
    if errors:
        ## when token expires:
        """
        {'errors': [{'errorId': 1001, 'domain': 'OAuth', 'category': 'REQUEST', 'message': 'Invalid access token', 'longMessage': 'Invalid access token. Check the value of the Authorization HTTP request header.'}]}
        """
        print("Error", errors)
        return []
   
    response_items = data['itemSummaries']
    show_items = []

    for item in response_items:
        show_items.append({
            'title': item['title'],
            'price': item['price']['value'] + " " + item['price']['currency'],
            'image': item['thumbnailImages'][0]['imageUrl'],
            'url': item['itemWebUrl']
        })

    return show_items

def home_view(request):
    latest_post = BlogPost.objects.order_by('-date_posted').first()
    query = request.GET.get('q', 'pyrex')
    ebay_listings = fetch_ebay_listings(query)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'ebay_listings': ebay_listings})
    
    return render(request, 'pages/home.html', {'latest_post': latest_post, 'ebay_listings': ebay_listings})

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')