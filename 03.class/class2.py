score = int(input("Enter your score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

match score:
    case 90|100:
        print("Grade: A")
    case 80|89:
        print("Grade: B")
    case 70:
        print("Grade: C")
    case 60:
        print("Grade: D")
    case _:
        print("Grade: F")

if score >= 60:
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Grade: F")