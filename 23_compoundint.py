def compound_interest(principalamt, rate, time):
    amount = principalamt * (pow((1 + rate / 100). time))
    CI = amount - principalamt
    print("the compound interest is", CI)