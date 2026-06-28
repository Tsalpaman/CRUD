teachers = [
    {"teacher_id": "full_name"}
]


def create_teacher(full_name):
    fl = True
    fl2 = False
    for i in range(1, len(teachers)):
        for v in teachers[i].values():
            if v == full_name:
                fl2 = True
                print(f"There is another teacher with the name: {full_name}")
                while True:
                    ch5 = (input("Do you want to continue? If yes press 1 otherwise press 0: ")).strip()
                    if ch5.isdigit() and (ch5 == "1" or ch5 == "0"):
                        break
                    else:
                        print("Wrong input!", end=" ")
                if ch5 == "0":
                    print("No registration!")
                    fl = False  # stops the loop
                    break
        if fl2:  # stops the outer loop
            break
    flag = False
    if fl:
        for i in range(1, len(teachers)):
            for k in teachers[i].keys():
                if k != str(i + 1000 - 1):
                    teachers.insert(i, {str(i + 1000 - 1): full_name})
                    flag = True
                    break
            if flag:
                break
        else:
            teachers.append({str(len(teachers) + 1000 - 1): full_name})
        print("\nRegistration done succesfully!")


def read_teachers(teacher_id):
    for i in range(1, len(teachers)):
        for k, v in teachers[i].items():
            if k == teacher_id:
                print(f"Teacher with id {teacher_id}: {v}")  # teachers[i]
                return teachers[i]
    print(f"There is no teacher with id: {teacher_id}")
    return None


""" def update_teacher(teacher_id, keynew): # key change
    fl = False
    for i in range(1, len(teachers)):
        for k, v in teachers[i].items():
            if teacher_id == k:
                teachers[i].clear()
                teachers[i][keynew] = v
                print(teachers[i])
                print(teachers)
                fl = True
                break
        if fl:
            break
"""


def update_teacher(teacher_id, valuenew):  # value change
    fl = False
    for i in range(1, len(teachers)):
        for k, v in teachers[i].items():
            if teacher_id == k:
                teachers[i].clear()
                teachers[i][teacher_id] = valuenew
                print(f"Teacher's name with id {teacher_id} has changed as: {valuenew}")
                fl = True
                break
        if fl:
            break
    else:
        print(f"There is no teacher with id: {teacher_id}")


def delete_teacher(teacher_id):
    fl = False
    for i in range(1, len(teachers)):
        for k, v in teachers[i].items():
            if teacher_id == k:
                teachers[i].clear()
                print(f"Teacher with id {teacher_id} has deleted")
                fl = True
                break
        if fl:
            break
    else:
        print(f"There is no teacher with id: {teacher_id}")
