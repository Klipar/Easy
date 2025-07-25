import datetime

class colors:
    BLACK    = '\33[30m'
    RED      = '\33[31m'
    GREEN    = '\33[32m'
    YELLOW   = '\33[33m'
    BLUE     = '\33[34m'
    VIOLET   = '\33[35m'
    BEIGE    = '\33[36m'
    WHITE    = '\33[37m'
    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'
    END      = '\33[0m'

def Beautiful_Timestamp () -> str:
    return datetime.datetime.now().strftime("[%H:%M:%S]")

def failed(str, st = "", en = "\n"):
    print(st + Beautiful_Timestamp (), colors.RED + ' [FAILED]  ' + colors.END, str, end = en)
    return (f"{Beautiful_Timestamp ()} [FAILED] {str}")

def success (str, st = "", en = "\n"):
    print(st + Beautiful_Timestamp (), colors.GREEN + ' [SUCCESS] ' + colors.END, str, end = en)
    return (f"{Beautiful_Timestamp ()} [SUCCESS] {str}")

def inform(str, st = "", en = "\n"):
    print(st + Beautiful_Timestamp (), colors.BLUE + ' [INFORM]  ' + colors.END, str, end = en)
    return (f"{Beautiful_Timestamp ()} [INFORM] {str}")

def warn(str, st = "", en = "\n"):
    print(st + Beautiful_Timestamp (), colors.YELLOW + ' [ WARN ]  ' + colors.END, str, end = en)
    return (f"{Beautiful_Timestamp ()} [WARN] {str}")

def pr(str, st = "", en = "\n"):
    print(st + Beautiful_Timestamp (),' [PRINT]   ' , str)
    return (f"{Beautiful_Timestamp ()} [PRINT] {str}")

def test(str, st = "", en = "\n"):
    print(st + colors.VIOLET + f"{Beautiful_Timestamp ()}  [ TEST ]  " + colors.END, str, end = en)
    return (f"{Beautiful_Timestamp ()} [TEST] {str}")
