from datetime import date
import funcs
f = open("expenseslist.txt", "w")
f.close()
ID = 1
while z := input().split():
    match z[0]:
        case 'add':
            funcs.add(z, ID)
            ID += 1
        case 'list':
            funcs.list()
        case 'summary':
            funcs.summary()
        case 'delete':
            funcs.delete(z)
            ID -= 1
        case 'clear':
            ID = 1
            funcs.clear()
        case 'stop':
            break