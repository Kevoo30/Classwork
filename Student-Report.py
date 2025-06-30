from typing import Final

# Immutable types
# '''
# str
# int
# float
# bool
# bytes
# tuple
# '''
# #Mutable types
# '''
# list
# set
# dict
# '''

#type annotation
number: int = 10
decimal: float = 2.5
active: bool = True

names: list = ["John","Doe"]
name: str = 'John Doe'
marks: tuple = (1, 24, 5)

print(number)
print(decimal)
print(names)

def greet(name: str): #name is the argument
    # print(name)
    return f"Welcome, {name.title()}"

def function_one(self):
    pass


# print(f"Welcome, {name}")
    #
    # if age < 20:
    #     print("adult")
    # elif age > 50:
    #     print("adult")
    # else:
    #     print("underage")
    #
    # return None


for i in 'John Doe':
    print(i)

#arguments are dummy parameters while parameters are the actual values that are passed

greet("John") #john is the parameter

def add(x: int, y: int) -> int:
    return  x + y
#
# def area_circle(radius: float)-> None:
#     PI = 3.14
#     radius_sq = radius * radius
#     area = PI * radius_sq
#     print(area)
#     return
# print(area_circle(7))

def area_circle(radius: float)-> float:
    PI = 3.14
    return  PI *(radius * radius)
print(area_circle(7))



def has_passed(average: float) -> bool:
    return average >= 50

def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

def students_performance() -> None:
    name: str = input("Enter student name: ")
    print(greet(name))

    scores: list[int] = []

    for  i in range(3):
        while True:
            try:
                score = int(input(f"Enter score for subject {i+1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("The score must be between 0 and 100")

            except ValueError:
                print("Please enter a valid number")


        average_score: float = compute_average(scores)
        is_pass: bool = has_passed(average_score)


        print("\n ----Report Card----")
        print(f"Name     : {name}")
        print(f"Scores   : {scores}")
        print(f"Average  : {average_score:.2f}")
        print(f"Status   : {'Pass' if has_passed else 'Fail'}")

        assignments_done: int = 5
        pts: float = 2.5
        total_score: float = average_score + pts

        print(f"Bonus Points: + {pts} for {assignments_done} assignments")
        print(f"Final Score: {total_score:.2f}")

if __name__ == "__main__":
    students_performance()

