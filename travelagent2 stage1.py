#Authors: Alisha Jeon, Ji Li
#Date: Aug 7, 2020
#Purpose: Stage 1

import random

# Welcom function
def welcome():
    print("""Welcome! I am your friendly travel agent bot.
Based on your answers, I will provided a recommendation.
If you are interested, I will provide you
with a one-time password to create a user
account on our website.""")


#Ask user information
def ask_userinfo():
    
    name=input("What is your name?")
    print("Hello,", name,"!")

    age=ask_number("What is your age")

    nights=ask_number("How many nights are you planning to stay?")

    userinfo_dic = {"name":name, "age":age, "nights":nights}
    return userinfo_dic

#Ask_yesno
def ask_yesno(message):
    n=input(message)
    n=n.lower()
    if (n=="y"):
        return True
    else:
        return False

#Ask_userpref
def ask_userpref():
    m_answer=ask_yesno("Do you prefer classical music?")
    b_answer=ask_yesno("Do you prefer beaches and surfing?")
    pref_dic={"m_answer":m_answer, "b_answer":b_answer}
    return pref_dic

#Ask_number
def ask_number(message):
    n=int(input(message))
    return n

#Discount_percentage
def discount_percentage(age):
    if age>64:
        discount = float(age-64)
    else:
        discount = 0
    return discount

#Totalcost
def totalcost(flight,hotel,nights,age):
    total=(flight+(hotel*nights))-(flight+(hotel*nights))*(discount_percentage(age)*0.01)
    return total

    
#Suggest Trip
def suggest_trip(pref,flight_vienna,hotel_vienna,flight_bali,hotel_bali):

    if (pref["m_answer"]==True and pref["b_answer"]==False):
         total_cost=totalcost(flight_vienna,hotel_vienna,nights,age)
         destination="Vienna"
         
    elif (pref["m_answer"]==False and pref["b_answer"]==True):
        total_cost=totalcost(flight_bali,hotel_bali,nights,age)
        destination= "Bali"
        
    elif (pref["m_answer"]==True and pref["b_answer"]==True):
        total_cost_v=totalcost(flight_vienna,hotel_vienna,nights,age)
        total_cost_b=totalcost(flight_bali,hotel_bali,nights,age)
        if total_cost_v>total_cost_b:
            destination="Vienna"
        elif total_cost_b>total_cost_v:
            destination="Bali"
        else:
            destination="Bali"
    else:
        destination=None
    return destination
    

#Trip details
def details(deestination,flight,hotel,nights,age):
    discount=discount_percentage(age)
    if destination=="Vienna":
        total=totalcost(flight_vienna,hotel_vienna,nights,age)
        
    elif destination=="Bali":
        total=totalcost(flight_bali,hotel_bali,nights,age)
        
    print("How about a trip to", destination,"?")
    print("Flight:", flight,"$")
    print("Hotel:", hotel,"$/night")
    print("Discount:", discount,"%")
    print("Total for", nights,"(incl.discounts):{}$".format("%.2f"%total))

#Create account
def account():
    n=input("Are you interested, and want to create a user account?\nPlease answer y/n.")
    n=n.lower()
    if n=="y":
        p = age % 8
        password = name[-1] * p + name[0]
        e = random.randint(0,5)
        password = password + "!" * e
        print("Looking forward to working with you!")
        print("Your one-time password is:", password)
        print()
    else:
        print("Sorry to hear that. Please consider using our service again.")
        print()

###The Program###

#Display welcome message
welcome()

#Extracting values from a dictionary
info=ask_userinfo()
age=info["age"]
nights=info['nights']
name=info['name']

#Asking for preference using ask_pref function
pref=ask_userpref()

#Initialize 
flight_vienna=997.93
hotel_vienna=143.84
flight_bali = 849.93
hotel_bali=235.35

#Display the suggest_trip function
destination=suggest_trip(pref,flight_vienna,hotel_vienna,flight_bali,hotel_bali)
if destination == "Vienna":
    flight = flight_vienna
    hotel = hotel_vienna
elif destination == "Bali":
    flight = flight_bali
    hotel = hotel_bali
else:
    print("Sorry, we don't have any trips to offer at this point.")

#Run detail function only when there is suggested destination
if destination != None :
    details(destination,flight,hotel,nights,age)

#Run account function
account()
print("Goodbye.")  



