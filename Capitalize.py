def solve(s):
    c= ""
    for i in range(0,len(s)):
        if i == 0:
            c = c + (s[i].upper())
        elif s[i-1] == " ":
            c = c + (s[i].upper())
        else:
            c = c + s[i]
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
