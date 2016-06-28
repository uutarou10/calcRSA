# coding: UTF-8
import random

class calcRSA:
    def __init__(self,m,p,q):
        if CalcRSA.isPrimaryNum(p):
            self.p = p

        if CalcRSA.isPrimaryNum(q):
            self.q = q

        self.m = m

    @staticmethod
    def isPrimaryNum(num):
        """素数判定。"""
        i = 2
        result = True
        while num != i:
            if num % i == 0:
                result = False
                break

            i += 1

        return result

    @staticmethod
    def gcd(a,b):
        """GCD(最大公約数)を求める"""
        while b:
            a,b = b,a % b

        return a

    @staticmethod
    def lcm(a,b):
        """LCM(最小公倍数)を求める"""
        return a * b // CalcRSA.gcd(a,b)

    def n(self):
        """nを求める。n=pq"""
        return self.p * self.q

    def lamdaN(self):
        return Calc.lcm(self.p-1,self.q-1)

    def e(self):
        """eを求める。（ランダムで決定しようと思ったけど最小のやつを使うことにした）1は使わない。"""
        n = CalcRSA.lamdaN(self)
        e = 2
        list = []#eの候補になりうる数値の配列

        while e < n:
            if CalcRSA.gcd(e,n) == 1:
                list.append(e)

            e += 1

        return list[0]
        #return list[random.randint(0,len(list)-1)]
        #return list

    def d(self):
        n = CalcRSA.lamdaN(self)
        e = CalcRSA.e(self)

        d = 1

        while True:
            if (d * e - 1) % n == 0:
                break

            d += 1

        return d

    def c(self):
        return self.m ** CalcRSA.e(self) % CalcRSA.n(self)


