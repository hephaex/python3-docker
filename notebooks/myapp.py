class User:
    def __init__(self, name):
        # 인스턴스 변수 
        self.name = name

tom = User("tom")
bob = User("bob")

print(tom.name)
print(bob.name)
