numbers = list(range(1,6))
print(numbers) #[1,2,3,4,5,6]

# range() function to skip numbers in a given range.
# list the even numbers between 1 and 10:
# does not support float and string

even_numbers = list(range(2,11,2))
print(even_numbers)

def get_List_Of_Squares(range):
    squares = []
    for value in range:
        square = value**2
        squares.append(square)
    print(squares)
    return squares

name = get_List_Of_Squares(range(1,11))
get_List_Of_Squares(range(1,11,3))

print(name)

# Functions on lists
digits = list(range(1,10))
print(min(digits))
print(max(digits))
print(sum(digits))
