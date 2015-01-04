

def rtrim_zeros(ver_num):
    while len(ver_num) > 1 and ver_num[-1] == 0:
        ver_num.pop(-1)
    return ver_num

print(rtrim_zeros([0, 0, 0]))
print(rtrim_zeros([1, 0, 0]))
print(rtrim_zeros([1, 1, 0, 0]))