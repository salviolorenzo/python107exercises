floor = {}
hotel = {}

print('Hello, welcome to this hotel.')
check = (input('Are you checking in or out? (I for check in/ O for check out.) ')).upper()
if check ==  'I': #checking in
    which_floor = input('Which floor? ')
    which_room = input('Room Number: ')
    if which_room[0] == which_floor:
        guest_number = int(input('How many in your party? '))
        names = []
        while len(names) < guest_number: 
            names.append(input('Name: '))
    else:
        print('That room is not on your floor.')
    hotel = {
        which_floor: {
            which_room: names
        }
    }
    print(hotel)
    

elif check == 'O':
    pass
else:
    print("Please type I or O")