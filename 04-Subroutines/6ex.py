def num():
    for i in range(1, 10):
        if i % 3 == 1:
            print()
            print(i, end=" ")   
        else:
            print(i, end=" ")
    print()

num()


# def phone_num():
#     for i in range(0, 7, 3):
#         for j in range(1, 4):
#             print(f' {i+j}', end="")
#         print()

# phone_num()