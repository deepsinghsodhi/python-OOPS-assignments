'''4) Write a  code to find the distance from Mumbai to major cities of India. Hint: Create an String list of 
major cities and integer list of distances. User  gives the city name and the same is searched  in the 
respective array and displays result.

city=[“Indore”,”Mumbai”,”Pune”]
dist=[1200,3500,7888];
e.g: 
Input: Enter city: Pune
Output:Distance is 7888

Input: Enter city: Indore
Output:Distance is 1200
'''
# ============================================================

city = ["Indore", "Mumbai", "Pune"]
dist = [1200, 3500, 7888]
print("Given Cities are: ", city)
print("Distance of Cities:", dist)

#zip will merge all the data of list(city & dict)together according 
# to their position and than convert them into a dictionary.
new_list = dict(zip(city, dist)) 
print(new_list)

city = input("Enter the City name: ")
if city in new_list:
    print(new_list.get(city))
else:
    print("Invalid city name")