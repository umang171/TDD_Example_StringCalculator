class stringCalculator:
    def add(self, str):
        if(len(str.strip()) == 0):
            return 0
        elif(len(str.strip()) == 1):
            return int(str.strip())
        elif(str.strip().count(",") >= 1 or str.strip().count("\n") >= 1):
            str = str.replace("\n", ",")
            lst = str.split(",")
            lst = list(map(lambda x: int(x), lst))
            return sum(lst)
