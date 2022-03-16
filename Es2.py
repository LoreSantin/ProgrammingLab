
def sum_list(the_list):
# Se la lista è vuota
    if not the_list:
        return None
    else:
        total = 0
        for element in the_list:
            total += element
    return total

def sum_csv(file_name):
    if not file_name:
        return None
    else:
        values = []
        my_file = open('shampoo_sales.csv','r')
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                date = elements[0]
                value = elements[1]
                values.append(float(value))
    my_file.close()
    return sum_list(values)

print(sum_csv('shampoo_sales.csv'))
            