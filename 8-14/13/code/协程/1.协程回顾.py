def   go():
    print 1
    yield 1
    print 11
    yield 11
    print 111
    yield 111

my=go()  #分段执行
print type(my)
print  next(my)
print  next(my)
print  next(my)

