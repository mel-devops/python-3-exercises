#Create  `build_car_list()` function.  
#reads from the [input.txt](files/input.txt) & from [car-ids.txt](files/car-ids.txt) 
#find car id with bad mileage data and remove.
#output list of cars to a single file

from pprint import pprint


def build_car_list():
    #join input.txt and car-ids.txt by their id
    with open('files/input.txt') as file1:
        txt1 = file1.read().splitlines()
        txt1.pop(0)
    with open('files/car-ids.txt') as file2:
        txt2 = file2.read().splitlines()
        #create a list of dictionaries
    result = []

    for t1, t2 in zip(txt1, txt2):
        try:
            id1, miles = t1.split(', ')
            id1, model = t2.split(', ')
            result.append({'id': int(id1), 'miles': int(miles), 'model': model})
        except ValueError:
            continue
    print(result)



def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
