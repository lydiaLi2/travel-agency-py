

# Import Random
import random

# Lists
destinations = ["Vienna","Bali","Las Vegas","Macao"]

flight_prices = [997.93,849.93,338.37,734.34]

hotel_prices = [143.84,235.35,173.54,199.99]

highlights = ["classical music","beaches and surfing","history and architecture","gambling","musicals"]


# Functions
#Welcome
def welcome():
  print("Welcome ! I am your friendly travel agent bot . I will ask you some questions, and make a recommendation based on your answer. If you are interested , I will provide you with a one - time password to create a user account on our website.")

#Ask user information
def ask_userinfo():
    
  name =input("What is your name? ")
  print("Hello,",name,"!")
  print()

  age = ask_number("What is your age? ")
  if age > 64:
    print("Great! We offer a senior discount.\nFor every year over 64, you get 1% off.")
    print()
  else:
    print()

  nights= ask_number("How many nights are you planning to stay? ")
  print()

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
def ask_userpref(list2):
  list1 = []
  for i in list2:
    print("Do you like",i,"?")
    pre = ask_yesno("Please enter y/n: ")
    list1.append(pre)
  
  return list1



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
def totalcost(destination1,nights,age):
  n = destinations.index(destination1)
  flight_c = float(flight_prices[n])
  hotel_c = float(hotel_prices[n])
  total=(flight_c+(hotel_c * nights))-(flight_c+(hotel_c * nights))*(discount_percentage(age)*0.01)
  return total



#Suggest Trip
def suggest_trip(list1):
  count_v = 0
  count_b = 0
  count_l = 0
  count_m = 0
  i = 0
  list2 = []

  if list1[0] == True:
    print("** Trace : Vienna matches preference for classical music")
    count_v += 1
  if list1[2] == True:
    print("** Trace : Vienna matches preference for history and architecture")
    count_v += 1

  print("** Trace : matches for destination Vienna :",count_v)
  print()
  

  if list1[1] == True:
    print("** Trace : Bali matches preference for classical music")
    count_b += 1
  if list1[3] == True:
    print("** Trace : Bali matches preference for beaches and surfing")
    count_b += 1
  print("** Trace : matches for destination Bali :",count_b)
  print()


  if list1[3] == True:
    print("** Trace : Las Vegas matches preference for gambling")
    count_l += 1
  if list1[4] == True:
    print("** Trace : Las Vegas matches preference for musicals")
    count_l += 1
  print("** Trace : matches for destination Las Vegas :",count_l)
  print()


  if list1[2] == True:
    print("** Trace : Macao matches preference for history and architecture")
    count_m += 1
  if list1[3] == True:
    print("** Trace : Macao matches preference for gambling")
    count_m += 1
  print("** Trace : matches for destination Macao :",count_m)
  print()

  list2 = [count_v,count_b,count_l,count_m]
  m = max(list2)
  max_v = 0
  max_index = 0
  

  for i in range(len(list2)):

    if list2[i] == m:
      max_v = list2[i]
      max_index = i
      break
    
    

  
  if max_v == 0:
    print("I'm sorry, we don It have any trips to offer at this point.")
    return 0
  if max_v != 0:
    answer = destinations[max_index]
    return answer

  
      


#Trip details
def details(destination1,nights,age):
  discount=discount_percentage(age)
  n = destinations.index(destination1)
  flight_c = float(flight_prices[n])
  hotel_c = float(hotel_prices[n])
  total = totalcost(destination1,nights,age)
        
  print("How about a trip to", destination1,"?")
  print("Flight:", flight_c,"$")
  print("Hotel:", hotel_c,"$/night")
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






# Travel Agnet Stage 2 

welcome()

info=ask_userinfo()
age=info["age"]
nights=info['nights']
name=info['name']


list_pre = ask_userpref(highlights)
print()

choice = suggest_trip(list_pre)
print(choice)
print()

if choice != 0:
  details(choice,nights,age)
  print()
  account()
  print()
  print("Goodbye")

if choice == 0:
  account()
  print()
  print("Goodbye")

