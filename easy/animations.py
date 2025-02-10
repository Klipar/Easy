class SimpleAnimation:      # / 
    def __init__(self):
        self.char = '|'

    def step(self) -> str:
        if self.char == '/':
            self.char = '-'
            return self.char
        elif self.char == '-':
            self.char = '\\'
            return self.char
        elif self.char == '\\':
            self.char = '|'
            return self.char
        else:
            self.char = '/'
            return self.char
    def show(self) -> str:
        return self.char


# bar = LineProgresBar(MaxLength = 50, text = "Loading ", maxWalue = 500, isShowPersent = True, isShowWalue = True)
# ShoveAndUpdate(1)
class LineProgresBar:       # test [=======--------->] [45%] [130/500]
    def __init__(self, MaxLength, text, isShowPersent = False, maxWalue = 0, isShowWalue = False):
        self.MaxLength = MaxLength
        self.curentWalue = 0
        self.maxWalue  = maxWalue

        self.text   = text
        
        self.isShowPersent = isShowPersent
        self.isShowWalue   = isShowWalue

    def ShoveAndUpdate (self, dif_in_walue = 1):
        self.curentWalue += dif_in_walue
        x = int(((self.curentWalue*self.MaxLength)/self.maxWalue))
        
        
        print(self.text,"[", end="")

        for i in range(x):
            print("=", end = "")
        if (x < self.MaxLength):
            print(">", end = "")
            for i in range (self.MaxLength-x):
                print("-", end = "")
        print("]", end="")
        if (self.isShowWalue):
            print(f"  [{self.curentWalue}/{self.maxWalue}]", end = "")
        if (self.isShowPersent):
            print(f"  [{round((self.curentWalue/self.maxWalue*100), 1)}%]", end = "")
        print("\r", end = "")
        if (self.curentWalue == self.maxWalue):
            print()
