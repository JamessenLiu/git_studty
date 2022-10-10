
import sys


def fib(n):

    a, b, counter = 0, 1, 0
    while counter < n:
        yield a
        a, b = b, a + b
        counter += 1


f = fib(999)
print(sys.getsizeof(f))


# master / main 主分支  -> 生产环境
# staging / testing 测试分支  -> 测试环境
# develop / dev 开发分支  -> 开发环境

# feat/send_email  / feat/num-1 -> 需求分支命名
# fix/email_validation_error -> 修复问题分支命名
# improve/XXX -> 优化分支命名

def get_sum(a, b):
    return a + b
