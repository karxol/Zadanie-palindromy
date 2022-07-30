
def czyPalindrom(x):
    x = x.lower().replace(" ", "")
    n = len(x)
    for i in range(n-1):
        if x[i] != x[n - 1 - i]:
            return False
    return True

print("Podaj słowo: ")
s1 = input()
print("podane słowo" +(" jest" if(czyPalindrom(s1)) else " nie jest ") +  " palindromem")