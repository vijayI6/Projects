import random
next = next
while next != 'exit':
    num = random.randint(1,6)
    match num:
        case 1:
            print(' _______')
            print('|       |')
            print('|   1   |')
            print('|_______|')
        case 2:
            print(' _______')
            print('|       |')
            print('|   2   |')
            print('|_______|')
        case 3:
            print(' _______')
            print('|       |')
            print('|   3   |')
            print('|_______|')
        case 4:
            print(' _______')
            print('|       |')
            print('|   4   |')
            print('|_______|')
        case 5:
            print(' _______')
            print('|       |')
            print('|   5   |')
            print('|_______|')
        case 6:
            print(' _______')
            print('|       |')
            print('|   6   |')
            print('|_______|')

    if next == 'exit':
        break
    next = input('Press Enter to continue to Roll:')




