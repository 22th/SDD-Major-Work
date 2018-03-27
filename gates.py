class LogicGates:

    @staticmethod
    def And(A,B):
        if A == 1 and B == 1:
            return 1
        else:
            return 0

    @staticmethod
    def Or(A,B):
        if A == 1 or B == 1:
            return 1
        elif A == 0 and B == 0:
            return 0

    @staticmethod
    def Nor(A,B):
        A = LogicGates.NOT(A)
        B = LogicGates.NOT(B)
        if A == 1 or B == 1:
            return 1
        elif A == 0 and B == 0:
            return 0

    @staticmethod
    def Nand(A,B):
        A = LogicGates.NOT(A)
        B = LogicGates.NOT(B)
        if A == 1 and B == 1:
            return 0
        elif A == 0 or B == 0:
            return 1

    @staticmethod
    def Xor(A,B):
        if A == 1 and B == 0 or A == 0 and B == 1:
            return 1
        if A == 0 and B == 0:
            return 0
        if A == 1 and B == 1:
            return 0

    @staticmethod
    def Not(A):
        if A == 1:
            return 0
        elif A == 0:
            return 1