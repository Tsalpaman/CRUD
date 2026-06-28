from mod_pupils import print_pupil, print_pupils_details, create_pupil, delete_pupil_by_id, search_pupil_by_surname, \
    menu3, next_id, students
from teacher import teachers, create_teacher, read_teachers, update_teacher, delete_teacher


def main():
    global students

    cnt = 0
    cn = 0
    while True:
        tempname = ""  # final name
        tempsurname = ""  # final surname
        flag = 1
        fl5 = True  # it is for valid values
        # menu
        print("")
        print("Press 1 for a new registration of a pupil")
        print("Press 2 for print of pupils")
        print("Press 3 for update of a pupil")
        print("Press 4 for delete of a pupil")
        print("Press 5 for a new registration of teacher")
        print("Press 6 for print of a teacher")
        print("Press 7 for update of a teacher")
        print("Press 8 for delete of a teacher")
        print("Press 9 for exit")
        print("")

        while True:
            choice = input("Choice: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 9:
                    break
                print("Wrong Input! ", end="")
            else:
                print("Wrong Input! ", end="")
        print("")

        if choice == 1:  # appends a person
            create_pupil()
        elif choice == 2:  # prints a person
            print("Press 1 to print a specific student")
            print("Press 2 to print all students")
            print("Press 3 to print all students' name")
            print("")
            while True:
                ch22 = (input("Choice: ")).strip()
                if ch22.isdigit():
                    ch22 = int(ch22)
                    if 1 <= ch22 <= 3:
                        break
                    print("Wrong input!", end=" ")
                else:
                    print("Wrong input!", end=" ")
            print("")
            if ch22 == 1:
                while True:
                    iden = input("Insert ID: ")
                    iden = iden.strip()
                    if iden.isdigit():
                        iden = int(iden)
                        if iden >= 1000:
                            iden = str(iden)
                            break
                        print("Wrong Input! ", end="")
                    else:
                        print("Wrong Input! ", end="")
                print("")
                print_pupil(iden)
            elif ch22 == 2:
                print_pupils_details()
            else:
                for i in range(1, len(students) - 1):
                    print(students[i][1], end=" ")
                    print(f"{students[i][3][0]}.", end=" ")
                    print(students[i][2], end=", ")
                print(students[len(students) - 1][1], end=" ")
                print(f"{students[len(students) - 1][3][0]}.", end=" ")
                print(students[len(students) - 1][2])
                print("")
        elif choice == 3:  # updates information of a person
            fl3 = False
            while True:
                ans = input("Do you want to update a student with id or surname? Insert id or surname: ")
                if ans == "id" or ans == "surname":
                    break
                else:
                    print("Wrong Input! ", end="")
            print("")
            if ans == "id":
                pos = 0
                while True:
                    iden = input("Insert ID: ")
                    iden = iden.strip()
                    if iden.isdigit():
                        iden = int(iden)
                        if iden >= 1000:
                            iden = str(iden)
                            break
                        print("Wrong Input! ", end="")
                    else:
                        print("Wrong Input! ", end="")
                print("")
                for i in range(len(students)):
                    if students[i][0] == iden:
                        fl3 = True
                if not fl3:  # checks if there is a person with the user's input id
                    print(f"There is no registration with id: {iden}")
                menu3(iden, pos)
            else:
                pos = 2
                while True:
                    sur = input("Insert Surname: ")
                    sur = sur.strip()
                    sur = sur.capitalize()
                    if sur.isalpha():
                        break
                    print("Wrong Input! ", end="")
                print("")
                search_pupil_by_surname(sur)
        elif choice == 4:  # deletes person
            fl4 = False
            while True:
                ans = input("Do you want to delete a student with id or surname? Insert id or surname: ")
                if ans == "id" or ans == "surname":
                    break
                print("Wrong Input! ", end="")
            print("")
            if ans == "id":
                pos = 0
                while True:
                    iden = input("Insert ID: ")
                    iden = iden.strip()
                    if iden.isdigit():
                        iden = int(iden)
                        if 1000 <= iden <= len(students) + 1000 - 2:
                            iden = str(iden)
                            break
                        else:
                            print("Wrong Input! ", end="")
                    else:
                        print("Wrong Input! ", end="")

                delete_pupil_by_id(iden)
            else:
                pos = 2
                while True:
                    sur = input("Insert Surname: ")
                    sur = sur.strip()
                    sur = sur.capitalize()
                    if sur.isalpha():
                        break
                    print("Wrong Input! ", end="")
                print("")
                ids = set()  # to prevent to change id from other student that he has not the same surname
                cnt2 = 0  # chooses the cases of have no registration, one or two and more
                for i in range(1, len(students)):
                    if sur == students[i][2]:
                        ident = students[i][0]  # save the id of the student's surname for using it at the menu
                        cnt2 += 1
                if cnt2 >= 2:
                    for i in range(len(students)):
                        if sur == students[i][2]:
                            for j in range(len(students[i])):
                                print(students[0][j], end="")
                                print(students[i][j])
                                ids.add(students[i][0])
                            print("")
                    while True:
                        upid = input("Which student do you want to update? Insert id: ")
                        if upid.isdigit() and upid in ids:
                            break
                        print("Wrong input! ", end="")
                    for i in range(len(students)):
                        if students[i][0] == upid:
                            print("")
                            students.pop(i)
                            break
                    else:
                        print(f"There is no student with surname: {sur}")
                elif cnt2 == 0:
                    print(f"There is no student with surname: {sur}")
                else:
                    for i in range(len(students)):
                        if students[i][2] == sur:
                            students.pop(i)
                            fl4 = True
                            break
                    if not fl4:  # checks if there is a person with the user's input id
                        print("")
                        print(f"There is no registration with surname: {sur}")
        elif choice == 5:
            while fl5:
                tempname = ""
                fl5 = False
                name = input("Teacher's Name: ")
                while name == "":
                    name = input("Wrong input! Teacher's Name: ")
                name = name.strip()
                name = name.split()
                for i in range(len(name)):
                    if not name[i].isalpha():
                        fl5 = True  # to maintain the loop
                        name = name.clear()
                        tempname = ""
                        print("Wrong Input! ", end="")
                        break
                    name[i] = name[i].title()
                    tempname = tempname + name[i]  # if a person has more than 1 name adds it
                    if i != len(name) - 1:
                        tempname = tempname + " "
            fl5 = True
            while fl5:
                tempsurname = ""
                fl5 = False
                surname = input("Teacher's Surname: ")
                while surname == "":
                    surname = input("Wrong input! Teacher's Surname: ")
                surname = surname.strip()
                surname = surname.split()
                for i in range(len(surname)):
                    if not surname[i].isalpha():
                        fl5 = True
                        surname = surname.clear()
                        tempsurname = ""
                        print("Wrong Input! ", end="")
                        break
                    surname[i] = surname[i].title()
                    tempsurname = tempsurname + surname[i]
                    if i != len(surname) - 1:
                        tempsurname = tempsurname + " "  # if a person has more than 1 surname adds it
            full_name = tempname + " " + tempsurname
            create_teacher(full_name)
        elif choice == 6:
            while True:
                ch6 = input("Insert teacher's id: ")
                if ch6.isdigit():
                    break
                else:
                    print("Wrong input! ", end=" ")
            print("")
            r = read_teachers(ch6)
        elif choice == 7:
            fl7 = False
            while True:
                ch7 = input("Insert teacher's id: ")
                if ch7.isdigit():
                    break
                else:
                    print("Wrong input! ", end=" ")
            print("")
            for i in range(len(teachers)):
                for k, v in teachers[i].items():
                    if ch7 == k:
                        fl7 = True
                        while fl7:  # it is for valid values
                            tempname = ""
                            fl7 = False
                            name = input("Teacher's Name: ")
                            while name == "":
                                name = input("Wrong input! Teacher's Name: ")
                            name = name.strip()
                            name = name.split()
                            for i in range(len(name)):
                                if not name[i].isalpha():
                                    fl7 = True
                                    name = name.clear()
                                    tempname = ""
                                    print("Wrong Input! ", end="")
                                    break
                                name[i] = name[i].title()
                                tempname = tempname + name[i]  # if a person has more than 1 name adds it
                                if i != len(name) - 1:
                                    tempname = tempname + " "
                        fl7 = True
                        while fl7:
                            tempsurname = ""
                            fl7 = False
                            surname = input("Teacher's Surname: ")
                            while surname == "":
                                surname = input("Wrong input! Teacher's Surname: ")
                            surname = surname.strip()
                            surname = surname.split()
                            for i in range(len(surname)):
                                if not surname[i].isalpha():
                                    fl7 = True
                                    surname = surname.clear()
                                    tempsurname = ""
                                    print("Wrong Input! ", end="")
                                    break
                                surname[i] = surname[i].title()
                                tempsurname = tempsurname + surname[i]
                                if i != len(surname) - 1:
                                    tempsurname = tempsurname + " "  # if a person has more than 1 surname adds it
                        full_name = tempname + " " + tempsurname
                        print("")
                        update_teacher(ch7, full_name)
                        fl7 = True  # stops the loop
                        break
                if fl7:  # stops the outer loop
                    break
            else:
                print(f"There is no teacher with id: {ch7}")
        elif choice == 8:
            while True:
                ch8 = input("Insert teacher's id: ")
                if ch8.isdigit():
                    break
                print("Wrong Input! ", end="")
            print("")
            delete_teacher(ch8)
        else:  # exits the program
            break
        if flag == 0:
            students[len(students) - 1].clear()
            students.pop()


main()

# 25:00h
