"""
面向对象的三大支柱：封装、继承、多态
面向对象的设计原则：SOLID原则
S: Single Responsibility Principle (SRP)
O: Open-Closed Principle (OCP)
L: Liskov Substitution Principle (LSP)
I: Interface Segregation Principle (ISP)
D: Dependency Inversion Principle (DIP)

S - 单一职责原则 (SRP)
一个类应该只有一个理由去改变。也就是说，一个类应该只有一个单一的职责。
例子：假设我们有一个 User 类，它负责处理用户的登录、注册和个人信息管理。如果我们还想添加一个发送邮件的功能，我们不应该直接在 User 类中添加这个功能，而是应该创建一个新的 MailService 类来负责发送邮件。

O - 开闭原则 (OCP)
一个类应该对扩展开放，对修改关闭。也就是说，我们可以通过继承或组合来扩展一个类的功能，而不需要修改它的源代码。
例子：假设我们有一个 PaymentGateway 类，它负责处理不同类型的支付。我们可以通过创建子类 AlipayPaymentGateway 和 WechatPaymentGateway 来扩展支付类型，而不需要修改 PaymentGateway 类的源代码。

L - 里氏替换原则 (LSP)
子类应该可以替换父类。也就是说，任何使用父类的地方都应该能够使用子类。
例子：假设我们有一个 Bird 类，它有一个 fly 方法。我们创建一个 Duck 类继承自 Bird，但是 Duck 类的 fly 方法实现不同。那么，任何使用 Bird 类的地方都应该能够使用 Duck 类。

I - 接口隔离原则 (ISP)
一个类不应该被迫依赖它不需要的接口。也就是说，我们应该尽量减少接口的依赖关系。
例子：假设我们有一个 Print 接口，它有两个方法 print 和 scan。我们创建一个 Printer 类实现 Print 接口，但是它只需要 print 方法。那么，我们不应该强迫 Printer 类实现 scan 方法。

D - 依赖倒置原则 (DIP)
高层模块不应该依赖低层模块，而应该依赖抽象。也就是说，我们应该尽量减少模块之间的依赖关系。

面向对象的设计模式：GoF(Gang of Four)设计模式（单例、工厂、代理、策略、迭代器）
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工(抽象类)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp
