
def Search_Failure(Userdefined_Coin):
    import main
    print "User defined coin" + Userdefined_Coin
    Failure_Message = "Sorry, the cyrpto that you just entered " + Userdefined_Coin + " Is not available"
    main.Coin_Fail_Event()


def Search_Success(Userdefined_Coin):
    import main
    result = "void"
    main.Pending_Results(Userdefined_Coin)


def Cyrptodatabase(Input_Checker):
    coin_proper = Input_Checker.lower()
    approved_cyrptos = ["bitcoin", "etherium", "litecoin"]
    counter = len(approved_cyrptos)
    if coin_proper in approved_cyrptos:
        Search_Success(coin_proper)
    else:
        Search_Failure(coin_proper)
