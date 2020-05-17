def print_big(letter):
    l_dict = {"a" : ["00100","01010", "11111", "10001", "10001"], "b" : ["11100", "10010", "11100", "10010", "11100"]}
    l_list = l_dict[letter]
    print(l_list)
    for s in l_list :
        for bit in s :
            if bit == "0" :
                print(" ",end=" ")
            else :
                print("*", end=" ")
        print("\n")
    print("\n")

print_big("b")    