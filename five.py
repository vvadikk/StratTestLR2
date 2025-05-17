def new_m_f():
    m = [3.46871, 5.31916, 4.013449, 6.57686, 15.012678]
    precisions = [5, 4, 3, 2, 1]
    new_m = list(map(lambda x: round(x[0], x[1]), zip(m, precisions)))
    return new_m
if __name__ == '__main__':
    print(new_m_f())
