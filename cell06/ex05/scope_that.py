def add_one(number):
    """
    รับค่าหนึ่งตัว เพิ่ม 1 แล้ว return ค่าใหม่
    """
    number += 1
    return number

x = 5
print("Before calling add_one:", x)

add_one(x)
print("After calling add_one without assignment:", x)

x = add_one(x)
print("After calling add_one with assignment:", x)