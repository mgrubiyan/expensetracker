from datetime import date
import os


def add(z, ID):
    clear_screen()
    q, d, a = z[0], z[1], z[2]
    f = open("expenseslist.txt", "a")
    f.write(str(ID) + ' ' + str(date.today()) + ' ' + d + ' ' + a + '\n')
    f.close()
    print(f"Expense added successfully (ID: {ID})" + '\n')


def list():
    clear_screen()
    f = open("expenseslist.txt", "r")
    print(f.read())
    f.close()


def summary():
    clear_screen()
    f = open("expenseslist.txt", "r")
    s = 0
    for x in f.read().splitlines():
        s += float(x.split(' ')[3])
    print(f'Total expenses: {s}' + '\n')
    f.close()


def delete(z):
    clear_screen()
    l = []
    f = open("expenseslist.txt", "r")
    q, d = z[0], z[1]
    for x in f.read().splitlines():
        x = x.split()
        if int(x[0]) > int(d):
            l.append(str(int(x[0]) - 1) + ' ' + x[1] + ' ' + x[2] + ' ' + x[3])
        elif int(x[0]) < int(d):
            l.append(' '.join(x))
    f.close()
    f = open("expenseslist.txt", "w")
    for i in l:
        f.write(i + '\n')
    f.close()
    print(f"Expense deleted successfully (ID: {d})" + '\n')


def clear():
    clear_screen()
    f = open("expenseslist.txt", "w")
    f.close()


def getID():
    clear_screen()
    f = open("expenseslist.txt", "r")
    lines = f.readlines()
    f.close()
    if not lines:
        ID = 1
    else:
        max_id = 0
        for line in lines:
            current_id = int(line.split()[0])
            if current_id > max_id:
                max_id = current_id
        ID = max_id + 1
    return ID


def hlp():
    clear_screen()
    f = open("help.txt", "r")
    for x in f.read().splitlines():
        print(x)
    print()



def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass