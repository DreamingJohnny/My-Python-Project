
def print_my_info():
    my_age = 37

    my_name = "Johan"

    msg = f"My name is {my_name} and I am {my_age} years old"

    print(msg)

def string_manipulation():
    msg = "Python is an amazing programming language!"

    print(msg)

    first_word = msg.split()[0]
    print(first_word)

    upper_msg = msg.upper()
    print(upper_msg)

    replaced_msg = msg.replace("a", "@")

    print(replaced_msg)

def favorite_food_list():
    favorite_foods = ["chocolate", "black tea", "clementine"]

    print(f"These are my favorite foods: {favorite_foods}")

    favorite_foods.append("butter chicken")

    print(f"Here, I've added one more food I like: {favorite_foods}")

    favorite_foods.pop(0)

    print(f"And now I've removed the first one in the list: {favorite_foods}")

    favorite_foods.append("milk chocolate")

    print(f"And now I added it back to the end of the list: {favorite_foods}")

    food_starting_with_c = []

    for x in favorite_foods:
        if x.startswith("c"):
            food_starting_with_c.append(x)

    print(f"And here is the list again, with nothing changed: {favorite_foods}")
    print(f"and here are the items from the list, that starts with the letter \"c\" {food_starting_with_c}")

def list_comprehension():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    even_numbers = [x for x in numbers if x % 2 == 0]

    print(even_numbers)

    numbers_div_by_2_and_3 = [x for x in numbers if x % 2 == 0 and x % 3 == 0]

    print(numbers_div_by_2_and_3)

def student_dictionaries():
    student_scores = {
        "Anna": 76,
        "Bert": 59,
        "Clara": 66}

    for x in student_scores:
        print(x)

    # Adds another student
    student_scores.update({"Denni": 94})

    for x in student_scores:
        print(x)

    # Update the score of one student
    student_scores.update({"Anna": 92})

    for x in student_scores:
        print(x)

    # Prints every score above 90
    [print(f"Name: {name}") for name, score in student_scores.items() if score > 90]

    # Calc and prints average scores
    print(sum(student_scores.values()) / len(student_scores))

def dictionary_comprehension():

    squared_dict = {x: x**2 for x in range(1,6)}
    print(squared_dict)

    # is this the same "x" as is used above?
    stringed_numbers_dict = {x: str(x) for x in range(1,6)}
    print(stringed_numbers_dict)

    odd_numbers_dict = {x: x % 2 != 0 for x in range(1,6)}
    print(odd_numbers_dict)

    more_odd_numbers = {x: x for x in range(1,6) if x % 2 != 0}
    print(more_odd_numbers)

def grade_calculator(score):
    if not isinstance(score, (int,float)):
        raise TypeError("This argument must be a number")

    if score >= 90:
        return "A"
    if score >=80:
        return "B"
    if score >= 70:
        return "C"
    else:
        return "F"

def calculate_total(price, taxe_rate, discount):

    # Converts all variables to positive
    price, taxe_rate, discount = abs(price), abs(taxe_rate), abs(discount)

    total = price + (price*taxe_rate)
    total -= discount

    return "{:.2f}".format(total)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        return 2025-self.year

    def get_info(self):
        return f"{self.title}, {self.author}, {self.year}"
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        wheel = 4

    def move(self):
        return f"A car of the model {self.model} goes broom, broom."

class Bicycle:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        wheel = 2

    def move(self):
        return f"A bike of the model {self.model} swooshes past."

def test_movement(object):
    print(object.move())


# Exercise 11
universal_truth = "the Logos is without Beginning or End"

def the_outerworld():
    universal_truth = "the Darkness that Comes Before"

def the_conditioning():
    
    global universal_truth
    
    # interesting, does the global variable need to be declared on another line then it is modified on?
    universal_truth = "Through the Logos, my Chains are Lessened"

the_outerworld()
print(universal_truth)

the_conditioning()
print(universal_truth)

# Exercise 12
def safe_divide(dividend, divisor):

    try:
        return dividend/divisor
    except ZeroDivisionError:
        print("Couldn't divide by zero. Returning 0.")
        return 0
    except TypeError:
        print("Was unable to divide, argument received wasn't a number")
        return None

print(safe_divide(15,3))

print(safe_divide(10,0))

print(safe_divide("Hello", 5))

print(safe_divide(33,11))