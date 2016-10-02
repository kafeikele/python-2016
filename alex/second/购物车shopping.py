#_*_coding:utf-8_*_
'''
Create on Oct 1 , 2016
@author: Steven
'''
import  re, math

def get_customer_salary():
    while True:
        salary = raw_input("Please enter you monthly salary:")
        if __is_valid_num(salary): return int(salary)
        print "[Warn] Please enter a valid number!\n"
        continue

def __is_valid_num(salary):
    num_pattern = re.compile(r"\d+")
    if num_pattern.match(salary): return True
    return False


def get_customer_selection():
    while True:
        selection = raw_input("Please enter the goods number you would like to buy: ")
        if __is_valid_num(selection):
            if __is_a_valid_selection(int(selection)): return int(selection)
            print "[Warn] Please enter a valid selection number"
            continue
        print "[Warn] Please enter a valid number!\n"
        continue

def __is_a_valid_selection(selection):
    try:
        if 1 <= selection <= get_total_amount_of_products(): return True
        return False
    except:
        print "Please enter a valid integer!"

def get_products_list():
    return {'Flower':50,"Perfume":300,"Shoes":600,'Clothing':600,"Alcohol":300,
            "Makeup":800,"Bike":1500,"Car":200000,"Apartment":5000000}


def get_total_amount_of_products():
    return len(get_products_list())

def mapping_type_code_for_products():
    return ["Flower","Perfume","Shoes",'Clothing',"Alcohol","Makeup","Bike","Car","Apartment"]

def get_product_price(type_code):
    return get_products_list()[get_product_name(type_code)]

def get_product_name(type_code):
    return mapping_type_code_for_products()[type_code - 1]

def get_lowest_price_of_products():
    price_list = []
    for k, v, in get_products_list().items():
        price_list.append(v)
    return min(price_list)

def get_highest_price_of_products():
    price_list = []
    for k, v, in get_products_list().items():
        price_list.append(v)
    return max(price_list)

def still_can_buy_something(left_money):
    if left_money < get_lowest_price_of_products(): return False
    return True
def still_want_to_buy_something():
    while True:
        answer = raw_input("Do you still want to buy something?(y/n)\n")
        result = is_a_valid_answer(answer)
        if result == 'yes': return True
        if result == 'no': return False
        print "[Warn] Please enter [yes/no] or [y/n]!\n"

def is_a_valid_answer(answer):
    yes_pattern = re.compile("[Yy][Ee][Ss]|[Yy]")
    no_pattern = re.compile("[Nn][Oo]|[Nn]")
    if yes_pattern.match(answer): return "yes"
    if no_pattern.match(answer): return "no"
    return False

def show_shopping_list():
    counter = 1

def show_shopping_list():
    counter = 1
    for i in mapping_type_code_for_products():
        print '''
        (%d) %s: %s RMB''' %(counter,i+" "*(10-len(i)),str(get_products_list()[i]))
        counter += 1
    print "\n"

def is_affordable(left_money,product_price):
    if left_money >= product_price: return True
    return False

def time_needed_to_work_for_buying_products(salary,price):
    result = float(price) / salary
    return get_formatting_time(int(math.ceil(result)))

def get_formatting_time(months):
    if months < 12: return ("%d months" % months)
    years = months / 12
    months = months % 12
    return ("%d years,%d months" %(years,months))
#主程序这里开始
if __name__ == '__main__':
    #获取本月的工资
    salary = get_customer_salary()
    total_money = salary
    #初始化购物车
    shopping_cart = []
    while True:
        #打印购物车列表
        show_shopping_list()
        #半段剩余资金会否足够买购物车列表中的最低商品
        if still_can_buy_something(total_money):
            #获取用户需要购买的商品编号
            selection = get_customer_selection()
            #获取次商品价格
            #product_price = get_product_price(selection)
            #获取此商品价格
            product_price = get_product_price(selection)
            # 获取此商品名称
            product_name = get_product_name(selection)
            #判断剩余资金是否够购买此商品
            if total_money >= product_price:
                total_money -= product_price
                #打印购买成功信息
                print ("Congratulations! You bought a %s sucessfully!\n" %product_name)
                print ("You still have %d RMB left\n" %total_money)
                #判断是否还想购买其他商品
                if not still_want_to_buy_something():
                    print ("Thank you for comming!")
                    break
            else:
                #输出还需要工作多久才能买
                format_time = time_needed_to_work_for_buying_products(salary,product_price-total_money)
                print "Sorry, you can not afford this product!\n"
                print "You have to work '%s' to get it!\n" %format_time
                #判断是否还想购买其他的商品
                if  not still_want_to_buy_something():break
        else:
            #输出提示你已经无法负担任何商品
            print "Sorry, you do not have enough momey to purchase anything!\n"
            break
    #打印购物车列表
    print "You bought %s " %shopping_cart,