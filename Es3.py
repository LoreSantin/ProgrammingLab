
class CSVFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        my_file = open(self.name,'r')
        my_list = []
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            my_list.append((elements))
        return my_list

csvfile = CSVFile('shampoo_sales.csv')
print(csvfile.get_data())