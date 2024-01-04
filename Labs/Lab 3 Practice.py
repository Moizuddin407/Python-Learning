# Lab 3
# Q1
def q1():    
    my_list = ["apple", "cherry", "orange", "kiwi", "melon", "mango"]

    my_list.remove("cherry")
    my_list.remove("melon")

    # Inserting at second last index(-1 part)
    my_list.insert(-1,"banana")

    # Insert "banana" at the last index(Directly enter list length)
    my_list.insert(len(my_list), "banana")


def q2(lista):
    while len(lista) != 0:
        lista.pop()
    print(lista)    

listx=[1,2,3,4,5]

import random
def q3(list_size):
    '''Takes list size and returns min and max'''
    random_list = [random.randint(1, 100) for _ in range(list_size)]

    maxnum=max(random_list)
    minnum=min(random_list)

    return maxnum,minnum
minno,maxno=q3(20)

def q4():
    Tuple = ("john","mark",12,"14","orange",4.5)
#     lista=list(Tuple)
#     print(lista)
#     lista.append(6.5)
#     Tupleb=tuple(lista)
    Tuple=Tuple+(6.5,)
    listtypes=[]
    
    count_float=0
    count_int=0
    count_str=0
    for element in Tuple:
        if isinstance(element, int):
            count_int += 1
        elif isinstance(element, str):
            count_str += 1
        elif isinstance(element, float):
            count_float += 1
    print(f"float {count_float},string {count_str},int {count_int}")


def q5():    
    import random

def dictionary_operations():
    my_dict = {"brand": "Samsung", "OS type": "Oreo", "color": "black", "camera": "42 megapixels", "year": 2012}
    print("Original Dictionary:", my_dict)

    my_dict["sizes"] = [random.randint(10, 50) for _ in range(5)]
    print("Dictionary after adding 'sizes':", my_dict)

    if "year" in my_dict:
        del my_dict["year"]
    print("Dictionary after deleting 'year':", my_dict)

    order = ["brand", "color", "camera", "OS type", "sizes"]

    print("\nShowing Dictionary in the Following Order:")
    for key in order:
        if key in my_dict:
            print(f"{key.capitalize()}: {my_dict[key]}")


def q7():
    lista = [5, 6, 7, 23, 12, 3, 3, 4, 5, 12, 34]
    lista.sort(reverse=True)
    print(lista)
