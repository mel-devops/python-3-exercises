from ValidationException import ValidationException
import csv

def validate_file(fileToValidate):
    with open(fileToValidate) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            if "." in row[1]:
                print(f"Invalid mileage: {row[1]}")


def ex1():
    try:
        validate_file("files/input.txt")
    except ValidationException as ve:
        print(ve)
        
ex1()
