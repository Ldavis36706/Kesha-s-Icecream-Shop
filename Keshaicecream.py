#menu data
serving_choice = ("cone", "cup")
allowed_number_of_scoops = (1,2,3)
flavor = ["vanilla","strawberry","chocolate","cherry" ,"mint","peach","grape"]
individual_order = []
all_orders = []
order_taking_question = False
random_serving_choice_option = False
cone_or_cup = False
number_of_scoops_response = False

#Greeting
order_reply = input("Hello and welcome to Keshia's icecream shop! May I take your order please?").lower()
order_done = False
while (order_done == False and order_reply!="no"):
    
    individual_order = {}
    individual_order["flavors"] = []
    cone_or_cup = False
    scoops_choice = False
    number_of_scoops = 0
    flavor_choice = False
    order_done = True
    while(cone_or_cup == False and order_done == True):
        container_choice = input("Would you like a cup or a cone?")
        if(container_choice in serving_choice):
            individual_order["container"] = container_choice
            cone_or_cup = True
        else: 
            cone_or_cup = False
            
            
    while cone_or_cup==True and scoops_choice == False:
        number_of_scoops = input("How many scoops of icecream do you want?")
        if number_of_scoops.isnumeric() and int(number_of_scoops) in allowed_number_of_scoops:
            scoops_choice = True
        else:
            print("Please enter a valid input: 1, 2, or 3.")
            scoops_choice = False
             
        if cone_or_cup==True and number_of_scoops >= "2":
            print("Wow, you're really hungry!") 
            cone_or_cup = False
       
    while scoops_choice == True and flavor_choice == False:
        print("We have the following flavors:")
        for each_flavor in flavor:
            print(each_flavor)
            flavor_choice = True
            
    #while scoops_choice == True and random_serving_choice_option == False:
        for i in range(int(number_of_scoops)):
            random_flavor = input(f"Would you like me to randomly choose a flavor scoop{i+1}?").lower()
            if random_flavor == "yes":
                surprise_flavor = flavor.pop()
                individual_order["flavors"].append(surprise_flavor)
                print("Surprise, your random flavor is " + surprise_flavor.upper() + " !!!")
                flavor_choice = True
            else:
                flavors = input(f"What flavor icecream do you want for scoop{i+1}?")
                if flavors in flavor:
                    individual_order["flavors"].append(flavors)
                    flavor_choice = True
                else: 
                    print("We don't have that  flavor. Please try again.")
                    flavor_choice = False
        all_orders.append(individual_order)
    print(individual_order)
    print("Order: ", all_orders)
    
    more = input("Would you like to add another order? Please choose yes or no. ")
    if more == "no":
        order_done = True
        print("Here is your entire order ", all_orders)
        print("Thank you for visiting. Please come again!")
    else: 
        order_done = False
if order_reply != "no":
    all_orders.append(individual_order)