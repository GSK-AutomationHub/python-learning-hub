# Write a python function which converts inches to cms

def inches_to_cms(inch):
    if inch == 0 or inch < 0:
        print("Please enter valid positive iteger")
    else:
        return 2.54 * inch
    

print("inches to centimeter conversion: ",inches_to_cms(7))