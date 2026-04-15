def primo(n):
    cont = 0
    for i in range(2,n):
        if n%i==0:
            cont += 1
    if cont > 0:
        return False
    return True

def palindromo(s):
    return s==s[::-1]

palindromo("anitalavalatina")