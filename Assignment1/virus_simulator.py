import random
import matplotlib.pyplot as plt
import numpy as np

# function to swap 8 random entries with another set of 8 entries :
def swap_entries(array):
    x_coordinates = []
    y_coordinates = []
    while len(x_coordinates) < 16:
        x = random.randrange(0,100)
        if x not in x_coordinates:
            x_coordinates.append(x)

    while len(y_coordinates) < 16:
        y = random.randrange(0,150)
        if y not in y_coordinates:
            y_coordinates.append(y)   

    for i in range(8):
        temp = array[x_coordinates[i],y_coordinates[i]] 
        array[x_coordinates[i],y_coordinates[i]] = array[x_coordinates[15-i],y_coordinates[15-i]]
        array[x_coordinates[15-i],y_coordinates[15-i]] = temp


# function to change the first neighbours of infected cell :
def change_1st_neighbours(array,i,j):
    x = [0,1]        
    first_neighbours = [(i+1,j-1),(i+1,j),(i+1,j+1),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j),(i-1,j+1)]
    accepted_neighbours = []
    for neighbour in first_neighbours:
        if neighbour[0]>=0 and neighbour[0]<=99 and neighbour[1]>=0 and neighbour[1]<=149:
            accepted_neighbours.append(neighbour)

    for neighbour in accepted_neighbours:
        if array[neighbour[0],neighbour[1]] == 0 :
            array[neighbour[0],neighbour[1]] += random.choices(x,weights=(75,25),k=1)[0]

# function to change the second neighbours of infected cell :
def change_2nd_neighbours(array,i,j):
    x = [0,1] 
    second_neighbours = [(i-2,j-2),(i-2,j-1),(i-2,j),(i-2,j+1),(i-2,j+2),(i-1,j-2),(i-1,j+2),(i,j-2),(i,j+2),(i+1,j-2),(i+1,j+2),(i+2,j-2),(i+2,j-1),(i+2,j),(i+2,j+1),(i+2,j+2)]
    accepted_neighbours = []
    for neighbour in second_neighbours:
        if neighbour[0]>=0 and neighbour[0]<=99 and neighbour[1]>=0 and neighbour[1]<=149:
            accepted_neighbours.append(neighbour)

    for neighbour in accepted_neighbours:
        if array[neighbour[0],neighbour[1]] == 0 :
            array[neighbour[0],neighbour[1]] += random.choices(x,weights=(92,8),k=1)[0]


virus_matrix = np.zeros((100,150), dtype = 'i')              # initialising the matrix
virus_matrix[50,75] = 1                                      # initially infected cell
num_of_ones_in_matrix= [1]                   
ones_added_in_each_iteration = [0]
virus_not_spread = True
position_of_virus = []
num_of_iterations = 0

while virus_not_spread:
    virus_not_spread = False
    swap_entries(virus_matrix)
    for i in range(100):
        for j in range(150):
            if virus_matrix[i,j] == 1:
                position_of_virus.append((i,j))
            else :
                virus_not_spread = True 

    for virus in position_of_virus:
        change_1st_neighbours(virus_matrix,virus[0],virus[1])
        change_2nd_neighbours(virus_matrix,virus[0],virus[1])

    num_of_ones_in_matrix.append(len(set(position_of_virus)))
    ones_added_in_each_iteration.append(num_of_ones_in_matrix[-1]-num_of_ones_in_matrix[-2])
    num_of_iterations += 1

#Plot 1 : Number of ones v/s number of iterations
x1 = []
for i in range(num_of_iterations+1):
    x1.append(i+1)   
y1 = num_of_ones_in_matrix
plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.xlabel('Number of iterations')
plt.ylabel('Number of ones in the matrix')

#Plot 2: Change in number of ones in each iteration vs Number of iterations
x2 = x1
y2 = ones_added_in_each_iteration
plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.xlabel('Number of iterations')
plt.ylabel('Change in number of ones in each iteration')
plt.show()
print("Peak value in Plot 2 : "+str(max(ones_added_in_each_iteration)))





