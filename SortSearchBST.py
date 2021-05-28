# Hepper, Stephen
# May 28, 2021
# Sorting and search algorithms, and a Binary Search Tree

"""
A Program that will search through a data array using a sequential and a binary search
to determine if the data array contains any values from a query array. A binary
search tree is constructed from Node objects whose values are those from the data array.
The program will return true or false for each value within the query array
as well as the run time for each search.
"""

from time import perf_counter         # perf_counter is used to measure elapsed run time


def open_file(file_name = "small_test_input.txt"):

    '''
    Function that parses an input text file to determine the length of the data and query arrays,
    as well as the values each array should contain, and then creates the arrays

    First line of input file contains two numbers:
        1st # (m): next m lines will each be a value in a list to search
        2nd # (n): final n lines are the values to search for in the first list.

    :param file_name: string
    :return data, query: lists containing ints
    '''

    with open(file_name, 'r') as f:

        header = f.readline()
        data_size = int(header.split(" ")[0])
        query_size = int(header.split(" ")[1])

        #print(header)
        #print(data_size)
        #print(query_size)

        j = 1
        data = []
        query = []

        for i in range((data_size + query_size)):
            line = f.readline()
            if i < data_size:
                data.append(int(line))
            else:
                query.append(int(line))

            i += 1

    print("data is: ",data)
    print("query is: ", query)

    return data,query


def merge_sort(data):
    '''
      Function that performs a merge sort on the parameter array and returns the sorted array

       :param data: list of ints
       :return data: sorted list of ints
      '''

    list_length = len(data)
    templist = []

    if list_length > 1:

        leftsize = int(list_length / 2)
        left_list = data[0:leftsize]
        right_list = data[leftsize:]

        left_sorted = merge_sort(left_list)
        right_sorted = merge_sort(right_list)

        leftlength = len(left_sorted)
        rightlength = len(right_sorted)

        left_counter = 0
        right_counter = 0

        while (left_counter < leftlength) or (right_counter < rightlength):

            if left_counter == leftlength:  # Special case where sorted left list is exhausted first

                templist.append(right_sorted[right_counter])
                right_counter += 1
                continue

            elif right_counter == rightlength:  # Special case where sorted right list is exhausted first

                templist.append(left_sorted[left_counter])
                left_counter += 1
                continue



            if left_sorted[left_counter] > right_sorted[right_counter]:
                templist.append(left_sorted[left_counter])
                left_counter += 1

            else:
                templist.append(right_sorted[right_counter])
                right_counter += 1




        return templist

    return data



def sequential_search(data, key):
    '''
    Function that performs a sequential search for the value "key" within the "data" list

     :param data: list of ints
     :param key: int
     :return isIn: boolean
     :return elapsed_time_ms: float
    '''


    start_time = perf_counter()
    isIn = False

    for i in range(len(data)):
        if data[i] == key:
            isIn = True
            stop_time = perf_counter()
            elapsed_time_ms = round((stop_time - start_time) * 1000, 3)
            return isIn, elapsed_time_ms

    stop_time = perf_counter()
    elapsed_time_ms = round((stop_time - start_time) * 1000, 3)
    return isIn, elapsed_time_ms



def binary_search(data, key):

    '''
    Function that performs a binary search for the value "key" within the "data" list

    :param data: list of ints
    :param key: int
    :return isIn: boolean
    :return elapsed_time_ms: float
    '''

    start_time = perf_counter()
    isIn = False
    start = 0
    end = len(data) - 1
    mid  = 0

    while start <= end:
        mid = int((start + end) / 2)
        if data[mid] < key:
            start = mid + 1
        elif data[mid] > key:
            end = mid - 1
        elif data[mid] == key:
            isIn = True
            stop_time = perf_counter()
            elapsed_time_ms = round((stop_time - start_time) * 1000, 3)
            return isIn, elapsed_time_ms

    stop_time = perf_counter()
    elapsed_time_ms = round((stop_time - start_time) * 1000, 3)
    return isIn, elapsed_time_ms


class Node:

    '''
    Class that instantiates a Node object with attributes data, leftchild, and rightchild.
    The left and right children of a node will either be a reference to another node or none/null
    '''

    def __init__(self, data):

        self.data = data
        self.leftchild = None
        self.rightchild = None

    '''
     Function that recursively inserts nodes into a tree. First determines where the new node should be 
     inserted by comparing data values between nodes. When a node is reached that has either a left or right
     child of None, depending on the value of the node to be inserted, a new node is created and assigned
     to that child

     :param data: list of ints
     :param self: Node object
     
     '''
    def insert_node(self, data):

        if self.data:
            if data < self.data:
                if self.leftchild is None:
                    self.leftchild = Node(data)
                else:
                    self.leftchild.insert_node(data)
            elif data > self.data:
                if self.rightchild is None:
                    self.rightchild = Node(data)
                else:
                    self.rightchild.insert_node(data)
        else:
            self.data = data

    def search_element(self, root, element):

        '''
         Function that searches a binary tree for a particular element

         :param root: Node object
         :param element: int value being searched for
         :return True or False: boolean determine whether the element is present in the tree
         :return Left/Rightchild: Node object representing a left or right subtree to be recursively
         searched
         '''

        if root is None:
            return False
        if root.data == element:
            return True
        if root.data < element:
            return self.search_element(root.rightchild, element)
        else:
            return self.search_element(root.leftchild, element)


class BST:
    '''
    A binary search tree class used to instantiate a BST with the values from the data array
    '''

    #NodeList = []

    def __init__(self, data):
        self.data = data

    '''
    Function that creates a binary search tree. Uses the first value in data array to create a 
    root node. All further values are nodes added relative to the root node via calls to insert_node

    :param self: Node object
   
    :return root: Root Node object in the tree. Used to make search calls.
    :return elapsed_time: float value used to determine run time
    '''

    def make_tree(self):

        start_time = perf_counter()

        root = Node(self.data[0])
        for num in self.data[1:]:
            root.insert_node(num)

        stop_time = perf_counter()
        elapsed_time = round((stop_time - start_time) * 1000, 3)
        return root, elapsed_time


def main():

    file_name = input("Enter the name of the input file: ")

    try:
        data, query = open_file(file_name)

        bst = BST(data)
        root, elapsed_tree_time = bst.make_tree()
        isIn = root.search_element(root, 89)

    except FileNotFoundError:
        print("Using small_test_input.txt instead")
        data, query = open_file("small_test_input.txt")

        bst = BST(data)

    root, elapsed_tree_time = bst.make_tree()
    print("Prep time: ", elapsed_tree_time, "ms")

    for key in query:

        start_time = perf_counter()
        isIn = root.search_element(root, key)
        stop_time = perf_counter()
        elapsed_search_time = round((stop_time - start_time) * 1000, 3)

        print(isIn, ":", elapsed_search_time, key)



if __name__ == '__main__':
    main()
