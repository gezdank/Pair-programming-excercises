list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def listoverlap(list1, list2):
    return list(set(list1) & set(list2))
    
print(set(list1) & set(list2))

def main():
    return


if __name__ == '__main__':
    main()


