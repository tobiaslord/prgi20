def main():
    cont = "J"
    while cont != "N":
        a1 = float(input("Ange a1"))
        d = float(input("Ange d"))
        g1 = float(input("Ange g1"))
        q = float(input("Ange q"))
        n = int(input("Ange n"))
        print(comparator(a1, d, g1, q, n))
        done = input("Vill du fortsätta? (J/N)")
        
    
def comparator(a1, d, g1, q, n):
    aritmeticSum = aritmetic(a1, d, n)
    geometricSum = geometric(g1, q, n)
    print("Aritmetic sum: " + str(aritmeticSum))
    print("Geometric sum: " + str(geometricSum))
    if aritmeticSum > geometricSum:
        return "Den aritmetiska summan är störst"
    else:
        return "Den geometriska summan är störst"

def aritmetic(a1, d, n):
    return a1 + d*(n-1)

def geometric(g1, q, n):
    return g1*(q**(n-1))

main()
