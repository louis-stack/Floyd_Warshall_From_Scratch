from pprint import pprint

def print_graph(city_data):
    # create an empty graph
    graph = {}

    # populate the graph
    for data in city_data:
        city1, city2, distance = data
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}
        graph[city1][city2] = int(distance)
        graph[city2][city1] = int(distance)
    print("\nInitial graph :\n")
    pprint(graph)


def Floyd_Warshall_shrt_paths(n, roads):
    # initialize dp and path arrays
    dp = [[float('inf') for j in range(n)] for i in range(n)]
    path = [[i for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n):
        for j in range(n):
            if roads[i][j] != float('inf'):
                dp[i][j] = roads[i][j]
                path[i][j] = j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    path[i][j] = path[i][k]
    return dp, path

# read data from city_1.txt file
city_data = []
with open("city_1.txt", "r") as file:
    for line in file:
        city_data.append(line.strip().split())

# create a dictionary to map city names to indices
city_map = {chr(i + ord('A')): i for i in range(26)}

# create the roads matrix
n = 26
roads = [[float('inf') for j in range(n)] for i in range(n)]
for data in city_data:
    i = city_map[data[0]]
    j = city_map[data[1]]
    distance = int(data[2])
    roads[i][j] = distance
    roads[j][i] = distance

city_choosen = 'F'

# call the function with the city_map and city_data
print_graph(city_data)

# call the Floyd_Warshall_shrt_paths function
dp, path = Floyd_Warshall_shrt_paths(n, roads)

"""
The variable "dp" is a 2-dimensional array that stores the optimal distances between all vertices (cities) of the graph. 
It is used to store the intermediate results of the Dijkstra algorithm. It is of type list of lists of numbers.

The "path" variable is also a 2-dimensional array that stores the optimal paths between all vertices (cities) of the graph. 
It is used to retrace the optimal paths once the algorithm is finished. It is of type list of lists of integers.
"""

# print the shortest path from each city to F
print("\nShortest Paths & Optimal values:\n")
for i in range(n):
    city = chr(i + ord('A'))
    if dp[i][city_map[city_choosen]] == float('inf'):
        print(f"City {city}: Not Reachable, Value : {dp[i][city_map[city_choosen]]}")
    else:
        Floyd_Warshall_shrt_paths = city
        j = i
        while j != city_map[city_choosen]:
            j = path[j][city_map[city_choosen]]
            Floyd_Warshall_shrt_paths += "->"
            Floyd_Warshall_shrt_paths += chr(j + ord('A'))
            
        print(f"City {city}: {Floyd_Warshall_shrt_paths}, Value : {dp[i][city_map[city_choosen]]}")





"""
                Work by 
                Louis FERRAND & Arnaud PARMENTIER
          
"""


        