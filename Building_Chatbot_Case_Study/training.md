## Generated Story 424779093130289311
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location{"location": "hubli"}
    - slot{"location": "hubli"}
    - action_check_location
    - slot{"location_id": "Hubli,15.364683,75.123944"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* check_budget{"budget": "200-500"}
    - slot{"budget": "200-500"}
    - action_check_budget
    - slot{"budget": "200,500"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving south indian in Hubli\n\n1. Restaurant : Hotel Shree Ganesh\n    Locality : Keshwapur\n    Average cost for two : 300\n    Rating : 4.3\n\n2. Restaurant : Paradise Kitchen Hyderabadi Biryani\n    Locality : Vidya Nagar\n    Average cost for two : 300\n    Rating : 4.1\n\n3. Restaurant : Curry Weds RICE\n    Locality : Vidya Nagar\n    Average cost for two : 300\n    Rating : 4.1\n\n4. Restaurant : Hotel Shri Sai\n    Locality : Vidya Nagar\n    Average cost for two : 250\n    Rating : 4.0\n\n5. Restaurant : Hotel Shree Vaibhav\n    Locality : Vidya Nagar\n    Average cost for two : 500\n    Rating : 4.0\n\n6. Restaurant : Gokul Restaurant (Pure veg)\n    Locality : Rajendra Nagar\n    Average cost for two : 300\n    Rating : 3.9\n\n7. Restaurant : Big Mishra Pedha\n    Locality : New Hubli\n    Average cost for two : 300\n    Rating : 3.9\n\n8. Restaurant : Brahmashree Fishland\n    Locality : New Hubli\n    Average cost for two : 200\n    Rating : 3.9\n\n9. Restaurant : Ellora Family Restaurant\n    Locality : New Hubli\n    Average cost for two : 250\n    Rating : 3.9\n\n10. Restaurant : Renukadevi lingayath kanavali\n    Locality : Rajendra Nagar\n    Average cost for two : 200\n    Rating : 3.8\n\n"}
    - utter_ask_for_sending_mail
* affirm
    - utter_ask_for_mail_id
* send_mail{"mail_id": "sahooaniket@gmail.com"}
    - slot{"mail_id": "sahooaniket@gmail.com"}
    - action_send_mail
    - slot{"mail_text": null}
    - utter_need_anything_else
* deny
    - utter_goodbye
    - export

## Generated Story -4530325296969760743
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location{"location": "Indore"}
    - action_check_location
    - slot{"location_id": "Indore,22.7252,75.857"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
    - action_check_budget
    - slot{"budget": "300,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving mexican in Indore\n\n1. Restaurant : Hobnob Gourmet Caf\u00e9bar\n    Locality : Infiniti Hotel, Vijay Nagar\n    Average cost for two : 1950\n    Rating : 4.6\n\n2. Restaurant : Little Italy\n    Locality : Vijay Nagar\n    Average cost for two : 1400\n    Rating : 4.4\n\n3. Restaurant : Mr. Beans\n    Locality : Old Palasia\n    Average cost for two : 800\n    Rating : 4.3\n\n4. Restaurant : Mama Loca\n    Locality : New Palasia\n    Average cost for two : 1100\n    Rating : 4.3\n\n5. Restaurant : Mocha\n    Locality : YN Road\n    Average cost for two : 800\n    Rating : 4.2\n\n6. Restaurant : Chef's Alcove\n    Locality : Rau\n    Average cost for two : 850\n    Rating : 4.2\n\n7. Restaurant : Just My Bakes\n    Locality : Vijay Nagar\n    Average cost for two : 700\n    Rating : 4.1\n\n8. Restaurant : 5/78 Skybar\n    Locality : Vijay Nagar\n    Average cost for two : 1875\n    Rating : 4.1\n\n9. Restaurant : The Creative Kitchen - Radisson Blu Hotel\n    Locality : Radisson Blu Hotel, Vijay Nagar\n    Average cost for two : 2000\n    Rating : 4.1\n\n10. Restaurant : Go Bananas - Sayaji Hotel\n    Locality : Sayaji Hotel, Vijay Nagar\n    Average cost for two : 1000\n    Rating : 4.1\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
* deny
    - export

## Generated Story -7382941844581426098
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_id": "Mangalore,12.87,74.88"}
    - utter_ask_cuisine
* check_cuisine
    - action_check_cuisine
    - slot{"cuisine": null}
* check_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_check_budget
    - slot{"budget": "300,700"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Mangalore\n\n1. Restaurant : William Pereira Hotel\n    Locality : Hampankatta\n    Average cost for two : 600\n    Rating : 4.2\n\n2. Restaurant : Dinki Dine\n    Locality : Kadri\n    Average cost for two : 500\n    Rating : 4.2\n\n3. Restaurant : Maharaja Restaurant\n    Locality : Balmatta\n    Average cost for two : 700\n    Rating : 4.2\n\n4. Restaurant : Brick House\n    Locality : Hampankatta\n    Average cost for two : 500\n    Rating : 4.2\n\n5. Restaurant : Shetty Lunch Home\n    Locality : Balmatta\n    Average cost for two : 500\n    Rating : 4.2\n\n6. Restaurant : Anmol Family Veg Restaurant\n    Locality : Lalbagh\n    Average cost for two : 400\n    Rating : 4.2\n\n7. Restaurant : Thyme Family Restaurant\n    Locality : Lalbagh\n    Average cost for two : 700\n    Rating : 4.2\n\n8. Restaurant : Sagar Ratna\n    Locality : The Ocean Pearl, Kodailbail\n    Average cost for two : 700\n    Rating : 4.1\n\n9. Restaurant : Juice Romantic\n    Locality : Kadri\n    Average cost for two : 400\n    Rating : 4.1\n\n10. Restaurant : Hao Ming\n    Locality : Balmatta\n    Average cost for two : 600\n    Rating : 4.1\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "ahbcdj@dkj.com"}
    - slot{"mail_id": "ahbcdj@dkj.com"}
    - action_send_mail
    - slot{"mail_text": null}
    - utter_need_anything_else
* deny
    - utter_goodbye
    - export

## Generated Story 5880471684570647838
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_check_location
    - slot{"location_id": "Allahabad,25.45,81.85"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_check_budget
    - slot{"budget": "700,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Allahabad\n\n1. Restaurant : EDEN by Connoisseur\n    Locality : Civil Lines\n    Average cost for two : 1000\n    Rating : 4.6\n\n2. Restaurant : El Chico Restaurant\n    Locality : Civil Lines\n    Average cost for two : 800\n    Rating : 4.5\n\n3. Restaurant : Old School Cafe\n    Locality : Civil Lines\n    Average cost for two : 1000\n    Rating : 4.4\n\n4. Restaurant : Pind Balluchi\n    Locality : Civil Lines\n    Average cost for two : 1000\n    Rating : 4.3\n\n5. Restaurant : Berco's\n    Locality : Civil Lines\n    Average cost for two : 1600\n    Rating : 4.1\n\n6. Restaurant : Moti Mahal Delux\n    Locality : Vinayak City Centre Mall, Civil Lines\n    Average cost for two : 850\n    Rating : 4.1\n\n7. Restaurant : Makkhan's\n    Locality : Civil Lines\n    Average cost for two : 1000\n    Rating : 4.1\n\n8. Restaurant : Haldiram Bhujiawala\n    Locality : Civil Lines\n    Average cost for two : 700\n    Rating : 4.1\n\n9. Restaurant : Kohinoor Restaurant\n    Locality : Civil Lines\n    Average cost for two : 800\n    Rating : 4.0\n\n10. Restaurant : Relish Restaurant- The Legend Hotel\n    Locality : The Legend Hotel\n    Average cost for two : 1100\n    Rating : 4.0\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "xyz@sth.edu"}
    - slot{"mail_id": "xyz@sth.edu"}
    - action_send_mail
    - utter_need_anything_else
* deny
    - utter_goodbye
    - export

## Generated Story 4427179112093739486
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location_id": "Chandigarh,30.737793,76.77515"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "above 500"}
    - slot{"budget": "above 500"}
    - action_check_budget
    - slot{"budget": "500,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Chandigarh\n\n1. Restaurant : The Great Bear\n    Locality : Sector 26\n    Average cost for two : 1600\n    Rating : 4.9\n\n2. Restaurant : Baithak\n    Locality : Manimajra\n    Average cost for two : 1200\n    Rating : 4.8\n\n3. Restaurant : Hops n Grains\n    Locality : Sector 9\n    Average cost for two : 2100\n    Rating : 4.7\n\n4. Restaurant : Beach N Brew\n    Locality : Sector 26\n    Average cost for two : 1800\n    Rating : 4.7\n\n5. Restaurant : Qizo\n    Locality : Sector 26\n    Average cost for two : 1600\n    Rating : 4.7\n\n6. Restaurant : Sector 7 Social\n    Locality : Sector 7\n    Average cost for two : 1400\n    Rating : 4.6\n\n7. Restaurant : Barbeque Nation\n    Locality : Sector 26\n    Average cost for two : 1300\n    Rating : 4.6\n\n8. Restaurant : Barbeque Nation\n    Locality : Phase 5\n    Average cost for two : 1300\n    Rating : 4.6\n\n9. Restaurant : Pirates of Grill\n    Locality : Elante Mall, Chandigarh Industrial Area\n    Average cost for two : 1200\n    Rating : 4.6\n\n10. Restaurant : SHANGZ\n    Locality : Sector 8\n    Average cost for two : 500\n    Rating : 4.5\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
* deny
    - export

## Generated Story 5689369387984832589
* greet
    - utter_greet
* restaurant_search{"location": "cuttack", "cuisine": "chinese", "budget": "below 500"}
    - slot{"budget": "below 500"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "cuttack"}
    - action_check_location
    - slot{"location_id": "Cuttack,20.46252,85.882989"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - action_check_budget
    - slot{"budget": "0,500"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Cuttack\n\n1. Restaurant : Tastry\n    Locality : Buxi Bazaar\n    Average cost for two : 400\n    Rating : 3.9\n\n2. Restaurant : Blast\n    Locality : Siba Bazaar\n    Average cost for two : 500\n    Rating : 3.9\n\n3. Restaurant : Hotel Neeladri\n    Locality : Siba Bazaar\n    Average cost for two : 500\n    Rating : 3.9\n\n4. Restaurant : Meals and Memories\n    Locality : Buxi Bazaar\n    Average cost for two : 500\n    Rating : 3.9\n\n5. Restaurant : The Cocktail\n    Locality : Police Colony\n    Average cost for two : 500\n    Rating : 3.9\n\n6. Restaurant : Baromishali Bengali Restaurant\n    Locality : CDA Sector 6\n    Average cost for two : 350\n    Rating : 3.8\n\n7. Restaurant : DFC Dada's Biryani\n    Locality : Buxi Bazaar\n    Average cost for two : 400\n    Rating : 3.8\n\n8. Restaurant : Bawarchi Restaurant\n    Locality : Siba Bazaar\n    Average cost for two : 500\n    Rating : 3.8\n\n9. Restaurant : Bawarchi Fast Food\n    Locality : Siba Bazaar\n    Average cost for two : 300\n    Rating : 3.8\n\n10. Restaurant : Dexter's\n    Locality : CDA Sector 6\n    Average cost for two : 500\n    Rating : 3.8\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "xyz@fhg.im"}
    - slot{"mail_id": "xyz@fhg.im"}
    - action_send_mail
    - slot{"mail_text": null}
    - utter_need_anything_else
* affirm
    - utter_ask_howcanhelp
* out_of_scope
    - utter_cannot_help
* goodbye
    - utter_goodbye
    - export

## Generated Story -1688753086485219726
* restaurant_search{"location": "delhi", "cuisine": "chinese", "budget": "range of 200 to 400"}
    - slot{"budget": "range of 200 to 400"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_location
* check_location{"location": "belgaum"}
    - slot{"location": "belgaum"}
    - action_check_location
    - slot{"location_id": "Belgaum,15.8496953,74.4976741"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - action_check_budget
    - slot{"budget": "200,400"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Belgaum\n\n1. Restaurant : Masterchef's - Tilakwadi\n    Locality : Belgaum Locality\n    Average cost for two : 300\n    Rating : 4.4\n\n2. Restaurant : Donne Biriyani Adda\n    Locality : Belgaum Locality\n    Average cost for two : 300\n    Rating : 4.3\n\n3. Restaurant : Masterchef's - Nehru Nagar\n    Locality : Belgaum Locality\n    Average cost for two : 300\n    Rating : 4.3\n\n4. Restaurant : Al Bahar\n    Locality : Belgaum Locality\n    Average cost for two : 300\n    Rating : 4.3\n\n5. Restaurant : Hotel Niyaaz\n    Locality : Belgaum Locality\n    Average cost for two : 250\n    Rating : 4.2\n\n6. Restaurant : Munch Cafe & Resto\n    Locality : Belgaum Locality\n    Average cost for two : 300\n    Rating : 4.0\n\n7. Restaurant : Grand China\n    Locality : Belgaum Locality\n    Average cost for two : 200\n    Rating : 3.9\n\n8. Restaurant : Hotel New Green Taj\n    Locality : Belgaum Locality\n    Average cost for two : 300\n    Rating : 3.9\n\n9. Restaurant : Chinese Dhaba\n    Locality : Belgaum Locality\n    Average cost for two : 200\n    Rating : 3.7\n\n10. Restaurant : Sunil Fast Food\n    Locality : Belgaum Locality\n    Average cost for two : 300\n    Rating : 3.7\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "xyz@fgh.co.in"}
    - slot{"mail_id": "xyz@fgh.co.in"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
* deny
    - utter_goodbye
    - export

## Generated Story -7792110150260814036
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location{"location": "dhenkanal"}
    - slot{"location": "dhenkanal"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "amritsart"}
    - slot{"location": "amritsart"}
    - action_check_location
    - slot{"location_id": "Amritsar,31.64,74.86"}
    - utter_ask_cuisine
* check_cuisine
    - action_check_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "around 400"}
    - slot{"budget": "around 400"}
    - action_check_budget
    - slot{"budget": "0,400"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving mexican in Amritsar\n\n1. Restaurant : Publik\n    Locality : Ranjit Avenue\n    Average cost for two : 400\n    Rating : 3.3\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "abc.text@g.com"}
    - slot{"mail_id": "abc.text@g.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
* deny
    - utter_goodbye
    - export

## Generated Story -3662911745256794097
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* check_location{"location": "dehradun"}
    - slot{"location": "dehradun"}
    - action_check_location
    - slot{"location_id": "Dehradun,30.318,78.029"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "less than 200"}
    - slot{"budget": "less than 200"}
    - action_check_budget
    - slot{"budget": "0,200"}
    - action_restaurant
    - slot{"mail_text": ""}
    - utter_goodbye
    - export

## Generated Story 7384152129691369345
* restaurant_search{"cuisine": "mexican", "location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "more than 500"}
    - slot{"budget": "more than 500"}
    - action_check_budget
    - slot{"budget": "500,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving mexican in Mumbai\n\n1. Restaurant : Palladium Social\n    Locality : Palladium Mall, Lower Parel\n    Average cost for two : 1400\n    Rating : 4.9\n\n2. Restaurant : Colaba Social\n    Locality : Colaba\n    Average cost for two : 1400\n    Rating : 4.8\n\n3. Restaurant : Hitchki\n    Locality : First International Financial Centre, Bandra Kurla Complex\n    Average cost for two : 1600\n    Rating : 4.8\n\n4. Restaurant : Hitchki\n    Locality : Powai\n    Average cost for two : 1600\n    Rating : 4.8\n\n5. Restaurant : Bayroute\n    Locality : Juhu\n    Average cost for two : 3000\n    Rating : 4.8\n\n6. Restaurant : Drinkery 51\n    Locality : Bandra Kurla Complex\n    Average cost for two : 2000\n    Rating : 4.7\n\n7. Restaurant : Lord of the Drinks\n    Locality : Kamala Mills Compound\n    Average cost for two : 2100\n    Rating : 4.7\n\n8. Restaurant : JLWA\n    Locality : Linking Road, Bandra West\n    Average cost for two : 2500\n    Rating : 4.7\n\n9. Restaurant : London Taxi\n    Locality : Kamala Mills Compound\n    Average cost for two : 1800\n    Rating : 4.7\n\n10. Restaurant : Pot Pourri\n    Locality : Cubic Mall, Chembur\n    Average cost for two : 2000\n    Rating : 4.7\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
* deny
    - export

## Generated Story 6473955497625535615
* greet
    - utter_greet
* restaurant_search{"location": "virar", "cuisine": "north indian", "budget": "between 200 and 1000"}
    - slot{"budget": "between 200 and 1000"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "virar"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_location
* check_location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_check_location
    - slot{"location_id": "Hyderabad,17.366,78.476"}
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - action_check_budget
    - slot{"budget": "200,1000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving north indian in Hyderabad\n\n1. Restaurant : Paradise\n    Locality : Paradise Circle\n    Average cost for two : 800\n    Rating : 4.9\n\n2. Restaurant : Paradise\n    Locality : Gachibowli\n    Average cost for two : 800\n    Rating : 4.6\n\n3. Restaurant : Ohri's De Thali\n    Locality : Begumpet\n    Average cost for two : 900\n    Rating : 4.6\n\n4. Restaurant : Ohri's Gufaa\n    Locality : Basheer Bagh\n    Average cost for two : 1000\n    Rating : 4.5\n\n5. Restaurant : Paradise\n    Locality : Hitech City\n    Average cost for two : 800\n    Rating : 4.5\n\n6. Restaurant : 4M Biryani House\n    Locality : Musheerabad\n    Average cost for two : 250\n    Rating : 4.4\n\n7. Restaurant : NorFest - The Dhaba\n    Locality : SLN Terminus,Gachibowli\n    Average cost for two : 550\n    Rating : 4.4\n\n8. Restaurant : Paradise\n    Locality : Begumpet\n    Average cost for two : 800\n    Rating : 4.4\n\n9. Restaurant : Ohri's Pickles - Hotel Baseraa\n    Locality : Hotel Baseraa, S D Road\n    Average cost for two : 1000\n    Rating : 4.4\n\n10. Restaurant : Mehfil Restaurant\n    Locality : Shamshabad\n    Average cost for two : 600\n    Rating : 4.3\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
* thankyou
    - utter_thankyou
    - export

## Generated Story -6045870571399151005
* greet
    - utter_greet
* restaurant_search{"budget": "cost below 200"}
    - slot{"budget": "cost below 200"}
    - utter_ask_location
* check_location{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_id": "Nashik,20,73.78"}
    - utter_ask_cuisine
* check_cuisine
    - action_check_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - action_check_budget
    - slot{"budget": "0,200"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Nashik\n\n1. Restaurant : Sai Pavbhaji & Nashta Center\n    Locality : Nashik Road\n    Average cost for two : 200\n    Rating : 4.2\n\n2. Restaurant : Lollypop Restaurant\n    Locality : Parijat Nagar\n    Average cost for two : 150\n    Rating : 4.0\n\n3. Restaurant : Hotel Jay Durga\n    Locality : Sharanpur\n    Average cost for two : 150\n    Rating : 4.0\n\n4. Restaurant : Rock n' Roll\n    Locality : College Road\n    Average cost for two : 200\n    Rating : 3.9\n\n5. Restaurant : Bapu's Chinese Centre\n    Locality : Nashik Road\n    Average cost for two : 200\n    Rating : 3.8\n\n6. Restaurant : Dishaan Chinese Corner\n    Locality : Panchavati\n    Average cost for two : 200\n    Rating : 3.7\n\n7. Restaurant : Nakshtra's Chinese Corner\n    Locality : Nashik Road\n    Average cost for two : 200\n    Rating : 3.6\n\n8. Restaurant : Sai Chinese Corner\n    Locality : College Road\n    Average cost for two : 200\n    Rating : 3.6\n\n9. Restaurant : Al-Akbar\n    Locality : Doodh Bazar\n    Average cost for two : 150\n    Rating : 3.4\n\n10. Restaurant : Sai Shradha Pavbhaji Center\n    Locality : Panchavati\n    Average cost for two : 150\n    Rating : 3.3\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "sahoo@gmail.com"}
    - slot{"mail_id": "sahoo@gmail.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
* deny
    - utter_goodbye
    - export

## Generated Story -3098630434528420165
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "below 200"}
    - slot{"budget": "below 200"}
    - action_check_budget
    - slot{"budget": "0,200"}
    - action_restaurant
    - slot{"mail_text": ""}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
    - export

## Generated Story 1331910194814080332
* restaurant_search{"location": "vashi", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "vashi"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_location
* check_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "for 400"}
    - slot{"budget": "for 400"}
    - action_check_budget
    - slot{"budget": "0,400"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Mumbai\n\n1. Restaurant : Uncle's Kitchen\n    Locality : Malad West\n    Average cost for two : 300\n    Rating : 3.8\n\n"}
    - utter_goodbye
    - export

## Generated Story -8567899889277684040
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location{"location": "manhattan"}
    - slot{"location": "manhattan"}
    - action_check_location
    - slot{"location": null}
* check_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - utter_ask_cuisine
* check_cuisine
    - action_check_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* check_budget{"budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - action_check_budget
    - slot{"budget": "0,300"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving italian in Mumbai\n\n1. Restaurant : Joe's Pizza\n    Locality : Khar\n    Average cost for two : 200\n    Rating : 3.7\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "aniket@g.com"}
    - slot{"mail_id": "aniket@g.com"}
    - action_send_mail
    - reset_slots
    - export

## Generated Story -2503191191394754098
* restaurant_search{"location": "odisha"}
    - slot{"location": "odisha"}
    - action_check_location
    - slot{"location": null}
* check_location{"location": "surat"}
    - slot{"location": "surat"}
    - action_check_location
    - slot{"location_id": "Surat,21.17,72.83"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search
    - action_check_budget
    - slot{"budget": "0,100000"}
* check_budget{"budget": "above 200"}
    - slot{"budget": "above 200"}
    - action_check_budget
    - slot{"budget": "200,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Surat\n\n1. Restaurant : Coffee King\n    Locality : Adajan Gam\n    Average cost for two : 500\n    Rating : 4.6\n\n2. Restaurant : 3Seventy Kitchen\n    Locality : Pal Gam\n    Average cost for two : 700\n    Rating : 4.5\n\n3. Restaurant : Golden Dragon\n    Locality : Athwa\n    Average cost for two : 800\n    Rating : 4.4\n\n4. Restaurant : Steam\n    Locality : Valentine Mall, Dumas\n    Average cost for two : 700\n    Rating : 4.4\n\n5. Restaurant : Jakaas Chinese Food\n    Locality : Adajan Gam\n    Average cost for two : 350\n    Rating : 4.4\n\n6. Restaurant : Singh Saaab Di Rasoi\n    Locality : Piplod\n    Average cost for two : 800\n    Rating : 4.3\n\n7. Restaurant : The Sizzling Salsa\n    Locality : Piplod\n    Average cost for two : 1500\n    Rating : 4.3\n\n8. Restaurant : Geetha Restaurant\n    Locality : Vesu\n    Average cost for two : 400\n    Rating : 4.3\n\n9. Restaurant : Flow - The Gateway Hotel\n    Locality : The Gateway Hotel, Athwa\n    Average cost for two : 1700\n    Rating : 4.3\n\n10. Restaurant : Nareshbhai Bhelwala\n    Locality : New Textile Market\n    Average cost for two : 200\n    Rating : 4.2\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "mail@mail.com"}
    - slot{"mail_id": "mail@mail.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
* thankyou
    - utter_thankyou
    - export

## Generated Story 9145933482055743488
* greet
    - utter_greet
* restaurant_search{"location": "bihar", "cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bihar"}
    - action_check_location
    - slot{"location": null}
* check_location{"location": "secunderabad"}
    - slot{"location": "secunderabad"}
    - action_check_location
    - slot{"location_id": "Hyderabad,17.366,78.476"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "200-599"}
    - slot{"budget": "200-599"}
    - action_check_budget
    - slot{"budget": "200,599"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving mexican in Hyderabad\n\n1. Restaurant : Burgasm\n    Locality : Banjara Hills\n    Average cost for two : 400\n    Rating : 4.3\n\n2. Restaurant : Drunken Monkey\n    Locality : Madhapur\n    Average cost for two : 400\n    Rating : 4.1\n\n3. Restaurant : Domino's Pizza\n    Locality : Hitech City\n    Average cost for two : 400\n    Rating : 3.7\n\n4. Restaurant : Tortilla's\n    Locality : Panjagutta\n    Average cost for two : 500\n    Rating : 3.5\n\n5. Restaurant : Delicio Taco Truck\n    Locality : Gachibowli\n    Average cost for two : 250\n    Rating : 3.5\n\n6. Restaurant : Smokinn Barbecue & Mexican\n    Locality : Jubilee Hills\n    Average cost for two : 200\n    Rating : 3.2\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "aniket@g.com"}
    - slot{"mail_id": "aniket@g.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
    - export

## Generated Story 3558911532250203940
* greet
    - utter_greet
* restaurant_search{"location": "bihar"}
    - slot{"location": "bihar"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "illahabad"}
    - slot{"location": "illahabad"}
    - action_check_location
    - slot{"location_id": "Allahabad,25.45,81.85"}
    - utter_ask_cuisine
* check_location
    - action_check_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* check_budget
    - action_check_budget
    - slot{"budget": "0,100000"}
* check_budget{"budget": "below 500"}
    - slot{"budget": "below 500"}
    - action_check_budget
    - slot{"budget": "0,500"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving italian in Allahabad\n\n1. Restaurant : Coffee Machine The Cafe\n    Locality : Civil Lines\n    Average cost for two : 250\n    Rating : 4.3\n\n2. Restaurant : Mr. Dewsis\n    Locality : Civil Lines\n    Average cost for two : 500\n    Rating : 4.1\n\n3. Restaurant : Hot n Cool\n    Locality : Colonel Ganj\n    Average cost for two : 450\n    Rating : 4.1\n\n4. Restaurant : 7th Heaven\n    Locality : Civil Lines\n    Average cost for two : 400\n    Rating : 4.1\n\n5. Restaurant : Hot n Cool\n    Locality : Naini\n    Average cost for two : 300\n    Rating : 4.1\n\n6. Restaurant : Chicago Pizza\n    Locality : Civil Lines\n    Average cost for two : 400\n    Rating : 4.1\n\n7. Restaurant : Chicago Pizza\n    Locality : Katra\n    Average cost for two : 400\n    Rating : 4.1\n\n8. Restaurant : Domino's Pizza\n    Locality : George Town\n    Average cost for two : 400\n    Rating : 3.9\n\n9. Restaurant : Domino's Pizza\n    Locality : Civil Lines\n    Average cost for two : 400\n    Rating : 3.9\n\n10. Restaurant : Domino's Pizza\n    Locality : Civil Lines\n    Average cost for two : 400\n    Rating : 3.9\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - export

## Generated Story -1257548393311848552
* restaurant_search{"cuisine": "chinese", "location": "price"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "price"}
    - action_check_location
    - slot{"location": null}
* check_location{"location": "kakinada"}
    - slot{"location": "kakinada"}
    - action_check_location
    - slot{"location_id": "Kakinada,16.9890648,82.2474648"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": ">40"}
    - slot{"budget": ">40"}
    - action_check_budget
    - slot{"budget": "40,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Kakinada\n\n1. Restaurant : Hungry Birds\n    Locality : Kakinada Locality\n    Average cost for two : 800\n    Rating : 4.3\n\n2. Restaurant : Jaya Residency\n    Locality : Kakinada Locality\n    Average cost for two : 500\n    Rating : 4.2\n\n3. Restaurant : Kshatriyafoods\n    Locality : Kakinada Locality\n    Average cost for two : 400\n    Rating : 4.2\n\n4. Restaurant : The Food Factory\n    Locality : Kakinada Locality\n    Average cost for two : 600\n    Rating : 4.2\n\n5. Restaurant : Biryanis and More\n    Locality : Kakinada Locality\n    Average cost for two : 400\n    Rating : 4.2\n\n6. Restaurant : Bhimas Family Restaurant\n    Locality : Kakinada Locality\n    Average cost for two : 450\n    Rating : 4.1\n\n7. Restaurant : Ulavacharu Restaurant\n    Locality : Kakinada Locality\n    Average cost for two : 350\n    Rating : 4.1\n\n8. Restaurant : Kshatriya Foods\n    Locality : Kakinada Locality\n    Average cost for two : 400\n    Rating : 4.1\n\n9. Restaurant : Eat More\n    Locality : Kakinada Locality\n    Average cost for two : 300\n    Rating : 4.1\n\n10. Restaurant : Lotus Park\n    Locality : Kakinada Locality\n    Average cost for two : 600\n    Rating : 4.1\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
* restaurant_search{"location": "vishakhapatnam"}
    - slot{"location": "vishakhapatnam"}
    - action_check_location
    - slot{"location_id": "Visakhapatnam,17.6883,83.2186"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "> 400"}
    - slot{"budget": "> 400"}
    - action_check_budget
    - slot{"budget": "400,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Visakhapatnam\n\n1. Restaurant : Barbeque Nation\n    Locality : Kirlampudi Layout\n    Average cost for two : 1600\n    Rating : 4.9\n\n2. Restaurant : Mekong - Hotel GreenPark\n    Locality : Hotel GreenPark, Vizag\n    Average cost for two : 1300\n    Rating : 4.7\n\n3. Restaurant : R&G - Hotel GreenPark\n    Locality : Hotel GreenPark, Vizag\n    Average cost for two : 1100\n    Rating : 4.6\n\n4. Restaurant : Kamat Restaurant\n    Locality : Lawsons Bay\n    Average cost for two : 800\n    Rating : 4.5\n\n5. Restaurant : Myz-Uno Brew Pub\n    Locality : Siripuram\n    Average cost for two : 1400\n    Rating : 4.4\n\n6. Restaurant : Ming Garden - The Gateway Hotel\n    Locality : The Gateway Hotel, Maharani Peta \n    Average cost for two : 2000\n    Rating : 4.4\n\n7. Restaurant : Fresh Choice Bakery\n    Locality : Asilmetta\n    Average cost for two : 400\n    Rating : 4.4\n\n8. Restaurant : Pier 57\n    Locality : Jagadamba Junction\n    Average cost for two : 1000\n    Rating : 4.3\n\n9. Restaurant : Rasa\n    Locality : Siripuram\n    Average cost for two : 700\n    Rating : 4.3\n\n10. Restaurant : Satyam Non-Veg Restaurant\n    Locality : Dwaraka Nagar\n    Average cost for two : 400\n    Rating : 4.2\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "a@a.com"}
    - slot{"mail_id": "a@a.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
* restaurant_search{"location": "madhya"}
    - slot{"location": "madhya"}
    - action_check_location
    - slot{"location": null}
* check_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "more than 400"}
    - slot{"budget": "more than 400"}
    - action_check_budget
    - slot{"budget": "400,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving mexican in Mumbai\n\n1. Restaurant : Palladium Social\n    Locality : Palladium Mall, Lower Parel\n    Average cost for two : 1400\n    Rating : 4.9\n\n2. Restaurant : Hitchki\n    Locality : Powai\n    Average cost for two : 1600\n    Rating : 4.8\n\n3. Restaurant : Bayroute\n    Locality : Juhu\n    Average cost for two : 3000\n    Rating : 4.8\n\n4. Restaurant : Colaba Social\n    Locality : Colaba\n    Average cost for two : 1400\n    Rating : 4.8\n\n5. Restaurant : Hitchki\n    Locality : First International Financial Centre, Bandra Kurla Complex\n    Average cost for two : 1600\n    Rating : 4.8\n\n6. Restaurant : 145 Kala Ghoda\n    Locality : Fort\n    Average cost for two : 1500\n    Rating : 4.7\n\n7. Restaurant : Tamasha\n    Locality : Lower Parel\n    Average cost for two : 2700\n    Rating : 4.7\n\n8. Restaurant : Lord of the Drinks\n    Locality : Kamala Mills Compound\n    Average cost for two : 2100\n    Rating : 4.7\n\n9. Restaurant : Drinkery 51\n    Locality : Bandra Kurla Complex\n    Average cost for two : 2000\n    Rating : 4.7\n\n10. Restaurant : London Taxi\n    Locality : Kamala Mills Compound\n    Average cost for two : 1800\n    Rating : 4.7\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - export

## Generated Story 6877549661069343909
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - utter_ask_cuisine
* check_cuisine
    - action_check_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* check_budget{"budget": "500 to 600"}
    - slot{"budget": "500 to 600"}
    - action_check_budget
    - slot{"budget": "500,600"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving south indian in Mumbai\n\n1. Restaurant : Gughan Supreme South Indian\n    Locality : Marine Lines\n    Average cost for two : 500\n    Rating : 4.6\n\n2. Restaurant : Madrasam\n    Locality : Versova, Andheri West\n    Average cost for two : 500\n    Rating : 4.5\n\n3. Restaurant : Dakshinayan\n    Locality : Juhu\n    Average cost for two : 600\n    Rating : 4.3\n\n4. Restaurant : Dakshinayan\n    Locality : Malabar Hill\n    Average cost for two : 600\n    Rating : 3.9\n\n5. Restaurant : Udipi Sri Krishna\n    Locality : Matunga East\n    Average cost for two : 500\n    Rating : 3.9\n\n6. Restaurant : Balaji Idli House\n    Locality : Ghatkopar West\n    Average cost for two : 500\n    Rating : 3.8\n\n7. Restaurant : Balaji Idli House\n    Locality : Kandivali West\n    Average cost for two : 500\n    Rating : 3.6\n\n8. Restaurant : YumYumSouth\n    Locality : Worli\n    Average cost for two : 600\n    Rating : 3.3\n\n9. Restaurant : YumYumSouth\n    Locality : Jogeshwari\n    Average cost for two : 600\n    Rating : 3.3\n\n10. Restaurant : YumYumSouth\n    Locality : Chandivali\n    Average cost for two : 600\n    Rating : 3.2\n\n"}
    - utter_ask_for_sending_mail
* affirm
    - utter_ask_for_mail_id
* send_mail{"mail_id": "a@a.com"}
    - slot{"mail_id": "a@a.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
* restaurant_search{"location": "delhi", "cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_id": "Delhi NCR,28.625789,77.210276"}
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* check_budget
    - action_check_budget
    - slot{"budget": "0,100000"}
* check_budget{"budget": "around 400"}
    - slot{"budget": "around 400"}
    - action_check_budget
    - slot{"budget": "0,400"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving north indian in Delhi NCR\n\n1. Restaurant : Shree Gopal Ji Chole Bhature\n    Locality : Rohini\n    Average cost for two : 200\n    Rating : 4.3\n\n2. Restaurant : Moolchand Parantha\n    Locality : Lajpat Nagar 4\n    Average cost for two : 300\n    Rating : 4.2\n\n3. Restaurant : Sita Ram Diwan Chand\n    Locality : Paharganj\n    Average cost for two : 200\n    Rating : 4.2\n\n4. Restaurant : Baljeet's Amritsari Koolcha\n    Locality : Paschim Vihar\n    Average cost for two : 300\n    Rating : 4.2\n\n5. Restaurant : Pandit Ji Parantha Hut\n    Locality : Ashok Vihar Phase 2\n    Average cost for two : 200\n    Rating : 4.1\n\n6. Restaurant : Aslam Chicken\n    Locality : Jama Masjid\n    Average cost for two : 300\n    Rating : 4.1\n\n7. Restaurant : Baljeet's Amritsari Koolcha\n    Locality : Paschim Vihar\n    Average cost for two : 300\n    Rating : 4.1\n\n8. Restaurant : Janta Eating House\n    Locality : Shahdara\n    Average cost for two : 150\n    Rating : 4.1\n\n9. Restaurant : New Punjabi Khana\n    Locality : Nehru Place\n    Average cost for two : 300\n    Rating : 4.1\n\n10. Restaurant : Pandit Ji Paranthe Wale\n    Locality : Ashok Vihar Phase 2\n    Average cost for two : 200\n    Rating : 4.0\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - export

## Generated Story -8368520740555948045
* out_of_scope
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location
    - action_check_location
    - slot{"location": null}
* check_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_check_cuisine
    - slot{"cuisine": null}
* check_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "300-700 range"}
    - slot{"budget": "300-700 range"}
    - action_check_budget
    - slot{"budget": "300,700"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Mumbai\n\n1. Restaurant : Peco Peco\n    Locality : Powai\n    Average cost for two : 700\n    Rating : 4.6\n\n2. Restaurant : The Golden Wok\n    Locality : Chembur\n    Average cost for two : 600\n    Rating : 4.3\n\n3. Restaurant : Dimsum W\u016b\n    Locality : Goregaon East\n    Average cost for two : 650\n    Rating : 4.2\n\n4. Restaurant : Mystery Box\n    Locality : Malad West\n    Average cost for two : 550\n    Rating : 4.2\n\n5. Restaurant : Mystery Box\n    Locality : Mira Road\n    Average cost for two : 700\n    Rating : 4.1\n\n6. Restaurant : Pincuk\n    Locality : Airoli\n    Average cost for two : 700\n    Rating : 4.1\n\n7. Restaurant : Dimsum (Momo) Express\n    Locality : Hill Road, Bandra West\n    Average cost for two : 500\n    Rating : 4.1\n\n8. Restaurant : Kampa\n    Locality : Mulund East\n    Average cost for two : 700\n    Rating : 4.0\n\n9. Restaurant : Ming Yang\n    Locality : Kalyan\n    Average cost for two : 500\n    Rating : 4.0\n\n10. Restaurant : Zoodles - Oriental Street Wok\n    Locality : Oberoi Mall, Goregaon East\n    Average cost for two : 600\n    Rating : 4.0\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location_id": "Kolkata,22.572646,88.363895"}
    - utter_ask_cuisine
* check_cuisine
    - action_check_cuisine
    - slot{"cuisine": null}
* check_location
    - action_check_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* check_budget{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
    - action_check_budget
    - slot{"budget": "300,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving american in Kolkata\n\n1. Restaurant : Echoes Kolkata\n    Locality : Topsia\n    Average cost for two : 1300\n    Rating : 4.8\n\n2. Restaurant : Pa Pa Ya\n    Locality : Park Street Area\n    Average cost for two : 2000\n    Rating : 4.7\n\n3. Restaurant : Chili's Grill & Bar\n    Locality : South City Mall, Prince Anwar Shah Road\n    Average cost for two : 1200\n    Rating : 4.7\n\n4. Restaurant : Some Like It Hot\n    Locality : Dhakuria\n    Average cost for two : 600\n    Rating : 4.7\n\n5. Restaurant : Barbeque Nation\n    Locality : RDB Boulevard, Sector 5\n    Average cost for two : 1800\n    Rating : 4.7\n\n6. Restaurant : Fly Kouzina\n    Locality : Sector 1, Salt Lake\n    Average cost for two : 1100\n    Rating : 4.6\n\n7. Restaurant : Chili's Grill & Bar\n    Locality : Acropolis Mall, Kasba\n    Average cost for two : 1200\n    Rating : 4.6\n\n8. Restaurant : Traffic Gastropub\n    Locality : City Centre 2 Mall, Chinar Park\n    Average cost for two : 2800\n    Rating : 4.6\n\n9. Restaurant : Barbeque Nation\n    Locality : Park Street Area\n    Average cost for two : 1800\n    Rating : 4.6\n\n10. Restaurant : Chili's Grill & Bar\n    Locality : Quest Mall, Ballygunge\n    Average cost for two : 1200\n    Rating : 4.6\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - export

## Generated Story 22534074676600563
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location_id": "Chandigarh,30.737793,76.77515"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "< 300"}
    - slot{"budget": "< 300"}
    - action_check_budget
    - slot{"budget": "0,300"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Chandigarh\n\n1. Restaurant : Kathmandu Chinese Fast Food\n    Locality : Sector 15\n    Average cost for two : 300\n    Rating : 4.0\n\n2. Restaurant : Miso Hungry\n    Locality : Sector 35\n    Average cost for two : 300\n    Rating : 3.8\n\n3. Restaurant : Jalandhar Sweets\n    Locality : Sector 23\n    Average cost for two : 250\n    Rating : 3.8\n\n4. Restaurant : Hoshiarpurian Di Hatti Sweets\n    Locality : Phase 5\n    Average cost for two : 300\n    Rating : 3.8\n\n5. Restaurant : Shammi Chat & Sweets\n    Locality : Sector 10\n    Average cost for two : 300\n    Rating : 3.7\n\n6. Restaurant : Crazy Dumplings\n    Locality : Elante Mall, Chandigarh Industrial Area\n    Average cost for two : 300\n    Rating : 3.5\n\n7. Restaurant : Rohit Chinese Fast Food\n    Locality : Sector 15\n    Average cost for two : 300\n    Rating : 3.5\n\n8. Restaurant : Meri Virasat\n    Locality : Kharar Road\n    Average cost for two : 200\n    Rating : 3.1\n\n9. Restaurant : Meals Of China\n    Locality : Kharar Road\n    Average cost for two : 300\n    Rating : 3.0\n\n10. Restaurant : Tawa Kathi Roll\n    Locality : Kharar Road\n    Average cost for two : 200\n    Rating : 2.8\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - export

## Generated Story 5159924318771711017
* greet
    - utter_greet
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_check_location
    - slot{"location_id": "Cuttack,20.46252,85.882989"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* check_budget{"budget": "> 50000"}
    - slot{"budget": "> 50000"}
    - action_check_budget
    - slot{"budget": "50000,100000"}
    - action_restaurant
    - reset_slots
    - utter_need_anything_else
* restaurant_search{"location": "mumbai", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - action_check_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* check_budget{"budget": "> 500000"}
    - slot{"budget": "> 500000"}
    - action_check_budget
    - slot{"budget": "500000,100000"}
    - action_restaurant
    - reset_slots
    - utter_need_anything_else
* restaurant_search{"location": "mumbai", "cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "<500"}
    - slot{"budget": "<500"}
    - action_check_budget
    - slot{"budget": "0,500"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving mexican in Mumbai\n\n1. Restaurant : Prithvi Cafe\n    Locality : Juhu\n    Average cost for two : 400\n    Rating : 4.4\n\n2. Restaurant : Whacko Taco\n    Locality : Versova, Andheri West\n    Average cost for two : 400\n    Rating : 4.2\n\n3. Restaurant : Food Adda\n    Locality : Borivali West\n    Average cost for two : 400\n    Rating : 4.1\n\n4. Restaurant : Say Cheese\n    Locality : Charni Road\n    Average cost for two : 350\n    Rating : 4.1\n\n5. Restaurant : Las Tapas\n    Locality : Vile Parle East\n    Average cost for two : 400\n    Rating : 3.7\n\n6. Restaurant : Yaanfoods\n    Locality : Kalyan\n    Average cost for two : 400\n    Rating : 3.4\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
    - export

## Generated Story -540760606840224176
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* check_location{"location": "kurnool"}
    - slot{"location": "kurnool"}
    - action_check_location
    - slot{"location_id": "Kurnool,15.8281257,78.0372792"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "not more than 500"}
    - slot{"budget": "not more than 500"}
    - action_check_budget
    - slot{"budget": "0,500"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Kurnool\n\n1. Restaurant : DVR Restaurant\n    Locality : Kurnool Locality\n    Average cost for two : 500\n    Rating : 4.2\n\n2. Restaurant : Hotel Hindustan\n    Locality : Kurnool Locality\n    Average cost for two : 350\n    Rating : 4.2\n\n3. Restaurant : Madhu Family Restaurant\n    Locality : Kurnool Locality\n    Average cost for two : 350\n    Rating : 4.2\n\n4. Restaurant : Ruchi Restaurant\n    Locality : Kurnool Locality\n    Average cost for two : 300\n    Rating : 4.1\n\n5. Restaurant : Snackup\n    Locality : Kurnool Locality\n    Average cost for two : 250\n    Rating : 4.1\n\n6. Restaurant : Samrat Restaurant\n    Locality : Kurnool Locality\n    Average cost for two : 450\n    Rating : 4.0\n\n7. Restaurant : Chinthakaya Restaurant\n    Locality : Kurnool Locality\n    Average cost for two : 400\n    Rating : 4.0\n\n8. Restaurant : Biryani Hut\n    Locality : Kurnool Locality\n    Average cost for two : 400\n    Rating : 4.0\n\n9. Restaurant : Lavish Lounge\n    Locality : Kurnool Locality\n    Average cost for two : 250\n    Rating : 3.9\n\n10. Restaurant : Mourya inn Garden restaurant\n    Locality : Kurnool Locality\n    Average cost for two : 300\n    Rating : 3.9\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "xyz@gmail.com"}
    - slot{"mail_id": "xyz@gmail.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
* deny
    - utter_goodbye
    - export

## Generated Story -9045823990041100415
* greet
    - utter_greet
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_location
    - slot{"location_id": "Tirupati,13.628814,79.419122"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* check_budget{"budget": "around 500"}
    - slot{"budget": "around 500"}
    - action_check_budget
    - slot{"budget": "0,500"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving north indian in Tirupati\n\n1. Restaurant : The AFC\n    Locality : Tirumala\n    Average cost for two : 400\n    Rating : 4.1\n\n2. Restaurant : New Southern Spice\n    Locality : Tirumala\n    Average cost for two : 200\n    Rating : 4.1\n\n3. Restaurant : Lasa Multi Cuisine Restaurant\n    Locality : Srinivasa Nagar\n    Average cost for two : 300\n    Rating : 4.1\n\n4. Restaurant : Sushma Southern Spice\n    Locality : Tirumala\n    Average cost for two : 200\n    Rating : 4.1\n\n5. Restaurant : Spicy Bites\n    Locality : Tirumala\n    Average cost for two : 450\n    Rating : 4.1\n\n6. Restaurant : Kwality Spicy\n    Locality : Tirumala\n    Average cost for two : 200\n    Rating : 4.1\n\n7. Restaurant : Spicy Paradise\n    Locality : Tirumala\n    Average cost for two : 400\n    Rating : 4.1\n\n8. Restaurant : Lasa Food Court\n    Locality : Tirumala\n    Average cost for two : 400\n    Rating : 4.1\n\n9. Restaurant : Hotel Manasa Veg & Non Veg Restaurant\n    Locality : Tirumala\n    Average cost for two : 200\n    Rating : 4.0\n\n10. Restaurant : Godavari Ruchulu\n    Locality : Tirumala\n    Average cost for two : 400\n    Rating : 4.0\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
* affirm
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "tirupathi"}
    - slot{"location": "tirupathi"}
    - action_check_location
    - slot{"location_id": "Tirupati,13.628814,79.419122"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "500-1000"}
    - slot{"budget": "500-1000"}
    - action_check_budget
    - slot{"budget": "500,1000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving chinese in Tirupati\n\n1. Restaurant : Table 9\n    Locality : Tirumala\n    Average cost for two : 600\n    Rating : 4.1\n\n2. Restaurant : Carrots Restaurant\n    Locality : Tirumala\n    Average cost for two : 600\n    Rating : 4.1\n\n3. Restaurant : Park Lane Restaurant\n    Locality : Tirumala\n    Average cost for two : 600\n    Rating : 4.0\n\n4. Restaurant : Deforest Theme Restaurant\n    Locality : Tirumala\n    Average cost for two : 600\n    Rating : 3.9\n\n5. Restaurant : Mayuri Multicuisine Restaurant\n    Locality : Tirumala\n    Average cost for two : 500\n    Rating : 3.8\n\n6. Restaurant : Hotel Bliss\n    Locality : Korramenugunta\n    Average cost for two : 600\n    Rating : 3.8\n\n7. Restaurant : Amogha Restaurant\n    Locality : Tirumala\n    Average cost for two : 500\n    Rating : 3.8\n\n8. Restaurant : Brown Multicuisine Restaurant\n    Locality : Tirumala\n    Average cost for two : 600\n    Rating : 3.8\n\n9. Restaurant : Udayees Hotel BVN Grand\n    Locality : Tirumala\n    Average cost for two : 500\n    Rating : 3.6\n\n10. Restaurant : Gufha-Hotel Pai Viceroy\n    Locality : Tirumala\n    Average cost for two : 700\n    Rating : 3.6\n\n"}
    - utter_ask_for_sending_mail
* affirm
    - utter_ask_for_mail_id
* send_mail{"mail_id": "nageshgupta008@gmail.com"}
    - slot{"mail_id": "nageshgupta008@gmail.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
* deny
    - utter_goodbye
    - export

## Generated Story 6547166258307393017
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* check_budget{"budget": "more than 5000000"}
    - slot{"budget": "more than 5000000"}
    - action_check_budget
    - slot{"budget": "5000000,100000"}
    - action_restaurant
    - reset_slots
    - utter_need_anything_else
* restaurant_search{"cuisine": "mexican", "location": "mumbai", "budget": "costing 200 to 400"}
    - slot{"budget": "costing 200 to 400"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - action_check_budget
    - slot{"budget": "200,400"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving mexican in Mumbai\n\n1. Restaurant : Prithvi Cafe\n    Locality : Juhu\n    Average cost for two : 400\n    Rating : 4.4\n\n2. Restaurant : Whacko Taco\n    Locality : Versova, Andheri West\n    Average cost for two : 400\n    Rating : 4.2\n\n3. Restaurant : Food Adda\n    Locality : Borivali West\n    Average cost for two : 400\n    Rating : 4.1\n\n4. Restaurant : Say Cheese\n    Locality : Charni Road\n    Average cost for two : 350\n    Rating : 4.1\n\n5. Restaurant : Las Tapas\n    Locality : Vile Parle East\n    Average cost for two : 400\n    Rating : 3.7\n\n6. Restaurant : Yaanfoods\n    Locality : Kalyan\n    Average cost for two : 400\n    Rating : 3.4\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "xyz@gmail.com"}
    - slot{"mail_id": "xyz@gmail.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
    - export

## Generated Story 1014930169303790260
* restaurant_search{"cuisine": "mexican", "location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location_id": "Kolkata,22.572646,88.363895"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "more than 500000"}
    - slot{"budget": "more than 500000"}
    - action_check_budget
    - slot{"budget": "500000,100000"}
    - action_restaurant
    - reset_slots
    - utter_need_anything_else
* restaurant_search{"cuisine": "north indian", "location": "mumbai", "budget": "< 4000"}
    - slot{"budget": "< 4000"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - action_check_budget
    - slot{"budget": "0,4000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving north indian in Mumbai\n\n1. Restaurant : Delhi Highway\n    Locality : Times Square, Marol\n    Average cost for two : 1200\n    Rating : 4.6\n\n2. Restaurant : Taftoon Bar & Kitchen\n    Locality : Bandra Kurla Complex\n    Average cost for two : 2500\n    Rating : 4.6\n\n3. Restaurant : Rajdhani\n    Locality : R City Mall, Ghatkopar West\n    Average cost for two : 1000\n    Rating : 4.5\n\n4. Restaurant : Oye Kake\n    Locality : Fort\n    Average cost for two : 800\n    Rating : 4.5\n\n5. Restaurant : Oye Kake\n    Locality : Kamala Mills Compound\n    Average cost for two : 800\n    Rating : 4.4\n\n6. Restaurant : Butter Chicken Factory\n    Locality : Andheri Lokhandwala, Andheri West\n    Average cost for two : 800\n    Rating : 4.4\n\n7. Restaurant : Kangan - The Westin Mumbai Garden City\n    Locality : The Westin Mumbai Garden City, Goregaon East\n    Average cost for two : 3000\n    Rating : 4.4\n\n8. Restaurant : The Caravan Menu\n    Locality : Panch Pakhadi, Thane West\n    Average cost for two : 1600\n    Rating : 4.4\n\n9. Restaurant : Rajdhani\n    Locality : Phoenix Marketcity, Kurla\n    Average cost for two : 1000\n    Rating : 4.4\n\n10. Restaurant : India Bistro\n    Locality : Upvan, Thane West\n    Average cost for two : 1900\n    Rating : 4.4\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "aniket@g.com"}
    - slot{"mail_id": "aniket@g.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
    - export

## Generated Story 1014930169303790260
* restaurant_search{"cuisine": "mexican", "location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location_id": "Kolkata,22.572646,88.363895"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "more than 500000"}
    - slot{"budget": "more than 500000"}
    - action_check_budget
    - slot{"budget": "500000,100000"}
    - action_restaurant
    - reset_slots
    - utter_need_anything_else
* restaurant_search{"cuisine": "north indian", "location": "mumbai", "budget": "< 4000"}
    - slot{"budget": "< 4000"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - action_check_budget
    - slot{"budget": "0,4000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving north indian in Mumbai\n\n1. Restaurant : Delhi Highway\n    Locality : Times Square, Marol\n    Average cost for two : 1200\n    Rating : 4.6\n\n2. Restaurant : Taftoon Bar & Kitchen\n    Locality : Bandra Kurla Complex\n    Average cost for two : 2500\n    Rating : 4.6\n\n3. Restaurant : Rajdhani\n    Locality : R City Mall, Ghatkopar West\n    Average cost for two : 1000\n    Rating : 4.5\n\n4. Restaurant : Oye Kake\n    Locality : Fort\n    Average cost for two : 800\n    Rating : 4.5\n\n5. Restaurant : Oye Kake\n    Locality : Kamala Mills Compound\n    Average cost for two : 800\n    Rating : 4.4\n\n6. Restaurant : Butter Chicken Factory\n    Locality : Andheri Lokhandwala, Andheri West\n    Average cost for two : 800\n    Rating : 4.4\n\n7. Restaurant : Kangan - The Westin Mumbai Garden City\n    Locality : The Westin Mumbai Garden City, Goregaon East\n    Average cost for two : 3000\n    Rating : 4.4\n\n8. Restaurant : The Caravan Menu\n    Locality : Panch Pakhadi, Thane West\n    Average cost for two : 1600\n    Rating : 4.4\n\n9. Restaurant : Rajdhani\n    Locality : Phoenix Marketcity, Kurla\n    Average cost for two : 1000\n    Rating : 4.4\n\n10. Restaurant : India Bistro\n    Locality : Upvan, Thane West\n    Average cost for two : 1900\n    Rating : 4.4\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "aniket@g.com"}
    - slot{"mail_id": "aniket@g.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
    - export

## Generated Story -3577388606737267372
* out_of_scope
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* check_budget{"budget": "< 5000"}
    - slot{"budget": "< 5000"}
    - action_check_budget
    - slot{"budget": "0,5000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving mexican in Mumbai\n\n1. Restaurant : Palladium Social\n    Locality : Palladium Mall, Lower Parel\n    Average cost for two : 1400\n    Rating : 4.9\n\n2. Restaurant : Hitchki\n    Locality : First International Financial Centre, Bandra Kurla Complex\n    Average cost for two : 1600\n    Rating : 4.8\n\n3. Restaurant : Bayroute\n    Locality : Juhu\n    Average cost for two : 3000\n    Rating : 4.8\n\n4. Restaurant : Hitchki\n    Locality : Powai\n    Average cost for two : 1600\n    Rating : 4.8\n\n5. Restaurant : Colaba Social\n    Locality : Colaba\n    Average cost for two : 1400\n    Rating : 4.8\n\n6. Restaurant : Craftbar\n    Locality : Bandra East\n    Average cost for two : 2000\n    Rating : 4.7\n\n7. Restaurant : 145 Kala Ghoda\n    Locality : Fort\n    Average cost for two : 1500\n    Rating : 4.7\n\n8. Restaurant : Hitchki\n    Locality : Viviana Mall, Majiwada, Thane West\n    Average cost for two : 1600\n    Rating : 4.7\n\n9. Restaurant : Lord Of The Drinks\n    Locality : Veera Desai Area\n    Average cost for two : 2100\n    Rating : 4.7\n\n10. Restaurant : London Taxi\n    Locality : Kamala Mills Compound\n    Average cost for two : 1800\n    Rating : 4.7\n\n"}
    - utter_ask_for_sending_mail
* deny
    - action_goodbye
    - reset_slots
    - utter_need_anything_else
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "vashi"}
    - slot{"location": "vashi"}
    - action_check_location
    - slot{"location": null}
* restaurant_search
    - action_check_location
    - slot{"location": null}
* check_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_id": "Delhi NCR,28.625789,77.210276"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* check_budget{"budget": "> 300"}
    - slot{"budget": "> 300"}
    - action_check_budget
    - slot{"budget": "300,100000"}
    - action_restaurant
    - slot{"mail_text": "Hi, \n\nPlease find the list of restaurants serving american in Delhi NCR\n\n1. Restaurant : Plum By Bent Chair\n    Locality : Aerocity\n    Average cost for two : 3000\n    Rating : 4.9\n\n2. Restaurant : Feel Alive\n    Locality : Sector 29\n    Average cost for two : 2000\n    Rating : 4.8\n\n3. Restaurant : AB's - Absolute Barbecues\n    Locality : MGF Metropolis Mall, MG Road\n    Average cost for two : 1600\n    Rating : 4.7\n\n4. Restaurant : Gastronomica Kitchen & Bar\n    Locality : M Block Market, Greater Kailash 1 (GK1)\n    Average cost for two : 2000\n    Rating : 4.7\n\n5. Restaurant : Chili's Grill & Bar\n    Locality : DLF Mall of India, Sector 18,  Noida\n    Average cost for two : 1200\n    Rating : 4.7\n\n6. Restaurant : Hauz Khas Social\n    Locality : Hauz Khas Village\n    Average cost for two : 1300\n    Rating : 4.7\n\n7. Restaurant : C.I.A. Call it Asiian\n    Locality : Greater Kailash 2 (GK2)\n    Average cost for two : 1200\n    Rating : 4.7\n\n8. Restaurant : Out Of The Box\n    Locality : Khan Market\n    Average cost for two : 1550\n    Rating : 4.7\n\n9. Restaurant : Pa Pa Ya\n    Locality : Select Citywalk Mall, Saket\n    Average cost for two : 2500\n    Rating : 4.6\n\n10. Restaurant : Cafe Wink\n    Locality : Anand Vihar\n    Average cost for two : 800\n    Rating : 4.6\n\n"}
    - utter_ask_for_sending_mail
* send_mail{"mail_id": "a@a.com"}
    - slot{"mail_id": "a@a.com"}
    - action_send_mail
    - reset_slots
    - utter_need_anything_else
    - export

## Generated Story 5979772650911363837
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* check_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_id": "Mumbai,19.017656,72.856178"}
    - utter_ask_cuisine
* check_cuisine{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* check_budget{"budget": "> 50000"}
    - slot{"budget": "> 50000"}
    - action_check_budget
    - slot{"budget": "50000,100000"}
    - action_restaurant
    - reset_slots
    - export
