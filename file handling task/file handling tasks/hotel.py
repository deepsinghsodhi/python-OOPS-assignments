
f = open("hotelname.txt",mode='w')
h_name = input("Enter hotel name:")
room = int(input("Enter number of hotel rooms:"))
AC_room = int(input("Enter AC rooms:"))
Non_AC = int(input("Enter non AC rooms:"))
if room == AC_room + Non_AC:
    f.write(f"Hotel Name: {h_name}\n")
    print(f'Total Rooms: {room} ', file=f)
    print(f'AC Rooms: {AC_room} ', file= f)
    print(f'Non AC Rooms: {Non_AC}', file=f)
    print("Hotel details stored successfully....")
    f.close()
else:
    print("wrong inputs")
    f.close()