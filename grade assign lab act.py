#fucnjtion
def grade_assigner():
    score = int(input("Enter your score: \n >"))
    if score < 0 or score > 100:
        print("invalid Score, Please enter a value between 0 and 100")
    elif score >= 90:
        print ("Grade A")
    elif score >= 80:
        print ("Grade B")
    elif score >= 70:
        print ("Grade C")
    elif score >= 60:
        print ("Grade D")
    elif score >= 0:
        print ("Grade F")

#MAIN TYPE SHI

grade_assigner()

while True:
    a = input("Do you want to enter your score?(yes/no): \n > ").strip().lower()
    if a == "yes":
        print("very well")
        grade_assigner()

    else:
        print("program finished")
        break