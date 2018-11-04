
class Phone:
    def __init__(self,id,brand,model,price,count,version):
        self.id = id
        self.brand = brand
        self.model = model
        self.price = price
        self.count = count
        self.version = version

    def __str__(self):
        return '{id}\t\t{brand}\t\t{model}\t\t{price}\t\t{count}\t\t{version}'.format(id=self.id,brand=self.brand,model=self.model,price=self.price,count=self.count,version=self.version)






