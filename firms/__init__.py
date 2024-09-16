import numpy as np

class firm:
    def __init__(self, recept, product, maintainance=0):
        self.recept=recept
        self.product=product
        self.money=0
        self.maintainance=maintainance

    def produce(self, wage, prices):

        omahind=self.recept.calcomahind(prices)

        if not omahind<prices[self.product] or wage>=self.recept.alfa*(prices[self.product]-omahind):
            return 0

        labour=self.recept.alfa*(prices[self.product]-omahind)/wage-1

        return self.recept.alfa*np.log(labour+1)

    def process_cycle(self, market, lmarket):
        produced=self.produce(lmarket.wage, market.prices)
        for g in range(len(market.prices)):
            market.demands[g]+=self.recept.materials[g]*produced/self.recept.inputtech
        market.supply[self.product]+=produced
        if produced!=0:
            lmarket.demand+=(market.prices[self.product]-self.recept.calcomahind(market.prices))/lmarket.wage-1


    def getomahind(self, prices):
        return self.recept.calcomahind(prices)


class recept:
    def __init__(self, good, alfa, inputtech,  materials):
        self.good=good
        self.alfa=alfa
        self.materials=materials
        self.inputtech=inputtech

    def calcomahind(self, prices):
        omahind=0
        for good in range(len(self.materials)):
            omahind+=self.materials[good]/self.inputtech*prices[good]
        return omahind

    def calcmargin(self, prices):
        return (prices[self.good]-self.calcomahind(prices))