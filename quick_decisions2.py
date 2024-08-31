#Task 2: Venue Selection

#Based on the corrected code from Task 1, further enhance your code to recommend additional things like 
# "audio system" or "projector" based on the number of attendees.


attendees = int(input("Enter number of attendees: ") )
if attendees > 100:
    venue = "large hall"  
    equipment = "audio system and projector"
elif 50 <= attendees <= 100:
    venue = "medium conference room"
    equipment = "projector"
else:
    venue = "small conference room"
    equipment = "no additional equipment needed"
    
print(venue, equipment)

