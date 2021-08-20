# Money-Saving-Evaluation
By choosing one of three money saving plans, to evaluate users' money saving wish. The fourth option is for users to check how much amount of money to save first in order to withdraw the wish of a sum of money by the end of setting.  



## Strategy
1.
2.
3.
4.


## Requirements
● Python 3    
● numpy_financial   
● numpy   
● warnings  
● string  
● pymysql  
● matplotlib 


## Class
SavingEvaluate


## Functions
● future_value    
● irr  
● pay_all_at_once   
● present_value  
● start


## Create __init__
#### set saving_year, rate, pmt(payment per period), first deposit
    def __init__(self):
            self.all_charts = string.punctuation + string.whitespace
            warnings.filterwarnings('ignore', category=DeprecationWarning)
            warnings.filterwarnings('ignore', category=RuntimeWarning)

            # 總年期數
            self.saving_year = 0
            # 年利率
            self.rate = 0
            # 各按年存入之金額
            self.pmt = 0
            # 期出存入金額
            self.first_deposit = 0


## Run codes
#### 1. Call the main finction to work, start.
##### enter user's name if entering invalid name, which includes punctuations or whitespace, the code will request user to re-enter till entering a valid name to run next. 
    while True:
            username = input('請輸入您的名字: ')
            for i in username:
                if i in self.all_charts:
                    print('請輸入有效名字。')
                    continue
            if username.isalpha() is True:
                print('有效名字 :%s，您好!' % username)
                time.sleep(1)
                break
                
                
##### choose money saving plans
    while True:
        try:
            method = int(input('請選擇存錢方案\n'
                               '【1】期初存一筆，各按年存入\n'
                               '【2】期初存一筆，各按年提領\n'
                               '【3】一次繳清 \n'
                               '【4】想知道如果想賺多少，剛開始須存入之金額 \n: '))
        except ValueError as e:
            print('請輸入1~4的數字，非文字或其他。\n')
            continue
        else:
            if 1 <= method <= 4:
                self.saving_year = int(input("請輸入存錢總年期數： "))
                if self.saving_year < 1:
                    print('存錢總年期數須大於1年。\n')
                    continue
                self.rate = int(input("請輸入欲查詢的年利率(大於或是等於1)： ")) / 100
                print('\n您好:%s，您選擇【%d】方式。為期 %d年 存錢方案，%.2f%% 年利率。' % 
                (username, method, self.saving_year, self.rate*100))

                if method == 1:
                    self.first_deposit = int(input("請輸入期初存入金額： "))
                    self.pmt = int(input("請輸入各按年存入金額： "))
                    cash_flows = [-self.first_deposit]
                    for i in range(self.saving_year):
                        cash_flows.append(self.pmt)
                    npv = npf.npv(self.rate, cash_flows)
                    print('本存錢方案的淨現值: \033[1;30;43m%.1f \033[0m 元' % npv)
                    self.future_value()
                elif method == 2:
                    self.first_deposit = int(input("請輸入期初存入金額： "))
                    nwp = int(input("請輸入各按年提領金額： "))
                    self.irr(nwp)
                elif method == 3:
                    self.first_deposit = int(input("請輸入一次性存入金額： "))
                    self.pay_all_at_once()
                elif method == 4:
                    future_value = int(input("請輸入最後想領回金額： "))
                    money = int(input("請輸入各按年存入金額： "))
                    self.present_value(money, future_value)

			
#### 2. Go to the first function, future_value:  
    	
        
#### 3. Go to irr function: 


#### 4. Go to pay_all_at_once function:


#### 5. Go to present_value function:
