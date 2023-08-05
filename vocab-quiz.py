import sqlite3
import random

with sqlite3.connect("vocab-db.db") as db:
    cursor = db.cursor()

def checker(row_num,ans_user):
    cursor.execute("SELECT * FROM words WHERE ID = ?",[row_num])

    for x in cursor.fetchall():
        ans_comp = x[5]

    if ans_user == ans_comp:
        status = "Correct"
    else:
        status = "Wrong"

    print("")
    return status

def question_generator(row_num):
    cursor.execute("SELECT * FROM words WHERE ID = ?",[row_num])

    for x in cursor.fetchall():
        word = x[0]

        print("What is the meaning of",word,"?")
        print("")
        print("[a] ", x[1])
        print("")
        print("[b] ", x[2])
        print("")
        print("[c] ", x[3])
        print("")
        print("[d] ", x[4])
        print("")

def main():
    score = 0
    questions = 1

    while questions <= 10:
        row_num = random.randint(1,20)
        cursor.execute("SELECT flag FROM words WHERE ID = ?",[row_num])

        for x in cursor.fetchall():
            flag = x[0]

        if flag == "unused":
            print("")
            print("Question",questions)
            print("------------------")

            question_generator(row_num)

            cursor.execute("UPDATE words SET flag = 'used' WHERE ID = ?",[row_num])
            db.commit()

            ans_user = input("Enter here: ")

            status = checker(row_num,ans_user)
            print(status)

            questions = questions + 1

            if status == "Correct":
                score = score + 1

    print("You got",score,"questions correct!")
    print("------------------")

    if score == 10:
        print("Congratulations, you earned THREE STARS!")
    elif score >= 7 and score <= 9:
        print("Good job, you earned TWO STARS!")
    elif score >= 5 and score <= 6:
        print("Not bad, you earned ONE STAR!")
    else:
        print("Better luck next time, you get no stars")

main()
