dia=int(input("Dime el dia en el que se encuentra: "))
mes=int(input("Dime el mes en el que se encuentra: "))
año=int(input("Dime el año en el que se encuentra: "))
enero=31
febrero=28
marzo=31
abril=30
mayo=31
junio=30
julio=31
agosto=30
septiembre=31
octubre=30
noviembre=31
diciembre=30
match mes:
    case 1:
        print(dia)
    case 2:
        print((enero)+dia)
    case 3:
        print((enero+febrero)+dia)
    case 4:
        print((enero+febrero+marzo)+dia)
    case 5:
        print((enero+febrero+marzo+abril)+dia)
    case 6:
        print((enero+febrero+marzo+abril+mayo)+dia)
    case 7:
        print((enero+febrero+marzo+abril+mayo+junio)+dia)
    case 8:
        print((enero+febrero+marzo+abril+mayo+junio+julio)+dia)
    case 9:
        print((enero+febrero+marzo+abril+mayo+junio+julio+agosto)+dia)
    case 10:
        print((enero+febrero+marzo+abril+mayo+junio+julio+agosto+septiembre)+dia)
    case 11:
        print((enero+febrero+marzo+abril+mayo+junio+julio+agosto+septiembre+octubre)+dia)
    case 12:
        print((enero+febrero+marzo+abril+mayo+junio+julio+agosto+septiembre+octubre+noviembre)+dia)