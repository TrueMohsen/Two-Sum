


def search(dif, l,forbidden_index):
    list_len = len(l)
    res = None
    for j in range(forbidden_index + 1, list_len):
        if (l[j] == dif):
            res = j
    return res

def receive():
    l = list()
    ans = True
    ans_s = 'y'
    reading_option = input("file or keyboard?(f or k)")
    if reading_option =='k' or reading_option=='K':
        while ans:
            item = input("please enter a number:")
            l.append(int(item))
            ans_s = input("Do you want to continue?('Y' or 'N')")
            if (ans_s == 'N' or ans_s == 'n'):
                ans = False
    else:
        with open("bumbers_list") as file_object:
            l=file_object.read()


    return l


def twosum():
    l2 = list()
    s1 = set()
    nums = receive()
    list_len=len(nums)
    target = input("please enter target:")
    target=int(target)
    print(nums)
    for i in range(list_len):
        x = target - int(nums[i])
        index = search(x, nums,i)
        if (index!=None):
            s1.add(i)
            s1.add(index)

    print(list(s1))


if __name__ == '__main__':
    twosum()