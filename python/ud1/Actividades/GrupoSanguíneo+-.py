grupo1=input("Dime tu grupo sanguíneo: ").upper()
grupo2=input("Dime otro grupo sanguíneo para saber si sois complatibles: ").upper()
if grupo1=="A+":
    if grupo2==("A+" or "AB+"):
        print("Sus grupos son compatibles")
    else:
        print("Sus grupos no son compatibles")
    print("Su grupo sanguíneo, recive de A+- y de 0+-")
elif grupo1=="B+":
    if grupo2==("B+" or "AB+"):
        print("Sus grupos son compatibles")
    else:
        print("Sus grupos no son compatibles")
    print("Su grupo sanguíneo, recive de B+- y de 0+-")
elif grupo1=="AB+":
    if grupo2=="AB+":
        print("Sus grupos son compatibles")
    else:
        print("Sus grupos no son compatibles")
    print("Su grupo sanguíneo, recive de A+-, B+-, AB+- y de 0+-")
elif grupo1=="0+":
    print("Sus grupos sanguíneos son compatibles")
    print("Su grupo sanguíneo, recive de 0+-")
elif grupo1=="A-":
    if grupo2==("A-" or "AB-"):
        print("Sus grupos son compatibles")
    else:
        print("Sus grupos no son compatibles")
    print("Su grupo sanguíneo, recive de A- y de 0-")
elif grupo1=="B-":
    if grupo2==("B-" or "AB-"):
        print("Sus grupos son compatibles")
    else:
        print("Sus grupos no son compatibles")
    print("Su grupo sanguíneo, recive de B- y de 0-")
elif grupo1=="AB-":
    if grupo2=="AB-":
        print("Sus grupos son compatibles")
    else:
        print("Sus grupos no son compatibles")
    print("Su grupo sanguíneo, recive de A-, B-, AB- y de 0-")
elif grupo1=="0-":
    print("Sus grupos sanguíneos son compatibles")
    print("Su grupo sanguíneo, recive de 0-")
else:
    print("Error")