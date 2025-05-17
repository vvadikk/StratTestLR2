from five import new_m_f

filtered = list(filter(lambda x: len(str(x)) < 6, new_m_f()))
print(filtered)