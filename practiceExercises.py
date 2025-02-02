
def printmyinfo():
    my_age = 37

    my_name = "Johan"

    msg = f"My name is {my_name} and I am {my_age} years old"

    print(msg)

def stringmanipulation():
    msg = "Python is an amazing programming language!"

    print(msg)

    first_word = msg.split()[0]
    print(first_word)

    upper_msg = msg.upper()
    print(upper_msg)

    replaced_msg = msg.replace("a", "@")

    print(replaced_msg)

def favoritefoodlist():
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

def listcomprehension():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    even_numbers = [x for x in numbers if x % 2 == 0]

    print(even_numbers)

    

favoritefoodlist()