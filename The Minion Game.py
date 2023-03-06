vowels = 'AEIOU'
def minion_game(string):
    kevin = 0
    n =len(string)
    total = int((n*(n+1))/2)
    for i in range(n):
        if string[i] in vowels:
            kevin = kevin + (n-i)
    stuart = total - kevin
    
    if stuart == kevin:
        print ('Draw')
    elif stuart > kevin:
        print(f'Stuart {stuart}')
    else:
        print(f'Kevin {kevin}')
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
