#試著輸入True或False，看會run 出甚麼
# print(3 * False)
# print(-3.1 * True)
# print(type("abc" * True))
# print(len("abc" * True))

#設定一變數用布林定義
# def get_expected_cost(baths,beds,basements):
#     empty=80000
#     each_bathroom=10000
#     each_bedroom=30000
#     have_basement=40000
#     get_expected_cost=empty+each_bathroom*baths+each_bedroom*beds+have_basement*basements
#     return get_expected_cost
# a_total=get_expected_cost(1,1,True)
# print(a_total)


# print(False + False)
# print(True + False)
# print(False + True)
# print(True + True)
# print(False + True + True + True)
#得到結論，false值為0，true值為1

#You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# Spaces and punctuation are counted as engraved units.
# Write a function cost_of_project() that takes two arguments:

# engraving - a Python string with the text of the engraving
# solid_gold - a Boolean that indicates whether the ring is solid gold
def cost_of_project(engraving,solid_gold):
    cost_of_project=solid_gold*(100+10*len(engraving))+(1-solid_gold)*(50+7*len(engraving))
    return cost_of_project
a_total=cost_of_project("angel",True)
b_total=cost_of_project("angel",False)
print("A顧客總共刻了",len("angel"),"個字,總共",a_total,"元")
print(b_total)
    