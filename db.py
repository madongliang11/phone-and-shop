import pickle

class DB:
    def __init__(self):
        # 把phones.data文件中的数据加载到phones中
        try :
            with open('phones.data','rb') as f:
                phones_bytes = f.read()
                # 把二进制的list装换成list对象
                self.phones = pickle.loads(phones_bytes)
        except:
            self.phones = []

    def commit(self):
        # 把phones以二进制的形式写入phones.data文件中
        phones_bytes = pickle.dumps(self.phones)
        with open('phones.data','wb') as f:
            f.write(phones_bytes)

    def insert(self,phone):
        # 添加手机
        self.phones.append(phone)

