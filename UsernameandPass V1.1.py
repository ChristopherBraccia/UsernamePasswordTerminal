correct = True
while correct:
    name = input('Please Enter Your Username.')
    if name == 'Admin':
        print('Hello Chris!')
        pw = input('Please Enter Your Password.')
        if pw == 'Test':
            print('Access Granted!')
            break
        else:
            print('Access Denied!')
            break

