from datetime import date


def add(z, ID):
    q, d, a = z[0], z[1], z[2]
    f = open("expenseslist.txt", "a")
    f.write(str(ID) + ' ' + str(date.today()) + ' ' + d + ' ' + a + '\n')
    f.close()
    print(f"Expense added successfully (ID: {ID})" + '\n')


def list():
    f = open("expenseslist.txt", "r")
    print(f.read())
    f.close()


def summary():
    f = open("expenseslist.txt", "r")
    s = 0
    for x in f.read().splitlines():
        s += int(x.split(' ')[3])
    print(f'Total expenses: {s}' + '\n')
    f.close()


def delete(z):
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
    f = open("expenseslist.txt", "w")
    f.close()