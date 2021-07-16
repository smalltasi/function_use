
def read_file(filename):
    product = []

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                 continue
            name, price = line.strip().split(',')
            price = int(price)
            product.append([name, price])
    return product

def user_input(product):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        p = [name, price]
        product.append(p)
    #  也可以寫成  product.append([name, price])
    print(product)
    return product

def print_produce(product):
    for p in product:
        print(p)
        print(p[0], '的價格是', p[1])

def write_file(filename, product):
    with open(filename, 'w', encoding='utf-8') as f:   #csv要加編碼 通用utf-8
        f.write('商品,價格\n')
        for pd in product:
            f.write(pd[0] + ',' + str(pd[1]) + '\n') #pd[1]原是整數再轉為字串


def main():
    filename = input('請輸入檔案名稱: ')
    import os
    if os.path.isfile(filename):
        product = read_file(filename)
        print('開啟舊檔')
    else:
        print('開啟新檔')
        product = []

    product = user_input(product)
    print_produce(product)
    write_file(filename, product)

main()
