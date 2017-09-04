class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name
    # 인스턴스 메소드
    def say_hi(self):
        print("hi {0}".format(self.name))
    # 클래스 메소드 
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

tom.say_hi()
bob.say_hi()

User.show_info()
