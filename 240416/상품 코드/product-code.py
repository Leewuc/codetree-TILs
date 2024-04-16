class product:
    def __init__(self,name="codetree",code=88):
        self.name = name
        self.code = code
# print(f"product {product.code} is {product.name}")
print(f"product 50 is codetree")
na,co = tuple(input().split())
pro = product(na,int(co))
print(f"product {pro.code} is {pro.name}")