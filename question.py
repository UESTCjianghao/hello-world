import copy


def test_c():
    names = 'abcde'
    names_test_copy = copy.copy(names)

    # names[0][0] = 0
    # names_test_copy[0][0] = 0

    # names[0] = 0
    print('names', names, 'names_test_copy', names_test_copy, 'names的内存地址', id(names), 'names_test_copy的内存地址',
          id(names_test_copy))


if __name__ == '__main__':
    test_c()
