

def code_tracing():
    a = [0]
    b = 101
    c = {123: 456, 789: 101}
    if a[0]:
        print('Answer1:', b + c[123])
    else:
        print('Answer2:', b + c[789])
    mystery(b, a, a[0], c)
    if a[0]:
        print('Answer3:', c)
    else:
        print('Answer4:', c)


def mystery(b, a_0, a, c):
    b += 1
    a_0[0] += 1
    a -= 1
    c[123] = 101
    print('Answer5:', b, a_0, a)


if __name__ == '__main__':
    code_tracing()