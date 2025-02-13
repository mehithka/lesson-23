#zip
s1 = {1,2,3}
s2={'b','v','g'}
s3 = list(zip(s1,s1))
print(s3,'\n')

list1 = [10,20,30,40]
list2 = [100,200,300,400]

for x ,y in zip (list1,list2[::-1]):
    print(x,y)

stocks =  ['relaiance','indosys','TCS']
prices = [1231,1123,2001]

new_dict = {stocks: prices for stocks,prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))