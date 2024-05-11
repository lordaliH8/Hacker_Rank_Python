if __name__ == '__main__':
    N = int(input())
    my_arr = []
    for i in range(N):
        commands = input().split()
        commands = [commands[0]] + [int(x) for x in commands[1:]]

        if commands[0] == "insert":
            my_arr.insert(commands[1],commands[2])
        elif commands[0] == "print":
            print(my_arr)
        elif commands[0] == "remove":
            my_arr.remove(commands[1])
        elif commands[0] == "pop":
            my_arr.pop()
        elif commands[0] == "reverse":
            my_arr.reverse()
        elif commands[0] == "sort":
            my_arr.sort()
        elif commands[0] == "append":
            my_arr.append(commands[1])
