def hello():
    print("Hi")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty")
    else: 
        for food in range(len(lunch_list)):
            if food == 0:
                print(f"First I eat {lunch_list[food]}")
            else:
                print(f"Next I eat {lunch_list[food]}")


hello()
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["food1"])
eat_lunch(["food1", "food2", "food3"])