
# importing the required module
import matplotlib.pyplot as plt # plot graphs

# friction coefficient
def get_cf(road_type, road_condition):
    if(road_type == "concrete" and road_condition == "dry"):
        return 0.5
    elif(road_type == "concrete" and road_condition == "wet"):
        return 0.35
    elif(road_type == "ice" and road_condition == "dry"):
        return 0.15
    elif(road_type == "ice" and road_condition == "wet"):
        return 0.08
    elif(road_type == "water" and road_condition == "aquaplaning"):
        return 0.05
    elif(road_type == "gravel" and road_condition == "dry"):
        return 0.35
    elif(road_type == "concrete" and road_condition == "wet"):
        return 0.3


# calculate brake distance
def get_distance(vel = 0.0, fric_coeff = 0.0):
    d = (vel*vel) / (2 * 9.8 * fric_coeff)
    return d

#calculate brake time
def get_time(vel, d):
    t= vel/d
    return t


# create variables
vel = 0.0
g = 9.8
distance = 0.0
road_type = ""
road_condition = ""
fric_coeff = 0.0

# ask user for parameters
print("Enter initial velocity")
vel = float(input())
vel = vel * 1000 / 3600  # m/s
print("Enter road type")
road_type = input()
print("Enter road condition")
road_condition = input()

fric_coeff = get_cf(road_type, road_condition)

#output
d = get_distance(vel, fric_coeff)
print("The braking distance (m) is:", d)
t = get_time(vel,d)
print("The braking time in seconds:", t)

# function to plot a graph

# Define Data
x= [0,t]
data_1= [vel,0]
data_2= [0,d]

# Create Plot

fig, ax1 = plt.subplots() 
  
ax1.set_xlabel('X-Braking Time') 
ax1.set_ylabel('Y1-Initial velocity', color = 'black') 
plot_1 = ax1.plot( x,data_1, color = 'black') 
ax1.tick_params(axis ='y', labelcolor = 'black') 

# Adding Twin Axes

ax2 = ax1.twinx() 
  
ax2.set_ylabel('Y2-Braking distance', color = 'green') 
plot_2 = ax2.plot(x, data_2, color = 'green') 
ax2.tick_params(axis ='y', labelcolor = 'green') 


# giving a title to my graph
plt.title('Braking  time - Distance/ velocity-graph')
  
# function to show the plot
plt.show()