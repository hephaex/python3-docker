class User:
    # 클래스 변수 
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name

print(User.count) # 0
tom = User("tom")
bob = User("bob")
print(User.count) # 2

print(tom.count) # 2
