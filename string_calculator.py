class stringCalculator:
    def add(self, str):
        if(len(str.strip()) == 0):
            return 0
        elif(len(str.strip()) == 1):
            return int(str.strip())
