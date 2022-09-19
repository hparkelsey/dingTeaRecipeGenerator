# input variables

drinkName = (input("Name of drink? ")).lower()
sugarLevel = (input("Sugar level: R, L, H, S, or N? ")).lower()
iceLevel = (input("Ice Level: R, L, H, S, or N? ")).lower()
size = (input("Size: L or M? ")).lower()
toppingCount = int(input("How many toppings? "))

# object init parameters: (drinkName, sugarLevel, iceLevel, size, toppingCount)

isFlavored = False
noIce = False

if iceLevel == "N":
    noIce = True

sugarTable = [
             [1.5, 1.0, 0.8, 0.4],
             [1.0, 0.8, 0.5, 0.3],
             [0.8, 0.5, 0.4, 0.2],
             [0.5, 0.3, 0.2, 0.1]
                                ]

r = 0
c = 0

sugar = sugarTable[r][c]

base = 0
baseType = 0
creamer = 0
jamOrSyrup = 0
espresso = 0
powder = 0

freshTea = ["green tea", "oolong tea", "black tea"]
flavorTea = ["peach green tea", "peach black tea", "passion fruit green tea", "passion fruit black tea",
             "strawberry green tea", "strawberry black tea", "lychee green tea", "lychee black tea",
             "mango green tea", "mango black tea", "honey green tea", "honey black tea", "pineapple green tea",
             "pineapple black tea", "kiwi green tea", "kiwi black tea", "winter melon tea", "winter melon green tea"
             "kumquat tea", "kumquat lemon ice tea", "top fruit", "guava green tea", "apple green tea",
             "blueberry green tea", "kumquat pineapple green tea", "grapefruit green tea", "grapefruit black tea"]
fruitJuice = ["aloe vera kiwi juice", "aloe vera honey juice", "aloe vera passion fruit juice", "aloe vera peach juice",
              "aloe vera lychee juice", "aloe vera grapefruit juice"]
slush = ["taro slush", "matcha slush", "strawberry slush", "mango slush", "passion fruit slush",
         "strawberry yakult slush", "hokkaido coffee slush", "signature boba milk tea slush", "pineapple slush"]
milkTea = ["signature milk tea", "jasmine green milk tea", "oolong milk tea", "taro milk tea", "thai milk tea",
           "matcha milk tea", "black sesame milk tea", "chocolate milk tea", "honey milk tea", "strawberry milk tea"
           "lychee milk tea", "winter melon green milk tea", "winter melon milk tea", "peach milk tea",
           "mango milk tea", "passion fruit milk tea", "brown sugar milk tea", "hazelnut milk tea", "vanilla milk tea",
           "hokkaido black milk tea", "hokkaido oolong milk tea", "guava green milk tea", "blueberry green milk tea",
           "dalgona coffee milk tea"]
yakultYogurt = ["green tea yakult", "passion fruit yakult", "lychee yakult", "mango yakult", "peach yakult",
                "strawberry yakult", "grapefruit yakult", "green tea yogurt", "passion fruit yogurt",
                "lychee yogurt", "mango yogurt", "peach yogurt", "strawberry yogurt", "grapefruit yogurt"]
coffee = ["condensed milk coffee latte", "vanilla coffee latte", "hazelnut coffee latte", "brown sugar coffee latte",
          "vietnamese coffee"]
# vietnamese coffee only available in size m
latte = ["black tea latte", "jasmine green tea latte", "oolong latte", "matcha Latte", "taro Latte",
         "taro jasmine green latte", "monster boba latte", "thai tea latte", "black sesame latte"]
hotDrink = ["ginger tea", "longan tea", "ginger longan tea", "ginger milk tea", "longan milk tea"]
taroMash = ["taro green milk tea", "taro boba green milk tea", "taro mix burnt cream"]
honeySweet = ["strawberry honey", "kiwi honey", "passion fruit honey"]
# honeySweet only available in size l
seasonalDrink = ["strawberry matcha"]

flavors = ["strawberry", "passion fruit", "peach", "lychee", "mango", "pineapple", "kiwi", "kumquat", "apple",
           "blueberry", "grapefruit", "guava"]

for i in flavors:
    if i in drinkName:
        isFlavored = True
        break
    else:
        isFlavored = False


# super class
class Tea:

    # instance fields

    sugar = sugarTable[r][c]
    base = 0
    baseType = 0
    creamer = 0
    jamOrSyrup = 0
    espresso = 0
    powder = 0

    def __init__(self, drinkName, sugarLevel, iceLevel, size, toppingCount):
        self.drinkName = drinkName
        self.sugarLevel = sugarLevel
        self.iceLevel = iceLevel
        self.size = size
        self.toppingCount = toppingCount

    def getSugar(self):
        if isFlavored and (drinkName != "kumquat lemon ice tea"):
            c = 2
        else:
            c = 0
        r = 0
        # size adjustment
        if size == "m":
            c += 1
        # number of toppings adjustment
        if c + toppingCount <= 3:
            c += toppingCount
        else:
            c = 3
        # sugar level adjustments
        if sugarLevel == "r":
            r = 0
        elif sugarLevel == "l":
            r = 1
        elif sugarLevel == "h":
            r = 2
        elif sugarLevel == "s":
            r = 3
        # locate sugar
        sugar = sugarTable[r][c]
        # no ice adjustment
        if noIce:
            if size == "l":
                sugar += 0.4
            else:
                sugar += 0.2
        # no sugar adjustment
        if sugarLevel == "n":
            sugar = 0
        # keyword exceptions
        if "honey" in drinkName:
            sugar = 0
        elif "winter melon" in drinkName:
            sugar = 0
        elif "brown sugar" in drinkName:
            sugar = 0
        elif "vanilla" in drinkName:
            sugar = 0
        elif "hazelnut" in drinkName:
            sugar = 0
        elif "hokkaido" in drinkName:
            sugar = 0
        elif "top fruit" in drinkName:
            sugar = 0
        if drinkName == "thai tea latte":
            sugar = 0
        if drinkName == "guava green tea":
            if size == "l":
                sugar = 0.4
            else:
                sugar = 0
        if sugar != 0:
            print("Sugar: " + str(sugar))

    def getBase(self):
        if ((drinkName in latte) and (drinkName != "thai tea latte")) or (drinkName in yakultYogurt):
            base = 150
        else:
            base = 200
        if iceLevel == "l":
            base += 50
        elif iceLevel == "h":
            base += 100
        elif iceLevel == "s":
            base += 150
        elif iceLevel == "n":
            base += 200
        if toppingCount != 0:
            base -= 50 * toppingCount
        if ((drinkName in latte) and (drinkName != "thai tea latte")) or (drinkName in yakultYogurt):
            if base < 150:
                base = 150
        else:
            if base < 200:
                base = 200
        if base > 300:
            base = 300
        print("Base: " + str(base) + "cc")

    def getBaseType(self):
        baseType = "water"
        if "green" in drinkName:
            baseType = "green tea"
        elif "oolong" in drinkName:
            baseType = "oolong tea"
        elif "black" in drinkName:
            baseType = "black tea"
        print("Base type: " + str(baseType))

    def getJamOrSyrup(self):
        if size == "l":
            jamOrSyrup = 2
        else:
            jamOrSyrup = 1.5
        if drinkName == "ginger longan tea":
            print("half jam/syrup ginger, other half longan")
        print("Jam/Syrup: " + str(jamOrSyrup) + "oz. Jam after ice, syrup before ice!")

    def getCreamer(self):
        if size == "l":
            creamer = 4
        else:
            creamer = 3
        print("Creamer: " + str(creamer) + " scoops")

    def getPowder(self):
        if "taro" in drinkName:
            if size == "l":
                powder = 3
            else:
                powder = 2
        elif "chocolate" in drinkName:
            if size == "l":
                powder = 3
            else:
                powder = 2
        elif "matcha" in drinkName:
            if size == "l":
                powder = 3
            else:
                powder = 2
        elif "black sesame" in drinkName:
            if size == "l":
                powder = 3
            else:
                powder = 2
        elif "thai" in drinkName:
            if size == "l":
                powder = 4
            else:
                powder = 3
        else:
            powder = 0
        if powder != 0:
            print("Powder: " + str(powder) + " scoops")

    def getEspresso(self):
        if drinkName == "vietnamese coffee":
            espresso = 4
        else:
            if size == "l":
                espresso = 2
            else:
                espresso = 1.5
        print("Espresso: " + str(espresso) + "oz")


# subclasses
class FreshTea(Tea):
    def getBase(self):
        base = 250
        if iceLevel == "l":
            base += 50
        elif iceLevel == "h":
            base += 100
        elif iceLevel == "s":
            base += 150
        elif iceLevel == "n":
            base += 200
        if toppingCount != 0:
            base -= 50 * toppingCount
        if base < 250:
            base = 250
        if base > 300:
            base = 300
        print("Base: " + str(base) + "cc")


class FlavorTea(Tea):
    def getBaseType(self):
        baseType = "water"
        if ("green" in drinkName) or (drinkName == "top fruit") or (drinkName == "kumquat lemon ice tea"):
            baseType = "green tea"
        elif "oolong" in drinkName:
            baseType = "oolong tea"
        elif "black" in drinkName:
            baseType = "black tea"
        elif (drinkName == "kumquat tea") or (drinkName == "winter melon tea"):
            baseType = "water"
        print("Base type: " + str(baseType))

    def getJamOrSyrup(self):
        if drinkName == "top fruit":
            jamOrSyrup = 0
            if size == "l":
                print("4 scoops top fruit")
            else:
                print("3 scoops top fruit")
        elif drinkName == "guava green tea":
            if size == "l":
                jamOrSyrup = 2.5
            else:
                jamOrSyrup = 2
        elif drinkName == "blueberry green tea":
            if size == "l":
                jamOrSyrup = 2
                print("1oz lemon juice")
            else:
                jamOrSyrup = 1.5
                print("0.5oz lemon juice")
        elif drinkName == "kumquat pineapple green tea":
            if size == "l":
                jamOrSyrup = 2
                print("1.5oz kumquat")
            else:
                jamOrSyrup = 1.5
                print("1oz kumquat")
        elif drinkName == "kumquat lemon ice tea":
            jamOrSyrup = 0
            if size == "l":
                print("2oz lemon juice and 1oz kumquat")
            else:
                print("1.5oz lemon juice and 0.5oz kumquat")
        else:
            if size == "l":
                jamOrSyrup = 2
            else:
                jamOrSyrup = 1.5
        if jamOrSyrup != 0:
            print("Jam/Syrup: " + str(jamOrSyrup) + "oz. Jam after ice, syrup before ice!")

    def getExtra(self):
        if (drinkName == "grapefruit green tea") or (drinkName == "grapefruit black tea"):
            if size == "l":
                print("2 plums; filter out")
            else:
                print("1 plum; filter out")
        elif drinkName == "guava green tea":
            if size == "l":
                print("2 plums")
            else:
                print("1 plum")
        elif drinkName == "kumquat lemon ice tea":
            if size == "l":
                print("2 plums and 2 fresh kumquats")
            else:
                print("1 plum and 1 fresh kumquat")


class Slush(Tea):
    def getSugar(self):
        if size == "l":
            c = 0
        else:
            c = 1
        r = 0
        # sugar level adjustments
        if sugarLevel == "r":
            r = 0
        elif sugarLevel == "l":
            r = 1
        elif sugarLevel == "h":
            r = 2
        elif sugarLevel == "s":
            r = 3
        # locate sugar
        sugar = sugarTable[r][c]
        # no sugar adjustment
        if sugarLevel == "n":
            sugar = 0
        # exceptions
        if (drinkName == "strawberry yakult slush") or (drinkName == "hokkaido coffee slush"):
            sugar = 0
        if drinkName == "signature boba milk tea slush":
            if size == "l":
                sugar = 2.5
            else:
                sugar = 2
        if sugar != 0:
            print("Sugar: " + str(sugar))

    def getBase(self):
        print("1.5 cup ice")
        # base
        if (drinkName == "strawberry yakult slush") or (drinkName == "hokkaido coffee slush"):
            base = 0
        elif drinkName == "signature boba milk tea slush":
            base = 200
        else:
            base = 100
        # base type (combined methods)
        baseType = "water"
        if drinkName == "strawberry yakult slush":
            if size == "l":
                print("2 yakults")
            else:
                print("1 yakult")
        elif drinkName == "signature boba milk tea slush":
            print("comes with 1 scoop black boba")
            baseType = "black tea"
        if base != 0:
            print("Base: " + str(base) + "cc")
            print("Base type: " + str(baseType))

    def getCreamer(self):
        if (drinkName == "taro slush") or (drinkName == "hokkaido coffee slush"):
            if size == "l":
                creamer = 2
            else:
                creamer = 1
        elif drinkName == "matcha slush":
            if size == "l":
                creamer = 3
            else:
                creamer = 2
        elif drinkName == "signature boba milk tea slush":
            if size == "l":
                creamer = 5
            else:
                creamer = 4
        else:
            creamer = 0
        if creamer != 0:
            print("Creamer: " + str(creamer) + " scoops")

    def getJamOrSyrup(self):
        if drinkName == "taro slush":
            jamOrSyrup = 0
        elif drinkName == "matcha slush":
            jamOrSyrup = 0
        elif drinkName == "signature boba milk tea slush":
            jamOrSyrup = 0
        elif drinkName == "strawberry yakult slush":
            if size == "l":
                jamOrSyrup = 4
            else:
                jamOrSyrup = 3
        else:
            if size == "l":
                jamOrSyrup = 3
            else:
                jamOrSyrup = 2
        if jamOrSyrup != 0:
            print("Jam/Syrup: " + str(jamOrSyrup) + "oz. Jam after ice, syrup before ice!")

    def getEspresso(self):
        if drinkName == "hokkaido coffee slush":
            if size == "l":
                espresso = 4
            else:
                espresso = 3
        else:
            espresso = 0
        if espresso != 0:
            print("Espresso: " + str(espresso) + "oz")

    def getPowder(self):
        if drinkName == "taro slush":
            if size == "l":
                powder = 3
            else:
                powder = 2
        elif drinkName == "matcha slush":
            if size == "l":
                powder = 4
            else:
                powder = 3
        else:
            powder = 0
        if powder != 0:
            print("Powder: " + str(powder) + " scoops")


class MilkTea(Tea):
    def getSugar(self):
        if isFlavored:
            if drinkName == "blueberry green milk tea":
                c = 1
            else:
                c = 2
        else:
            c = 0
        if drinkName == "matcha milk tea":
            c = 2
        r = 0
        # size adjustment
        if size == "m":
            c += 1
        # number of toppings adjustment
        if c + toppingCount <= 3:
            c += toppingCount
        else:
            c = 3
        # sugar level adjustments
        if sugarLevel == "r":
            r = 0
        elif sugarLevel == "l":
            r = 1
        elif sugarLevel == "h":
            r = 2
        elif sugarLevel == "s":
            r = 3
        # locate sugar
        sugar = sugarTable[r][c]
        # no ice adjustment
        if noIce:
            if size == "l":
                sugar += 0.4
            else:
                sugar += 0.2
        # no sugar adjustment
        if sugarLevel == "n":
            sugar = 0
        if "honey" in drinkName:
            sugar = 0
        elif "winter melon" in drinkName:
            sugar = 0
        elif "brown sugar" in drinkName:
            sugar = 0
        elif "vanilla" in drinkName:
            sugar = 0
        elif "hazelnut" in drinkName:
            sugar = 0
        elif "hokkaido" in drinkName:
            sugar = 0
        elif "top fruit" in drinkName:
            sugar = 0
        if drinkName == "guava green milk tea":
            sugar = 0
        if drinkName == "thai milk tea":
            if size == "l":
                sugar = 0.2
            else:
                sugar = 0.1
        if sugar != 0:
            print("Sugar: " + str(sugar))

    def getBaseType(self):
        baseType = "black tea"
        if "green" in drinkName:
            baseType = "green tea"
        elif "oolong" in drinkName:
            baseType = "oolong tea"
        elif drinkName == "taro milk tea":
            baseType = "hot water"
        elif drinkName == "matcha milk tea":
            baseType = "hot water"
        elif drinkName == "black sesame milk tea":
            baseType = "hot water"
        elif drinkName == "chocolate milk tea":
            baseType = "hot water"
        elif drinkName == "winter melon milk tea":
            baseType = "hot water"
        print("Base type: " + str(baseType))

    def getCreamer(self):
        if (drinkName == "taro milk tea") or (drinkName == "chocolate milk tea"):
            if size == "l":
                creamer = 2
            else:
                creamer = 1
        elif (drinkName == "matcha milk tea") or (drinkName == "black sesame milk tea"):
            if size == "l":
                creamer = 3
            else:
                creamer = 2
        elif drinkName == "thai milk tea":
            if size == "l":
                creamer = 1
            else:
                creamer = 0.5
        elif drinkName == "guava green milk tea":
            if size == "l":
                creamer = 2
            else:
                creamer = 1.5
        else:
            if size == "l":
                creamer = 4
            else:
                creamer = 3
        print("Creamer: " + str(creamer) + " scoops")

    def getJamOrSyrup(self):
        if drinkName == "signature milk tea":
            jamOrSyrup = 0
        elif drinkName == "dalgona coffee milk tea":
            jamOrSyrup = 0
        elif drinkName == "jasmine green milk tea":
            jamOrSyrup = 0
        elif drinkName == "oolong milk tea":
            jamOrSyrup = 0
        elif drinkName == "taro milk tea":
            jamOrSyrup = 0
        elif drinkName == "thai milk tea":
            jamOrSyrup = 0
        elif drinkName == "matcha milk tea":
            jamOrSyrup = 0
        elif drinkName == "black sesame milk tea":
            jamOrSyrup = 0
        elif drinkName == "chocolate milk tea":
            jamOrSyrup = 0
        elif drinkName == "guava green milk tea":
            if size == "l":
                jamOrSyrup = 3
            else:
                jamOrSyrup = 2.5
        else:
            if size == "l":
                jamOrSyrup = 2
            else:
                jamOrSyrup = 1.5
        if jamOrSyrup != 0:
            print("Jam/Syrup: " + str(jamOrSyrup) + "oz. Jam after ice, syrup before ice!")

    def getDalgona(self):
        print("remember, dalgona counts as a topping (for sugar). Don't forget 1 dalgona scoop!")


class YakultYogurt(Tea):
    # base = 150 is already handled by parent method
    def getSugar(self):
        if (drinkName == "green tea yakult") or (drinkName == "green tea yogurt"):
            c = 0
            r = 0
            # size adjustment
            if size == "m":
                c += 1
            # number of toppings adjustment
            if c + toppingCount <= 3:
                c += toppingCount
            else:
                c = 3
            # sugar level adjustments
            if sugarLevel == "r":
                r = 0
            elif sugarLevel == "l":
                r = 1
            elif sugarLevel == "h":
                r = 2
            elif sugarLevel == "s":
                r = 3
            # locate sugar
            sugar = sugarTable[r][c]
            # no ice adjustment
            if noIce:
                if size == "l":
                    sugar += 0.4
                else:
                    sugar += 0.2
            # no sugar adjustment
            if sugarLevel == "n":
                sugar = 0
        else:
            sugar = 0
        if sugar != 0:
            print("Sugar: " + str(sugar))

    def getYakult(self):
        if "yakult" in drinkName:
            if size == "l":
                print("2 Yakults")
            else:
                print("1 Yakult")
        elif "yogurt" in drinkName:
            print("1 Yakult")

    def getCreamer(self):
        creamer = 0
        if "yogurt" in drinkName:
            if size == "l":
                creamer = 3
            else:
                creamer = 2
        if creamer != 0:
            print("Creamer: " + str(creamer) + " scoops")

    def getBaseType(self):
        baseType = "water"
        if "yakult" in drinkName:
            baseType = "water"
        elif "yogurt" in drinkName:
            baseType = "hot water"
        if (drinkName == "green tea yakult") or (drinkName == "green tea yogurt"):
            baseType = "green tea"
        print("Base type: " + str(baseType))


class Coffee(Tea):
    def getJamOrSyrup(self):
        if drinkName == "vietnamese coffee":
            jamOrSyrup = 2
        else:
            if size == "l":
                jamOrSyrup = 1.5
            else:
                jamOrSyrup = 1
        print("Jam/Syrup: " + str(jamOrSyrup) + "oz. Jam after ice, syrup before ice!")


class Latte(Tea):
    # base = 150 is already handled by parent method
    def getPowder(self):
        if ("taro" in drinkName) or ("chocolate" in drinkName) or ("matcha" in drinkName):
            if size == "l":
                powder = 3
            else:
                powder = 2
        elif "black sesame" in drinkName:
            if size == "l":
                powder = 3
            else:
                powder = 2
        elif "thai" in drinkName:
            if size == "l":
                powder = 4
            else:
                powder = 3
        else:
            powder = 0
        if powder != 0:
            print("Powder: " + str(powder) + " scoops")

    def getBaseType(self):
        baseType = "hot water"
        if "green" in drinkName:
            baseType = "green tea"
        elif "oolong" in drinkName:
            baseType = "oolong tea"
        elif (("black" in drinkName) or ("thai" in drinkName)) and (drinkName != "black sesame latte"):
            baseType = "black tea"
        print("100cc of milk")
        print("Base type: " + str(baseType))


class HotDrink(Tea):
    def getCreamer(self):
        if (drinkName == "ginger milk tea") or (drinkName == "longan milk tea"):
            if size == "l":
                creamer = 4
            else:
                creamer = 3
        else:
            creamer = 0
        if creamer != 0:
            print("Creamer: " + str(creamer) + " scoops")

    def getBaseType(self):
        print("Base: 80% of hot water")


class TaroMash(Tea):
    def getBaseType(self):
        print("Base type: green tea")

    def getTaroMash(self):
        if size == "l":
            print("4 scoops of taro mash")
        else:
            print("3 scoops of taro mash")
        # topping specification:
        if drinkName == "taro boba green milk tea":
            print("comes with boba!")
        elif drinkName == "taro mix burnt cream":
            print("comes with boba and sea cream creme brulee!")


class HoneySweet(Tea):
    def getJamOrSyrup(self):
        print("1.5oz honey")
        print("Jam/Syrup: 1oz. Jam after ice, syrup before ice!")


class SeasonalDrink:
    def getSeasonalDrink(self):
        print("only comes in a large")
        print("1.5oz strawberry")
        base = 200
        if iceLevel == "l":
            base += 50
        elif iceLevel == "h":
            base += 100
        elif iceLevel == "s":
            base += 150
        elif iceLevel == "n":
            base += 200
        if toppingCount != 0:
            base -= 50 * toppingCount
        if base < 200:
            base = 200
        if base > 300:
            base = 300
        print("base: " + str(base) + "cc of hot water")
        print("3 scoops matcha powder")
        print("comes with sea cream")


# objects + method calls
if drinkName in freshTea:
    drink = FreshTea(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getSugar()
    drink.getBase()
    drink.getBaseType()
elif drinkName in flavorTea:
    drink = FlavorTea(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getSugar()
    drink.getBase()
    drink.getBaseType()
    drink.getJamOrSyrup()
    drink.getExtra()
elif drinkName in fruitJuice:
    drink = Tea(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getSugar()
    drink.getBase()
    drink.getBaseType()
    drink.getJamOrSyrup()
    print("Remember! Aloe Vera is a default topping! Does not affect sugar level!")
elif drinkName in slush:
    drink = Slush(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getSugar()
    drink.getBase()
    drink.getCreamer()
    drink.getPowder()
    drink.getJamOrSyrup()
    drink.getEspresso()
elif drinkName in milkTea:
    drink = MilkTea(drinkName, sugarLevel, iceLevel, size, toppingCount)
    if drinkName == "dalgona coffee milk tea":
        drink.getDalgona()
    drink.getSugar()
    drink.getBase()
    drink.getBaseType()
    drink.getCreamer()
    drink.getPowder()
    drink.getJamOrSyrup()
elif drinkName in yakultYogurt:
    drink = YakultYogurt(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getSugar()
    drink.getYakult()
    drink.getBase()
    drink.getBaseType()
    drink.getCreamer()
    drink.getJamOrSyrup()
elif drinkName in coffee:
    drink = Coffee(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getEspresso()
    drink.getJamOrSyrup()
elif drinkName in latte:
    drink = Latte(drinkName, sugarLevel, iceLevel, size, toppingCount)
    if drinkName == "monster boba latte":
        if size == "l":
            print("2 scoops syrup")
        else:
            print("1.5 scoops of syrup")
        print("comes with 1 scoop black boba")
        print("fill with milk of choice")
    else:
        drink.getSugar()
        drink.getBase()
        drink.getBaseType()
        drink.getPowder()
elif drinkName in hotDrink:
    drink = HotDrink(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getBaseType()
    drink.getCreamer()
    drink.getJamOrSyrup()
elif drinkName in taroMash:
    drink = TaroMash(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getSugar()
    drink.getBase()
    drink.getBaseType()
    drink.getTaroMash()
    drink.getCreamer()
elif drinkName in honeySweet:
    drink = HoneySweet(drinkName, sugarLevel, iceLevel, size, toppingCount)
    drink.getJamOrSyrup()
    drink.getBase()
    drink.getBaseType()
elif drinkName in seasonalDrink:
    drink = SeasonalDrink()
    drink.getSeasonalDrink()
else:
    print("drink name invalid")


