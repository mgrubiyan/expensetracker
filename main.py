from datetime import date
import funcs
ID = funcs.getID()
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
        case 'help':
            funcs.hlp()
        case _:
            funcs.clear_screen()
            print(f'Unknown command: '
                  f'Use [help] for more info')
            print()
