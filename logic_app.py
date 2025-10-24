

#fuction to create flights
flights = []

#E: code(string), origin(string), destination(string), price(float), price(integer), column,column(integer), sold_count(int)
def create_flight(code, origin, destination, price, row, column,elem, sold_count=0):
    seat_matrix = [[elem]*row for i in range(column)]
    
    flights.append([code,origin,destination, price, seat_matrix,sold_count])
    return len(flights)-1


