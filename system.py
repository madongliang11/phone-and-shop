from db import DB
from phone import Phone

class System:
    def __init__(self):
        self.db = DB()

    def menu(self):
        print('-------------------------------------')
        print('手机信息管理系统')
        print('1、手机录入')
        print('2、根据手机品牌查询手机信息')
        print('3、查询全部手机信息')
        print('4、根据手机编号修改手机价格')
        print('5、根据手机编号删除手机记录')
        print('6、退出')
        print('-------------------------------------')

    # 添加手机信息
    def addphone(self):
        nums = input('请输入手机编号：')
        for phone in self.db.phones:
            if nums == phone.id:
                print('编号已存在！请重新输出')
                return -1
        brand = input('请输入手机品牌：')
        model = input('请输入手机型号：')
        price = input('请输入手机价格：')
        count = input('请输入手机数量：')
        version = input('请输入手机版本：')
        phone = Phone(nums,brand,model,price,count,version)
        self.db.insert(phone)
        self.db.commit()

    # 根据手机编号删除手机记录
    def del_phone(self):
        num = input("请输入要删除的手机编号：")
        for phone in self.db.phones:
            if num == phone.id:
                self.db.phones.remove(phone)
                print('删除成功！')
                self.db.commit()
                return 1
        print('对不起，您所要删除的手机不存在！')



    # 根据手机品牌查询手机信息
    def search_phone(self):
        brand_str = input("请输入您要查询的手机品牌：")
        phone_list=[]
        for phone in self.db.phones:
            if brand_str in phone.brand:
                phone_list.append(phone)
        if not phone_list:
            print('对不起，你所要查询的手机不存在！')
        else:
            print("序号\t\t品牌\t\t\t型号\t\t\t价格\t\t\t数量\t\t版本")
            for i in phone_list:
                print(i)


    # 修改价格
    def update_price(self):
        num = input('请输入要修改的手机编号：')
        for phone in self.db.phones:
            if num == phone.id:
                price_str = input("请输入修改后的价格：")
                phone.price = price_str
                print('修改成功！')
                self.db.commit()
                return 1
        print('对不起，你所要修改的手机不存在！')


    def display_all_phones(self):
        # 显示所有手机信息
        print("序号\t\t品牌\t\t\t型号\t\t\t价格\t\t\t数量\t\t版本")
        for phone in self.db.phones:
            print(phone)

