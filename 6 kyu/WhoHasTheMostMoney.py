class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

sum_money = lambda student: 5*student.fives + 10*student.tens + 20*student.twenties


def most_money(students):
    richest = students[0]
    same_wealth = False

    if len(students) == 1: 
        return richest.name


    for student in students[1:]:
        if sum_money(student) > sum_money(richest):
            richest = student
            same_wealth = False
    
        elif sum_money(student) == sum_money(richest):
            same_wealth = True
        

    if same_wealth:
        return 'all'
    else:
        return richest.name
    

def most_money(students):
    if len(students) == 1:
        return students[0].name

    total = [sum_money(student) for student in students]
    
    return 'all' if min(total) == max(total) else students[total.index(max(total))].name
