# Accepting user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Computing the sum of all integers in the list
total_sum = sum(numbers)

print("The sum of all integers in the list is:", total_sum)

# Creating a tuple containing the names of five favorite books
favorite_books = ("To Kill a Mockingbird", "1984", "The Great Gatsby", "The Catcher in the Rye", "Moby-Dick")

#  a for loop to print each book name on a separate line
for book in favorite_books:
    print(book)

#  an empty dictionary to store information about a person
person_info = {}

# Asking the user for input and store the information in the dictionary
person_info['name'] = input("What is your name? ")
person_info['age'] = input("What is your age? ")
person_info['favorite_color'] = input("What is your favorite color? ")

# Printing the dictionary to the console
print(person_info)


# Accepting user input to create two sets of integers
set1 = set(map(int, input("Enter the first set of integers separated by spaces: ").split()))
set2 = set(map(int, input("Enter the second set of integers separated by spaces: ").split()))

#  a new set that contains only the elements that are common to both sets
common_elements = set1.intersection(set2)

print("The common elements in both sets are:", common_elements)

# Storing a list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

#  list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with an odd number of characters:", odd_length_words)
