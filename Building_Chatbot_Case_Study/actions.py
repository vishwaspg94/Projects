from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import warnings
warnings.filterwarnings("ignore")
import re
import json
import smtplib
import zomatopy
import pandas as pd
from fuzzywuzzy import fuzz
from email.message import EmailMessage

from rasa_core.events import SlotSet
from rasa_core.events import AllSlotsReset
from rasa_core.actions.action import Action

# Cuisine dictionary for Zomato
cuisines_dict = {'chinese':25,'mexican':73,'italian':55,'american':1,'north indian':50,'south indian':85}

# Tier I and II city list with their respective zomato city_names
tier_I_II_cities = ['agra','ahmedabad','ajmer','aligarh','allahabad','amravati','amritsar','asansol','aurangabad',
                    'bareilly','belgaum','bengaluru','bhavnagar','bhiwadi','bhopal','bhubaneswar','bijapur','bikaner',
                    'bokaro','chandigarh','chennai','coimbatore','cuttack','dehradun','delhi ncr','dhanbad','dharwad',
                    'durg bhilai','durgapur','erode','firozabad','goa','gorakhpur','gulbarga','guntur','guwahati',
                    'gwalior','hubli','hyderabad','indore','jabalpur','jaipur','jalandhar','jammu','jamnagar',
                    'jamshedpur','jhansi','jodhpur','kakinada','kannur','kanpur','kochi','kolhapur','kolkata','kollam',
                    'kota','kottayam','kozhikode','kurnool','lucknow','ludhiana','madurai','malappuram','mangalore',
                    'mathura','meerut','moradabad','mumbai','mysore','nagpur','nanded','nashik','nellore','palakkad',
                    'patna','pune','raipur','rajahmundry','rajkot','ranchi','rourkela','salem','sangli','siliguri',
                    'solapur','srinagar','surat','thrissur','tirunelveli','tirupati','tiruppur','tiruvannamalai',
                    'trichy','trivandrum','ujjain','vadodara','varanasi','vellore','vijayawada','visakhapatnam','warangal']

def correct_spelling(wrong_word, dictionary, threshold):
    correct_word = wrong_word
    ratio = threshold 
    for word in dictionary:
        qratio = fuzz.QRatio(wrong_word, word)
        if qratio > ratio:
            ratio = qratio
            correct_word = word
    return correct_word

class ActionCheckLocation(Action):
    def name(self):
        return 'action_check_location'
    
    def run(self, dispatcher, tracker, domain):
        try:
            location = tracker.get_slot('location')
            if location:
                location = correct_spelling(location, tier_I_II_cities, 80)
                zomato = zomatopy.Zomato()
            
                location_id = zomato.is_valid_city(location)
                if location_id:
                    if location_id.split(',')[0].lower() in tier_I_II_cities:
                        return [SlotSet('location_id',location_id)]
                    else:
                        dispatcher.utter_template("utter_no_service_location", tracker)
                        return [SlotSet('location',None)]
                else:
                    dispatcher.utter_template("utter_not_a_valid_location", tracker)
                    return [SlotSet('location',None)]
            else:
                dispatcher.utter_template("utter_not_a_valid_location", tracker)
                return [SlotSet('location',None)]
        except:
            dispatcher.utter_template("utter_something_went_wrong", tracker)
    
class ActionCheckCuisine(Action):
    def name(self):
        return 'action_check_cuisine'
    
    def run(self, dispatcher, tracker, domain):
        try:
            cuisine = tracker.get_slot('cuisine')
            cuisine = correct_spelling(cuisine, cuisines_dict, 80)
            if cuisine:
                if cuisine.strip().lower() in cuisines_dict:        
                    return [SlotSet('cuisine',cuisine)]
                else:
                    dispatcher.utter_template("utter_not_a_valid_cuisine", tracker)
                    return [SlotSet('cuisine',None)]
            else:
                dispatcher.utter_template("utter_not_a_valid_cuisine", tracker)
                return [SlotSet('cuisine',None)]
        except:
            dispatcher.utter_template("utter_something_went_wrong", tracker)
        
class ActionCheckBudget(Action):
    def name(self):
        return 'action_check_budget'
    
    def run(self, dispatcher, tracker, domain):
        try:
            budget = tracker.get_slot('budget')

            if budget:
                prices = re.findall('\d+',budget.replace(',',''))
                price_range = ''
                if len(prices) == 0:
                    price_range = '0,100000'
                elif len(prices) == 1:
                    if re.findall('more|great|greater|exceed|exceeding|above|>',budget.lower()):
                        if re.findall('not',budget.lower()):
                            price_range = '0,' + str(prices[0])
                        else:
                            price_range = str(prices[0]) + ',100000'
                    elif re.findall('less|less|lesser|below|<',budget.lower()):
                        if re.findall('not',budget.lower()):
                            price_range = str(prices[0]) + ',100000'
                        else:
                            price_range = '0,' + str(prices[0])
                    else:
                        price_range = '0,' + str(prices[0])
                elif len(prices) > 1:
                    if int(prices[0])<int(prices[1]):
                        price_range = str(prices[0]) + ',' + str(prices[1])
                    else:
                        price_range = str(prices[1]) + ',' + str(prices[0])
                return [SlotSet('budget',price_range)]
            else:
                dispatcher.utter_template("utter_not_a_valid_budget", tracker)
                return [SlotSet('budget','0,100000')]
        except:
            dispatcher.utter_template("utter_something_went_wrong", tracker)
    
class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_restaurant'
    
    def run(self, dispatcher, tracker, domain):
        try:
            response = None
            mail_text = ''
            zomato = zomatopy.Zomato()

            location_id = tracker.get_slot('location_id')
            loc = location_id.split(',')[0]
            lat = location_id.split(',')[1]
            lon = location_id.split(',')[2]
            cuisine = tracker.get_slot('cuisine')
            budget = tracker.get_slot('budget')
            min_price = int(budget.split(',')[0])
            max_price = int(budget.split(',')[1])

            start = 0
            restaurants = json.loads(zomato.restaurant_search('', lat, lon, str(cuisines_dict.get(cuisine)), start))
            results_shown = restaurants['results_shown']

            if results_shown == 0:
                response = None
            else:
                restaurant_list = []

                while results_shown != 0 and start < 5:
                    for restaurant in restaurants['restaurants']:
                        restaurant_list.append([restaurant['restaurant']['name'],
                                                restaurant['restaurant']['location']['address'],
                                                restaurant['restaurant']['location']['locality'],
                                                restaurant['restaurant']['average_cost_for_two'],
                                                restaurant['restaurant']['user_rating']['aggregate_rating']])
                    start += 1
                    restaurants = json.loads(zomato.restaurant_search('', lat, lon, str(cuisines_dict.get(cuisine)), start*20))
                    results_shown = restaurants['results_shown']                

                data = pd.DataFrame(restaurant_list,columns=['name', 'address', 'locality', 'cost_for_two', 'rating'])
                data = data.fillna(0)
                data = data.astype({"cost_for_two": int, "rating": float})
                data = data[(data['cost_for_two']>=min_price) & (data['cost_for_two']<=max_price)]            

                if len(data)>0:
                    data.sort_values(by='rating',ascending=False,inplace=True)
                    data.reset_index(drop=True, inplace=True)
                    response = 'Found the below restaurants serving ' + cuisine + ' in ' + loc + '\n'
                    for row in range(5 if len(data)>=5 else len(data)):
                        response += str(row+1) + '. ' + str(data.loc[row,'name']) + ' in ' + str(data.loc[row,'address']) + ' has been rated ' + str(data.loc[row,'rating']) + '\n'

                    mail_text = 'Hi, \n\nPlease find the list of restaurants serving ' + cuisine + ' in ' + loc + '\n\n'
                    for row in range(10 if len(data)>=10 else len(data)):
                        mail_text += str(row+1) + '. Restaurant : ' + str(data.loc[row,'name']) + '\n'
                        mail_text += '    Locality : ' + str(data.loc[row,'locality']) + '\n'
                        mail_text += '    Average cost for two : ' + str(data.loc[row,'cost_for_two']) + '\n'
                        mail_text += '    Rating : ' + str(data.loc[row,'rating']) + '\n\n'
                else:
                    response = None
            if response:
                dispatcher.utter_message(response)
                return [SlotSet('mail_text',mail_text)]
            else:
                response = 'Sorry, we could not find any restaurants serving ' + cuisine + ' in ' + loc
                dispatcher.utter_message(response)
                return[AllSlotsReset()]
        except:
            dispatcher.utter_template("utter_something_went_wrong", tracker)       
    
class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'
    
    def run(self, dispatcher, tracker, domain):
        try:
            msg = EmailMessage()

            mail_text = tracker.get_slot('mail_text')
            to_mail_id = tracker.get_slot('mail_id')

            msg.set_content(mail_text)
            msg['Subject'] = 'Location Details from Foodie'
            msg['From'] = 'foodiechatbot.2019@gmail.com'
            msg['To'] = to_mail_id
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("foodiechatbot.2019@gmail.com", "foodie@2019")
            server.send_message(msg)
            server.quit()

            dispatcher.utter_template("utter_mail_sent", tracker)
            return[AllSlotsReset()]
        except:
            dispatcher.utter_template("utter_something_went_wrong", tracker)
            
class ActionGoodBye(Action):
    def name(self):
        return 'action_goodbye'
    
    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_template("utter_goodbye", tracker)
            return[AllSlotsReset()]
        except:
            dispatcher.utter_template("utter_something_went_wrong", tracker)