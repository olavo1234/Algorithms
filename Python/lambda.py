# fazer pequenas funções anônimas
def fazer_func(n):
    return lambda x: n+x 


f = fazer_func(10)

print(f(90))
