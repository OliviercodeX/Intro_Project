

#fuction to create flights
flights = []
People = [[]]

#E: code(string), origin(string), destination(string), price(float), price(integer), column,column(integer), sold_count(int)
#S: a list with new elements
#R: only if the row is less than 50 and row 20
def create_flight(code, origin, destination, price, row, column, sold_count=0):
    seat_matrix = [[0]*row for i in range(column)]
    if row > 50 and column > 20:
        return "Has sobrepasado el limite maximo permitido row: 50, column:20"
    flights.append([code,origin,destination, price, seat_matrix,sold_count])
    return len(flights)-1

print(create_flight("M","A","B",0, 3,3, "x"))
print(create_flight("S","A","B",0, 3,3, "x"))
print(create_flight("D","A","B",0, 3,3, "x"))
print(create_flight("F","A","B",0, 3,3, "x"))

#E: a integer
#S: one list inside the main list of the program
def get_flight(index):
    return flights[index]

def book_flight(row,column,index):
    matrix = flights[index][4]  #to look the matrix inside the flight selected of index of flights
    for _ in range(len(matrix)):
        for _ in range(len(matrix[0])):

            
            

            if matrix[row][column] == 0:  #if the number keep going 0 get chance it by 1
                matrix[row][column] == 1
                
            else:
                return "El campo esta ocupado"
    flights[index][4] == matrix


    




def cancel_flight(row,column,index):
    matrix = flights[index][4]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[row][column] != 0:
                matrix[row][column] == 0
    flights[index][4] == matrix






