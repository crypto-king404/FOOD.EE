### MODULES
import random, sqlite3

### VARIABLES

user = ''

resto = {
    1: 'jehangirs',
    2: 'gazebo',
    3: 'manvaar',
    4: 'kamat',
    5: 'venus',
    6: 'aryaas'
}

### FUNCTIONS

datab = sqlite3.connect('accounts.db')
cur = datab.cursor()

cur.execute(
    'create table if not exists accounts(username varchar(10), password varchar(10), address varchar(10))'
)

cur.execute(
    'create table if not exists resto1(name varchar(10), rating float(3,1), veg_nonveg varchar(10))'
)


def valid_char(y):
    x = ''
    while True:
        x = input('---->'.center(10))
        if x.isdigit() == True:
            if int(x) in y:
                x = int(x)
                break
            else:
                print("*Please Enter a Valid Option*".center(60))
                pass
        else:
            print("*Please Enter a Valid Option*".center(60))
            pass

    return x


def valid_text(x):
    return x.strip()


def main_menu():
    print('\n', '-' * 60, '\n')
    print('FOOD.EE'.center(60), '\n')
    print('MAIN MENU'.center(60), '\n')
    print(
        '1. Register'.center(15) + "2. Login".center(15) +
        "3. View as Guest".center(15), "4. Exit".center(15), '\n')

    ch = valid_char([1, 2, 3, 4])
    print("\n" * 2)

    if ch == 1:
        register()
    elif ch == 2:
        login()
    elif ch == 3:
        guest()
    elif ch == 4:
        print("*END OF PROGRAMME*".center(60))


def register():
    print('\n', '-' * 60, '\n')
    print("REGISTRATION".center(60), '\n')

    username = valid_text(input("Enter username: "))
    password = valid_text(input("Enter password: "))
    pass1 = valid_text(input("Confirm password: "))

    while password != pass1:
        print()
        print("Please enter correct password: ")
        pass1 = valid_text(input("Confirm password: "))

    address = input('Address - ')

    cur.execute(
        "insert into accounts(username,password,address) values('{}','{}','{}')"
        .format(username, pass1, address))
    datab.commit()

    print('\n', '-' * 60, '\n')
    prnt = 'Welcome to FOOD.EE, \'' + username + '\' !!!'
    print(prnt.center(60), '\n')
    online_or_dinein()


def login():
    print('\n', '-' * 60, '\n')
    print('LOGIN'.center(60), '\n')

    while True:
        acc1 = cur.execute('select username,password from accounts')
        acc = acc1.fetchall()

        print('\n')
        username = valid_text(input("Enter username: "))
        password = valid_text(input("Enter password: "))
        print('\n')

        var = 0

        for i in acc:
            if i[0] == username and i[1] == password:
                prnt = 'Welcome to FOOD.EE, \'' + username + '\' !!!'
                print(prnt.center(60), '\n')
                var = 1
                break
        else:
            print("Username/Password is Incorrect")

        if var == 1:
            break

    online_or_dinein()


def guest():
    print('\n', '-' * 60, '\n')
    print('\n', "You are now viewing as a \"GUEST\"".center(60), '\n')
    online_or_dinein()


def online_or_dinein():
    print('\n', '-' * 60, '\n')

    print('1. Online Delivery'.center(30) + "2. Main Menu".center(30), '\n')

    y = valid_char([1, 2])

    if y == 1:
        online_del()
    elif y == 2:
        main_menu()


def online_del():
    print('\n', '-' * 60, '\n')

    print('SORT BY - '.center(60), '\n')
    print('1. Rating'.center(30) + "2. Veg/NonVeg".center(30), '\n')
    print('0. Skip'.center(60), '\n')

    choice = valid_char([0, 1, 2])

    print('\n', '-' * 60, '\n')

    if choice == 0:
        print('RESTAURANTS'.center(60), '\n')
        with open("restaurants.txt", "r") as file:
            for i in file.readlines():
                print(valid_text(i).center(60))
                print('\n')
        line = [1, 2, 3, 4, 5, 6]

    if choice == 2:

        aa = cur.execute('select name from resto1 where veg_nonveg=="Veg"')
        a = aa.fetchall()
        print('Veg'.center(60), '\n')
        for i in a:
            for j in i:
                print(j.center(60))

        print("\n")

        aaaa = cur.execute(
            'select name from resto1 where veg_nonveg=="NonVeg"')
        aaa = aaaa.fetchall()
        print('NonVeg'.center(60), '\n')
        for i in aaa:
            for j in i:
                print(j.center(60))
        print("\n" * 3)
        line = [1, 2, 3, 4, 5, 6]

    if choice == 1:
        print(
            '1. Rating > 4.5'.center(20) + "2. Rating > 4".center(20) +
            "3. Rating > 3.5".center(20), '\n')
        selec = valid_char([1, 2, 3])
        print("\n" * 2)
        if selec == 1:
            aa = cur.execute('select name from resto1 where rating>=4.5')
            aa = aa.fetchall()
            for i in aa:
                for j in i:
                    print(j.center(60) + '\n')
            line = [3, 4, 5]

        if selec == 2:
            aa = cur.execute('select name from resto1 where rating>=4')
            aa = aa.fetchall()
            for i in aa:
                for j in i:
                    print(j.center(60) + '\n')
            line = [1, 2, 3, 4, 5]

        if selec == 3:
            aa = cur.execute('select name from resto1 where rating>=3')
            aa = aa.fetchall()
            for i in aa:
                for j in i:
                    print(j.center(60) + '\n')
            line = [1, 2, 3, 4, 5, 6]

    global rchoice
    rchoice = valid_char(line)
    bill(rchoice)


def menu(x):
    print('\n', '-' * 60, '\n')

    temp = resto[x] + 'menu' + '.txt'
    u = 0

    with open(temp, "r") as file:
        r = file.readlines()
        for i in r:
            print(valid_text(i).center(60))

    print('\n', 'Press 0 after selecting your desired items')

    print()

    menulist = []
    ch = 1

    while True:
        temp2 = resto[x] + 'prices' + '.txt'
        with open(temp2, "r") as file:
            u = len(file.readlines())
        ch = valid_char(range(0, u + 1))
        if ch == 0:
            break
        menulist.append(ch)

    return menulist


def bill(x):
    val = menu(rchoice)
    print('\n', '-' * 60, '\n')
    print("FOOD.EE".center(60))
    print('\n')
    var = str(resto[x]).upper()
    print(var.center(60))
    print('\n')
    print("BILL".center(60))
    print('\n')

    total = 0
    temp3 = resto[x] + 'prices' + '.txt'
    with open(temp3, 'r') as file:
        items = file.readlines()
        for i in val:
            x = valid_text(items[i - 1])
            print(x.center(60), '\n')
            uu = len(x)
            total += int(x[uu - 3:uu + 1])

    y = 'Total ................... ' + str(total) + " AED"
    print('\n', y.center(60))
    print('\n')

    payment(total)


def payment(x):
    print('\n', '-' * 60, '\n')
    print("PAYMENT GATEWAY\n".center(60))
    print("--------------------------------\n".center(60))
    print("MODE OF PAYMENT\n".center(60))
    print("1 - Credit/Debit Card\n".center(60))
    print("2 - COD (+10AED)\n".center(60))
    n = valid_char(range(1, 5))

    if n == 1:
        print("Please Enter your Bank Number -\n".center(60))
        no = valid_char(range(1000000000000000, 9999999999999999))
        print(
            "\n",
            'YOU HAVE BEEN REDIRECTED TO A SAFE PAYMENT GATEWAY\n'.center(60))
        print('Please Enter your CVV No. -\n'.center(60))
        cvv = valid_char(range(10, 999))
        print('\n')
        print('Payment Successfully Received\n'.center(60))
        var = 'Your order will be delivered in ' + str(random.randint(
            20, 50)) + ' mins'
        print(var.center(60))

    if n == 2:
        print('\n')
        newtotal = x + 10
        str1 = 'Total Amount - ' + str(newtotal) + "DHS" + '\n'
        print(str1.center(60))
        var1 = 'Your order will be delivered in ' + str(random.randint(
            20, 50)) + ' mins'
        print(var1.center(60))


main_menu()

datab.close()
