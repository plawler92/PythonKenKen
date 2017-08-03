import os
from board import Board

def clear():
    os.system('clear')
    #windows: os.system('cls')

size = int(input('Board Size: '))
board = Board(size)
clear()


def main_menu():
    print('1) Add')
    print('2) Subtract')
    print('3) Multiply')
    print('4) Divide')
    print('Anything else = exit')
    return input('')
    
def process_add():
    print('Add')
    target = input('Target Number: ')
    nums = input('Num Boxes: ')
    repeats = input('Max Repeats: ')
    return board.add(target, nums, repeats)
    
def process_subtract():
    print('Subtract')
    target = input('Target Number: ')
    return board.subtract(target)
    
def process_multiply():
    print('Multiply')
    target = input('Target Number: ')
    nums = input('Num Boxes: ')
    repeats = input('Max Repeats: ')
    return board.multiply(target, nums, repeats)
    
def process_divide():
    print('Divide')
    target = input('Target Number: ')
    return board.divide(target)
    
def print_results(results):
    for result in results:
        print(result)

history = []
while True:
    option = main_menu()
    history.append((option, type(option)))
    clear()
    results = []
    if option == '1':
        results = process_add()
    elif option == '2':
        results = process_subtract()
    elif option == '3':
        results = process_multiply()
    elif option == '4':
        results = process_divide()
    else:
        break
    print_results(results)
    input('press any button to continue ')