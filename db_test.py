import pandas as pd

orderdb=pd.read_csv('OrderDB.csv')
productdb=pd.read_csv('ProductDB.csv')
userdb=pd.read_csv('UserDB.csv')

order_product_ids=orderdb['product_id'].unique() # orderdb의 제품 id
product_ids=productdb['product_id'].unique() # productdb의 id
# product_names=productdb['name'].unique # prodctdb name (프린터 이름)
# product_colors=productdb['color'].unique # prodctdb color (프린터 컬러)

order_user_ids=orderdb['user_id'].unique() # orderdb의 user id
user_user_ids=userdb['user_id'].unique() # userdb의 user id
# user_name=userdb['name'].unique() # userdb의 user name

order_quantity=orderdb['quantity'].unique() #orderdb의 quantity

print_pr_name=[]
print_color=[]
print_us_name=[]

# orderDB의 proudct_id에 맞는 프린트 제품과 컬러 추출
for order_product_id in order_product_ids:
    if order_product_id in product_ids: #현재 order_product_id가 product_ids 배열에 있는지 확인합니다.
        # 해당 product_id의 이름을 찾기
        pr_name = productdb[productdb['product_id'] == order_product_id]['name'].values
        color=productdb[productdb['product_id'] == order_product_id]['color'].values
        #if len(name) > 0:
        print_pr_name.append(pr_name[0])  # 이름을 리스트에 추가
        print_color.append(color[0])
# orderDB의 user_id에 맞는 name 추출
for order_user_id in order_user_ids:
    if order_user_id in user_user_ids:
        us_name=userdb[userdb['user_id'] == order_user_id]['name'].values
        print_us_name.append(us_name[0])

print(order_product_ids)
print(print_pr_name)
print(print_color)
print(print_us_name)
print(order_quantity)