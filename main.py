# Instructions
print('''
Welcome to <game name>!
Enter the level you wanna play
''')

# main variables
run = True
level_done = 0

# Main command loop
while run:
    # Asking for commands
    inp = input('Enter a level: ')

    if inp == 'quit()':
        break
    else:
        inp = int(inp)

    while inp > 3 and inp < 1:
        print('Please input a valid command.')
        inp = input('Enter a level: ')

    if inp == 1:
        import level1
        level1.main()
        level_done += 1
    elif inp == 2:
        import level2
        level2.main()
        level_done += 1
    elif inp == 3:
        import level3
        level3.main()
        level_done += 1

    if level_done >= 3:
        run = False