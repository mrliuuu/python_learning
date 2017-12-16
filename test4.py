"""文章原地址：http://yangcongchufang.com/%E9%AB%98%E7%BA%A7python
%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/python-object-class.html"""
"""最简单的类"""
"""__init__方法的第一个参数永远都是self，表示创建实例本身，
在__init__方法内部，可以把各种属性绑定到self，因为self指向创建的实例本身"""
class Student:
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def Print_Message(self):
        print('%s:%s'%(self.__name,self.__score))


stu = Student('peter',98)
stu.Print_Message()
""""和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同："""
stu.age = 18
print('age=%s'%stu.age)

print('\r')


""""在python中在变量前加上双下划綫__表示该变量是私有变量，只有内部能访问外部不能
    若在外部想要得到name,score变量或对变量做修改，可在类中加入相关函数，需要注意的是
    ，Python中如果变量名以双下划线开头和结尾的，是特殊变量__XXX__。特殊变量是可以直
    接从类内部访问的。
    有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可
    以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被
    访问，但是，请把我视为私有变量，不要随意访问”。"""
class Student2:
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_message(self):
        print('%s:%s'%(self.__name,self.__score))
    def set_name_score(self,name,score):
        self.__name = name
        self.__score = score


liu = Student2('liu',100)
liu.print_message()
liu.set_name_score('rui',99)
liu.print_message()

"""继承和多态"""
"""关键字class后面跟着类名，类名通常是大写字母开头的单词，紧接着是(object)，
表示该类是从哪个类继承下来的。通常，如果没有合适的继承类，就使用object类，这
是所有类最终都会继承下来的类。子类的的方法如果和父类的方法重名，子类会覆盖掉父类。
因为这个特性，就获得了一个继承的好处”多态”。"""
class Animal(object):
    def run(self):
        print("running...")
class dog(Animal):
    pass
little_dog = dog()
little_dog.run()



class MyObject(object):
    def __init__(self, x):
        self.x = x*x
        self.y = 10
    def cheng(self):
        return self.x * self.y

obj = MyObject(5)
print(obj.cheng())
print(getattr(obj,'z',100))
print(hasattr(obj,'__init__'))
print(getattr(obj,'__init__'))




