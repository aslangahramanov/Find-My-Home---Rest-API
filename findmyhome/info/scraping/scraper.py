#### The libraries required for web scraping are imported

import requests
from bs4 import BeautifulSoup as bSoup



#######    A web scraping application that extracts data from a defined website based on user choices.


class HomeAdsScraper():
    def __init__(self, city, buy_or_rent, category, rooms, min_price, max_price):
        self.base_url = "https://bina.az"
        self.buy_or_rent = buy_or_rent
        self.city = city
        self.category = category
        self.rooms = rooms
        self.min_price = min_price
        self.max_price = max_price
        
        
        
        
    #####   A method that analyzes the data from the user and prepares a dynamic url.
            
    def get_link(self):
        user_link = f"{self.base_url}" + "/"
        if self.city:
            user_link += self.city + "/"
        if self.buy_or_rent:
            user_link += self.buy_or_rent + "/"
        if self.category:
            user_link += self.category + "/"
        if self.rooms:
            user_link += self.rooms + "?"
        if self.min_price:
            if self.min_price and self.max_price:
                user_link += "price_from=" + str(self.min_price) + "&"
            else:
                user_link += "price_from=" + str(self.min_price)
        if self.max_price:
            user_link += "price_to=" + str(self.max_price)
        
        return user_link
    
    
    
    #####   This method paginates the dynamic url up to a certain number after it is created
    
    def get_pages_link(self):
        links = list(map(lambda num: self.get_link() + f"&page={num}", range(1, 6)))
        return links
    
    
    
    ####    Sends request to prepared url and pulls data as BS4 object
            
    def get_source(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            soup = bSoup(request.content, 'html.parser')
            return soup
        else:
            return False
        
        
        
        
    ####    Accesses links by examining the source of each item.
    ####    Avoids duplication by keeping it as a set data type.
        
    def get_elements_link(self, source):
        links = set()
        all_element = source.find_all("div", attrs={"class": "items-i"})
        for element in all_element:
            link = element.find("a", attrs={"class": "item_link"}).get("href")
            if "items" in link:
                link = self.base_url + link
                links.add(link)
            else:
                continue
            
        return links
        
        
        
        
        
    ####    All collected links are looped through and combined with the base url,
    ####    making it ready to receive their source
    
    def get_elements_source(self):
        for link in self.get_pages_link():
            elements_source = self.get_source(link)
            elements_link = self.get_elements_link(elements_source)
        
        return elements_link 
    
    
    
    ####    Pulls the relevant data from the source of each element and freezes it in a list

    
    def get_elements_data(self):
        data = []
        for el_link in self.get_elements_source():
            el_source = self.get_source(el_link)
            title = el_source.find("div", attrs={"class": "services-container"}).find("h1").text
            price = el_source.find("span", attrs={"class": "price-val"}).text
            currency = el_source.find("span", attrs={"class": "price-cur"}).text
            meter_price = el_source.find("div", attrs={"class": "unit-price"}).text
            category = list(el_source.find("table", attrs={"class": "parameters"}).find_all("td"))[1].text or None
            floor = list(el_source.find("table", attrs={"class": "parameters"}).find_all("td"))[3].text or None
            area = list(el_source.find("table", attrs={"class": "parameters"}).find_all("td"))[5].text or None
            rooms = list(el_source.find("table", attrs={"class": "parameters"}).find_all("td"))[7].text or None
            data.append({
                "title": title,
                "price" : price,
                "currency" : currency,
                "meter_price" : meter_price,
                "category" : category,
                "floor" : floor,
                "area" : area,
                "rooms" : rooms,
            })
            
        return data