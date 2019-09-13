import requests
import time

# print the data array with only the IDs (with smaller length) from cat-fact
def print_array(array):
    id_array = [(value['_id']//10**25) for value in array]
    print(id_array)
    print()


def selection_sort(array):
    sorted_array = array
    for i in range(len(sorted_array)):
        index_min = i
        for j in range(i + 1, len(sorted_array)):
            if(sorted_array[j]['_id'] < sorted_array[index_min]['_id']):
                index_min = j
                
        if(index_min != i):
            aux = sorted_array[index_min]
            sorted_array[index_min] = sorted_array[i]
            sorted_array[i] = aux
            print_array(sorted_array)
            time.sleep(0.1)
    
    return sorted_array
            

def insertion_sort(array):
    sorted_array = array
    for i in range(1, len(sorted_array)):
        j = i
        while((j != 0) and sorted_array[j]['_id'] < sorted_array[j - 1]['_id']):
            aux = sorted_array[j]
            sorted_array[j] = sorted_array[j - 1]
            sorted_array[j - 1] = aux
            j -= 1
            print_array(sorted_array)
            time.sleep(0.1)

    return sorted_array


def bubble_sort(array):
    sorted_array = array
    for i in range(len(sorted_array)):
        for j in range(i + 1, len(sorted_array)):
            if(sorted_array[j]['_id'] < sorted_array[i]['_id']):
                aux = sorted_array[j]
                sorted_array[j] = sorted_array[i]
                sorted_array[i] = aux
                print_array(sorted_array)
                time.sleep(0.1)

    return sorted_array


def shell_sort(array):
    sorted_array = array
    height = len(sorted_array)//2
    while height > 0:
        for i in range(height, len(sorted_array)):
            aux = sorted_array[i]
            j = i
            while(j >= height and sorted_array[j - height]['_id'] > aux['_id']):
                sorted_array[j] = sorted_array[j - height]
                j = j - height

            sorted_array[j] = aux
            
        print_array(sorted_array)
        time.sleep(0.1)
        height = height//2

    return sorted_array


# executes http request to cat-fact api
URL = "https://cat-fact.herokuapp.com/facts"
print("Fazendo requisição para a API")
r = requests.get(url = URL)
print("Requisição feita com sucesso\n")
data = r.json()
facts_objects = data['all']

# converts hexadecimal to decimal
for fact in facts_objects:
    fact['_id'] = int(fact['_id'], 16)

which_algorithm = int(input("Qual algoritmo deseja testar?\n1- Selection Sort\n2- Insertion Sort\n3- Bubble Sort\n4- Shell Sort\n"))
if(which_algorithm == 1):
    print("Selection Sort")
    selection_sort_array = selection_sort(facts_objects)
elif(which_algorithm == 2):
    print("Insertion Sort")
    insertion_sort_array = insertion_sort(facts_objects)
elif(which_algorithm == 3):
    print("Bubble Sort")
    bubble_sort_array = bubble_sort(facts_objects)
elif(which_algorithm == 4):
    print("Shell Sort")
    shell_sort_array = shell_sort(facts_objects)
        