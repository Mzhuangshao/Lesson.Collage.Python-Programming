# def test(a, b, c=33, *args, **kwargs):
#     print(a, b, c, args, kwargs)


# test(1, 2)
# test(1, 2, 3)
# test(1, 2, 3, 4)
# test(1, 2, 3, 4, e=5)

# print((lambda x, y=1: x if x > y else y)(x=5, y=3))
def many_param(num_one, num_two, *args):
    print(args)
many_param(11, 22, 33, 44, 55)