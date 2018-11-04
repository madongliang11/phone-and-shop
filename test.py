import time
from system import System


def main():
    system = System()
    while True:
        system.menu()
        oper = input('请输入您的操作：')
        if oper =='1':
            system.addphone()
        elif oper =='2':
            system.search_phone()
        elif oper =='3':
            system.display_all_phones()
        elif oper =='4':
            system.update_price()
        elif oper =='5':
            system.del_phone()
        elif oper =='6':
            exit()
        time.sleep(2)

if __name__ == '__main__':
    main()


