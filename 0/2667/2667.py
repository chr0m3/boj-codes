map_size = 0
home_map = list()


def dfs(x: int, y: int, i: int):
    global map_size
    global home_map

    home_map[y][x] = -i

    if y > 0 and home_map[y-1][x] == 1:
        dfs(x, y-1, i)

    if x < (map_size - 1) and home_map[y][x+1] == 1:
        dfs(x+1, y, i)

    if y < (map_size - 1) and home_map[y+1][x] == 1:
        dfs(x, y+1, i)

    if x > 0 and home_map[y][x-1] == 1:
        dfs(x-1, y, i)


def main():
    global map_size
    global home_map

    num_component = 0

    map_size = int(input())

    for i in range(0, map_size):
        home_map.append(list(map(int, list(input()))))

    for y in range(0, map_size):
        for x in range(0, map_size):
            if home_map[y][x] == 1:
                num_component += 1
                dfs(x, y, num_component)

    print(num_component)

    num_element_list = list()
    for i in range(1, num_component+1):
        count = 0
        for y in range(0, map_size):
            for x in range(0, map_size):
                if home_map[y][x] == -i:
                    count += 1
        num_element_list.append(count)
    num_element_list.sort()

    for i in num_element_list:
        print(i)


if __name__ == '__main__':
    main()
