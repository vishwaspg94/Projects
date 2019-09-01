import requests
import ast

base_url = "https://developers.zomato.com/api/v2.1/"
# Multiple user keys
keys = ['fa2d333061a63f2155c7cc9a30620c7c','aac7c0ae1178381ab1448f5f03ed2916']

class Zomato:
    
    def __init__(self):
        """
        Sets the working user key if the previous one has expired
        """
        for user_key in keys:
            self.user_key = user_key            
            headers = {'Accept': 'application/json', 'user-key': self.user_key}
            r = (requests.get(base_url + "categories", headers=headers).content).decode("utf-8")
            a = ast.literal_eval(r)
            if self.is_key_invalid(a) or self.is_rate_exceeded(a):
                continue
            else:
                break

    def is_valid_city(self, city_name):
        """
        Takes City Name as input.
        Returns the ID for the city given as input.
        """
        if city_name.isalpha() == False:
            return ''
        
        city_name = city_name.split(' ')
        city_name = '%20'.join(city_name)
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cities?q=" + city_name, headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)

        if len(a['location_suggestions']) == 0:
            return ''
        elif 'name' in a['location_suggestions'][0]:
            #city_name = city_name.replace('%20', ' ')
            city = str(a['location_suggestions'][0]['name'])
            lr = (requests.get(base_url + "locations?query=" + city + "&count=" + str(1), headers=headers).content).decode("utf-8")
            la = ast.literal_eval(lr)
            latitude = str(la['location_suggestions'][0]['latitude'])
            longitude = str(la['location_suggestions'][0]['longitude'])
            return city + ',' + latitude + ',' + longitude

    def restaurant_search(self, query="", latitude="", longitude="", cuisines="", start=0, count=20):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        cuisines = "%2C".join(cuisines.split(","))
        if str(count).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "search?q=" + str(query) + "&start=" + str(start) + "&count=" + str(count) + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&cuisines=" + str(cuisines), headers=headers).content).decode("utf-8")
        return r

    def is_key_invalid(self, a):
        """
        Checks if the API key provided is valid or invalid.
        If invalid, throws a InvalidKey Exception.
        """
        if 'code' in a:
            if a['code'] == 403:
                return True
        return False

    def is_rate_exceeded(self, a):
        """
        Checks if the request limit for the API key is exceeded or not.
        If exceeded, throws a ApiLimitExceeded Exception.
        """
        if 'code' in a:
            if a['code'] == 440:
                return True
        return False