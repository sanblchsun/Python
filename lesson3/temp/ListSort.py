
ls = [4,2,5,1,3]
ls.sort(reverse=1)
print(ls)

def insert_sort(b):
    """сортировка списка  вставками"""
    n = len(b)
    for k in range(1,n):
        while k > 0 and b[k - 1] > b[k]:
            b[k], b[k - 1] = b[k - 1], b[k]
            k -= 1

def bubble_sort(b):
    """сортировка списка методом пузырька"""
    n = len(b)
    for bypass in range(1, n):
        for k in range(n-bypass):
            if b[k] > b[k + 1]:
                b[k], b[k + 1] = b[k + 1], b[k]

def choise_sort(b):
    """сортировка списка методом выбором"""
    n = len(b)
    for pos in range(n-1):
        for k in range(pos+1, n):
            if b[k] < b[pos]:
                b[k], b[pos] = b[pos], b[k]

def Count_sort(b):
    """сортировка подсчетом"""
    if check(b):
        list_counter = [0] * 10
        for element in b:
            for pos_counter in range(len(list_counter)):
                if element==pos_counter:
                    list_counter[pos_counter] += 1
        b.clear()
        for it in range(len(list_counter)):
            for it1 in range(list_counter[it]):
                b.append(it)


def check(x):
    for i in x:
        if not isinstance(i, int) or i > 9:
            raise ValueError("Value Error or value > 9")
            return False
    return True


def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__)

    print("testcase #1: ", end="")
    a = [4,2,5,1,3]
    a_sorted = [1,2,3,4,5]
    sort_algorithm(a)
    # if a == a_sorted:
    #     print('ok')
    # else:
    #     print("FAIL")
    print("OK" if a==a_sorted else "FAILE")

    print("testcase #2: ", end="")
    a = list(range(10,20)) + list(range(10))
    a_sorted = list(range(20))
    sort_algorithm(a)
    print("OK" if a==a_sorted else "FAILE")

    print("testcase #3: ", end="")
    a = [4,2,4,1,3]
    a_sorted = [1,2,3,4,4]
    sort_algorithm(a)
    print("OK" if a==a_sorted else "FAILE")

def test_sort_count(sort_algorithm):
    print('Тестируем длинный список: ', sort_algorithm.__doc__)

    a = [1,2,3,6,4,6,5,4,6,5,1,3,1,6,5,4,6,5,4,6,
         5,4,6,5,4,6,5,4,6,4,9,8,7,1,1,3,3,2,9,0]
    a_sorted = a.copy()
    a_sorted.sort()
    sort_algorithm(a)
    print("OK" if a==a_sorted else "FAILE")

if __name__== "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
    test_sort_count(Count_sort)
