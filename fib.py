class FibIterator(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """
        :param n: int, 指明生成数列的前n个数
        """
        self.n = n
        # current用来保存当前生成到数列中的第几个数了
        self.i = 0
        # num1用来保存前前一个数，初始值为数列中的第一个数0
        self.a = 0
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.b = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.i < self.n:
            num = self.b
            self.a, self.b = self.b, self.a + self.b
            self.i += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self


def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        a, b = b, a + b
        i = i + 1
        # 已经通过中间量转换
        print(a)
    return 'done'


def generator_fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        yield b
        a, b = b, a + b
        i = i + 1
    return 'done'


if __name__ == '__main__':
    # fib = FibIterator(10)
    # print(fib)
    # # fib实例化对象，它具有生成器的性质，区别于普通函数的返回包含所有数值的数组
    # # 实际只返回的一个值，构建某种算法推导，实现一边循环一边计数的生成器的机制，
    # for num in fib:
    #     print(num, end=" ")
    f = fib(10)
    print(f)
    # gen_f = generator_fib(10)
    # print(gen_f.__next__())
    # print(gen_f.__next__())
    # print(gen_f.__next__())
    # print(next(generator_fib(1)))
    # print(gen_f)
    # for i in gen_f:
    #     print(i, end=" ")
    # end 循环中默认不换行
    # 调用方式
