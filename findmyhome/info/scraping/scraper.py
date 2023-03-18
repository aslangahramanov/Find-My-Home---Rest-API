#### The libraries required for web scraping are imported

import requests
from bs4 import BeautifulSoup as bSoup
import json
from info.models import HomeAds





#######    A web scraping application that extracts data from a defined website based on user choices.


class HomeAdsScraper():
    def __init__(self, city=None, buy_or_rent=None, category=None, rooms=None, min_price=None, max_price=None):
        self.base_url = "https://bina.az"
        self.city = city
        self.buy_or_rent = buy_or_rent
        self.category = category
        self.rooms = rooms
        self.min_price = min_price
        self.max_price = max_price
        
        
        
        
        
    #####   A method that analyzes the data from the user and prepares a dynamic url.
            
    def get_link(self):
        dynamic_url = f"{self.base_url}" + "/"
        if self.city:
            dynamic_url += self.city + "/"
        if self.buy_or_rent:
            dynamic_url += self.buy_or_rent + "/"
        if self.category:
            dynamic_url += self.category + "/"
        if self.rooms:
            dynamic_url += self.rooms + "?"
        if self.min_price:
            if self.min_price and self.max_price:
                dynamic_url += "price_from=" + str(self.min_price) + "&"
            else:
                dynamic_url += "price_from=" + str(self.min_price)
        if self.max_price:
            dynamic_url += "price_to=" + str(self.max_price)
        
        return dynamic_url
    
    
    
    
    
    #####   This method paginates the dynamic url up to a certain number after it is created
    
    def get_pages_link(self):
        links = list(map(lambda num: self.get_link() + f"&page={num}", range(1, 2)))
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
            print("Processing")
            el_source = self.get_source(el_link)
            title = el_source.find("div", attrs={"class": "services-container"}).find("h1").text
            description = el_source.find("div", attrs={"class": "side"}).find("article").find("p").text
            price = el_source.find("span", attrs={"class": "price-val"}).text.replace(" ","")
            currency = el_source.find("span", attrs={"class": "price-cur"}).text
            square_price = el_source.find("div", attrs={"class": "unit-price"}).text if el_source.find("div", attrs={"class": "unit-price"}) else ""
            buy_or_rent = "Alqı-satqı" if square_price else "Kirayə"
            category = list(el_source.find("table", attrs={"class": "parameters"}).find_all("td"))[1].text or ""
            floor = list(el_source.find("table", attrs={"class": "parameters"}).find_all("td"))[3].text or ""
            area = list(el_source.find("table", attrs={"class": "parameters"}).find_all("td"))[5].text or ""
            rooms = list(el_source.find("table", attrs={"class": "parameters"}).find_all("td"))[7].text or ""
            no = list(el_source.find("div", attrs={"class": "item_info"}).find_all("p"))[0].text[16:] or ""
            image_url = el_source.find("div", attrs={"class": "large-photo"}).get("data-mfp-src") or ""
            print(image_url)
            data.append({
                "title": title,
                "description": description,
                "buy_or_rent" : buy_or_rent,
                "price" : int(price),
                "currency" : currency,
                "square_price" : square_price,
                "category" : category,
                "floor" : floor,
                "area" : area,
                "rooms" : rooms,
                "no": no,
                "image_url" : image_url,
            })
            
        return data
    
    
    
    
    
    #####     We convert each element of the data list we received as a result of the
    ####      process into model instance through our model and save 
    ###       it to the database with the bulk create method.
    
    
    def sendtodatabase(self):
        data_set = self.get_elements_data()
        instance_data_set = list()
        for data in data_set:
            instance_data_set.append(HomeAds(**data))
        
        return HomeAds.objects.bulk_create(instance_data_set, ignore_conflicts=True)
        
