# repetition.py
def main():
    pass
    inphw=input().split()
    inp=input().split()
    lis1=list(inphw)
    lis2=list(inp)
    if (lis1[1] in lis2):
        k=lis2.count(lis1[1])
        print(k)
    else:
        print(0)

if __name__ == '__main__':
    main()
