#Task 3: Catering Choices

#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: ") )
vegetarian = input("Do you want vegetarian food? (yes/no): ")

if attendees > 100:
    venue = "large hall"  
    equipment = "audio system and projector"
elif 50 <= attendees <= 100:
    venue = "medium conference room"
    equipment = "projector"
else:
    venue = "small conference room"
    equipment = "no additional equipment needed"

if vegetarian == "yes":
    caterer = "VegeDelight Caterers"
else:
    caterer = "Gourmet Meals Caterers"


    
print(venue, equipment, caterer)



