import copy


def test_c():
    names1 = ['Amir', 'Barry', 'Cgakes', 'Dao', [11, 22, 33]]
    names1_test_copy = ['Amir', 'Barry', 'Cgakes']
    names2_test_copy = [[11, 22, 33]]
    names2 = names1  # 直接赋值，指向同一个对象
    # 直接赋值，对于可变对象而言，随动，对于不可变对象而言，替换
    names3 = names1[:]  # 切片生成一个新的对象
    names4 = names1.copy()  # 浅拷贝，拷贝父对象，和切片效果一样,
    names1_test_copy4 = names1_test_copy.copy()
    names2_test_copy5 = names2_test_copy.copy()
    names2_test_copy[0][0] = 00
    print(names2_test_copy5, names2_test_copy, id(names2_test_copy5), id(names2_test_copy))
    names5 = copy.deepcopy(names1)  # 深拷贝，拷贝父对象和子对象
    # 深拷贝，结果独立

    # 做修改
    names1[0] = 'fuck'
    names1[-1][0] = 44

    print('', id(names1_test_copy4), id(names1_test_copy))
    print('', id(names2_test_copy5), id(names2_test_copy))
    print('names1', names1, id(names1))
    print('names2', names2, id(names2))
    print('names3', names3, id(names3))
    print('names4', names4, id(names3))
    print('names5', names5, id(names4))


if __name__ == '__main__':
    test_c()
