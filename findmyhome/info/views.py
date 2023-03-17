from django.shortcuts import render, redirect
from info.scraping.scraper import HomeAdsScraper



def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        data = request.POST
        city = data.get("city")
        buy_or_rent = data.get("buy-or-rent")
        category = data.get("category")
        rooms = data.get("rooms")
        min_price = data.get("min-price")
        max_price = data.get("max-price")
        HomeAdsScraper(city=city, buy_or_rent=buy_or_rent, category=category, rooms=rooms, min_price=min_price, max_price=max_price).sendtodatabase()
    return render(request, 'index.html')
            
        