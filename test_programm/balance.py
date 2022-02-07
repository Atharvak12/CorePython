
try:
    balance =5000
    request = int(input("Enter amount you want to withdrew"))
    if request <= balance and request > 0  :
        print("Succesfull transaction")
    else:
        raise Exception ("Not possible transaction")
except Exception as e:
    print(e)
