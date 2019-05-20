def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    rate_of_adult=37550*no_of_adults
    rate_of_children=(37550/3)*no_of_children
    total=rate_of_adult+rate_of_children
    service_tax=(total*7)/100
    total_cost=service_tax+total
    total_ticket=(total_cost*10)/100
    total_ticket_cost=total_cost-total_ticket
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
