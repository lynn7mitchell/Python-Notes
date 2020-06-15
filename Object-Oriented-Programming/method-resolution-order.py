# MRO Method Resolution Order

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

# D -> B -> C -> A
print(D.num)
print(D.mro())

#     A
#   /   \
#  /     \
# B       C
#  \     /
#   \   /
#     D