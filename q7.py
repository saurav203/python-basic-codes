def f1(*a):
    ssr=[i.upper() for i in a]
    return sorted(ssr)
print(f1("snow","glacier","iceberg"))    