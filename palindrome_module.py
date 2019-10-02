def palindrome(str):
    lista =[]
    for ch in str:
        if ch != " ":
            lista.append(ch.lower())

    print(lista)
    return lista[::-1] == lista
    


def main():
    return


if __name__ == '__main__':
    main()