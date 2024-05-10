if __name__ == '__main__' :
    x = int(input().strip())
    if x%2 != 0 :
        print("Weird")
    if x%2 == 0  and 2<=x<=5:
        print("Not Weird")
    if x%2 == 0  and 6<=x<=20:
        print("Weird")
    if x%2 == 0 and x>20:
        print("Not Weird")