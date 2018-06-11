# encoding:utf-8

class A:
    """
    定义Class A
    """

    # 类变量定义,类的所有实例之间共享,可以再内部类或外部类使用
    id = 100

    def __init__(self, pp1="p1", pp2=None):
        """
        构造函数
        :param p1:参数p1,默认值p1
        :param p2:参数p2,默认值None
        """
        self.p1 = pp1
        self.p2 = pp2
        self.p3 = "p3"

        # 自动测试所有的函数
        # self.testAll()

    def testAll(self):
        """
        测试所有的函数
        :return:
        """
        self.printA("HelloWorld")
        self.welcomeA()
        self.testException()

    def printA(self, msg=None):
        """
        打印消息函数
        :param msg:文本消息
        :return:None
        """
        print("--------------------")
        print("A = %s " % self)
        print("A.print %s" % msg)
        print("A.p1 = %s" % self.p1)
        print("A.p2 = %s" % self.p2)
        print("A.p3 = %s" % self.p3)
        print("A.id = %s" % self.id)
        print("\n")

    def welcomeA(self):
        """
        测试pass
        :return:
        """
        print("welcome")
        pass

    def testException(self):
        """
        测试引发异常
        :return:
        """
        try:
            print("todo")
            raise Exception("测试引发异常")
        except Exception as err:
            print("todo err: %s" % err)
        finally:
            print("todo goodbye")
