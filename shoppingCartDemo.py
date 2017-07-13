
commodities = [
    ("iPhone6s", 7899),
    ("Macbook", 19002),
    ("Watch", 3002),
    ("ikbc", 489)
]

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
            if index < len(commodities):
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
            break;
        else:
            print("无效输入！")
