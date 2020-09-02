def user_input():
    n = int(input("Antal värden att mata in: "))
    d_seq = [None]*n
    q_seq = [None]*n

    for i in range(n):
        print("Ange värde för index", i)
        d_seq[i] = float(input("d? "))
        q_seq[i] = float(input("q? "))
    
    return d_seq, q_seq

def calculate(d_vals, q_vals):
    total = 0
    n = len(d_vals)

    for i in range(n):
        total = (total + d_vals[i])*q_vals[i]

    return total
    
def main():
    done = False

    while not done:
        d, q = user_input()
        print("Beräknad summa: ", calculate(d,q))
        done = input("Är du klar? (J/N) ") in ("J", "j", "y", "Y")

main()
