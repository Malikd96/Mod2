#Task 1: Code Correction. You are provided with a Python script that is supposed to help in event planning, 
# but it has errors. Identify and fix them. 

#Buggy Code:

attendees = int(input("Enter number of attendees: ") )
if attendees > 100:
    venue = "large hall"  
else:
    venue = "conference room"
print(venue)
