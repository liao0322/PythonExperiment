

def file_to_list(filename):
    l = []
    try:
        with open(filename) as f:
            for raw in f:

                raw_dict = {}
                raw_list = raw.strip().split(',')
                raw_dict["name"] = raw_list[0]
                raw_dict["price"] = raw_list[1]
                l.append(raw_dict)
        return l
    except FileNotFoundError as e:
        print("文件未找到!")
        return None

if __name__ == '__main__':

    while True:
        goods_list = file_to_list("goods")
        for index, goods in enumerate(goods_list):
            print(index, goods["name"], goods["price"])
        instruct_str = input("请输入命令：[i]新增商品，[m]修改商品价格, [q]退出 >>> ")

        if instruct_str == 'q':
            exit()
        elif instruct_str == 'i':
            goods_name = ''
            while len(goods_name) == 0:
                goods_name = input("请输入商品名称或[b]返回，[q]退出：")
                if goods_name == 'b':
                    break
                elif goods_name == 'q':
                    exit()
                else:
                    while True:
                        goods_price = input("请输入商品价格或[b]返回，[q]退出：")

                        if goods_price == 'q':
                            exit()
                        elif goods_price == 'b':
                            break
                        else:
                            if goods_price.isdigit():
                                with open("goods", "a+") as f:
                                    f.write(goods_name + "," + goods_price + '\n')
                                break
                            else:
                                print("价格只能为数字!")


        elif instruct_str == 'm':
            pass
        else:
            print("无效命令!")


'''
hasToBuyGoods = []

balance_str = input("请输入您的资产: ")

if balance_str.isdigit():
    balance = int(balance_str)
    while True:
        for index, item in enumerate(commodities):
            print(index, item[0], item[1])
        index = input("请输入将要购买的商品序号: ")
        if index.isdigit():
            index = int(index)
            if index < len(commodities) and index >= 0:
                item = commodities[index]
                if balance >= item[1]:
                    hasToBuyGoods.append(item)
                    balance -= item[1]
                else:
                    print("余额不足！")
            else:
                print("无效商品！")
        elif index == 'q':
            print(hasToBuyGoods)
            exit()
        else:
            print("无效输入！")
'''
