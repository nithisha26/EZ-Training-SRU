#Multi-level inheritance and hierarchical inheritance
class Siva1:
    def gold(hnk):
        print("40L")
class baby1(Siva1):
    def chain(hnk):
        print("50L")
class baby2(Siva1):
    def car(hnk):
        print("20L")
class gbaby(baby1):
    def silver(hnk):
        print("30L")
v1=gbaby()
v1.silver()
v1.chain()
v1.gold()

v2=baby2()
v2.car()
v2.gold()
