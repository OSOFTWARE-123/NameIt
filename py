def enterName(val, pluss):
    res = 0
    plus = pluss
    for i in range(1, val + 1):
        res += (i * plus)
        print(f"Step {i} : {res}")
    return res

val = int(input("\nEnter how many times its loop : "))
plus = int(input("Enter every step how much its plus : "))
print("")
print(enterName(val, plus))
print("")
