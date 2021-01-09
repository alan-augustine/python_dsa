# as per solution hint, below is not an optimal solution
import sys
def change(amount_charged, amont_given):
    if amount_charged > amont_given:
        print("amont_given should be greather than or equal to amont_given")
        sys.exit(1)
    bills= (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
    current_bill = bills[0]
    change_details = {}
    next_bill_index = 1
    remaining = amont_given - amount_charged
    while remaining > 0:
        bill_count = remaining // current_bill
        if bill_count > 0:
            change_details[current_bill] = bill_count
            remaining = remaining % current_bill
        if remaining > 0:
            current_bill = bills[next_bill_index]
            next_bill_index += 1
        #print("diff={0}, n={1}, i={2}, current_bill={3}".format(remaining, bill_count, next_bill_index, current_bill))
    return change_details

charged = 2000
given= 4134
print("given - charged = {0} - {1} = {2}".format(given, charged, given-charged),
      "\nChange details: ", change(charged, given))

charged = 2000
given= 2000
print("given - charged = {0} - {1} = {2}".format(given, charged, given-charged),
      "\nChange details: ", change(charged, given))

charged = 3000
given= 5000
print("given - charged = {0} - {1} = {2}".format(given, charged, given-charged),
      "\nChange details: ", change(charged, given))
