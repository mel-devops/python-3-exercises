import csv

def find_total_visits():
    def weekTotal(inputFile):
        count = 0
        with open(inputFile) as csv_file:
            rows = csv.reader(csv_file, delimiter=',')
            for row in rows:
                #There is a space in front of value
                count += row.count(' 1')
        return count

    
    result1 = weekTotal(inputFile="files/week-1.csv")
    result2 = weekTotal(inputFile="files/week-2.csv")
    result3 = weekTotal(inputFile="files/week-3.csv")

    return result1+result2+result3

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()