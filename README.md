# Money-Saving-Plans
By choosing one of three money saving plans, to evaluate users' money saving wish. The fourth option is for users to check how much amount of money to save firstly in order to withdraw the wish of a sum of money by the end of setting.  



## Strategy
1. chose plan 1 : deposit the amount of money firstly, save some per period then.
2. chose plan 2 : deposit the amount of money firstly, withdraw some per period then.
3. chose plan 3 : deposit all amount of money, not save or withdraw any per period. 
4. chose plan 4 : withdraw the amount of money in the end, how much to deposit firstly and the amount per period to save.


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
● pay_all   
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
	if __name__ == "__main__":
	    run = SavingEvaluate()
	    run.start()
	    
	    
#### 2. Enter user's name if entering invalid name, which includes punctuations or whitespace, codes will request user to re-enter till entering a valid name to run next. 
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
                
                
#### 3. Choose money saving plans
    while True:
        try:
            plan = int(input('請選擇存錢方案\n'
                             '【1】期初存一筆，各按年存入\n'
                             '【2】期初存一筆，各按年提領\n'
                             '【3】一次繳清 \n'
                             '【4】想知道如果想賺多少，剛開始須存入之金額 \n: '))
			       
			       
#### 4. Codes will not run next till user enters numerical numbers( only from 1 to 4 ). 		       
        except ValueError as e:
            print('請輸入1~4的數字，非文字或其他。\n')
            continue
        else:
            if 1 <= plan <= 4:
                self.saving_year = int(input("請輸入存錢總年期數： "))
                if self.saving_year < 1:
                    print('存錢總年期數須大於1年。\n')
                    continue
		    
		    
#### 5. Codes will run next for user to enter rate to search
                self.rate = int(input("請輸入欲查詢的年利率(大於或是等於1)： ")) / 100
                print('\n您好:%s，您選擇【%d】方式。為期 %d年 存錢方案，%.2f%% 年利率。' % 
                (username, method, self.saving_year, self.rate*100))

		    
#### 6. Codes run next which depends on the money saving plan that user chooses.
##### if user chooses plan 1, user will be asked to enter the amount of money to firstly deposit, and the amount per period to save then. Codes call the future_value() function in the end.
                if plan == 1:
                    self.first_deposit = int(input("請輸入期初存入金額： "))
                    self.pmt = int(input("請輸入各按年存入金額： "))
                    cash_flows = [-self.first_deposit]
                    for i in range(self.saving_year):
                        cash_flows.append(self.pmt)
                    npv = npf.npv(self.rate, cash_flows)
                    print('本存錢方案的淨現值: \033[1;30;43m%.1f \033[0m 元' % npv)
                    self.future_value()
##### if user chooses plan 2, user will be asked to enter the amount of money to firstly deposit, and hope to withdraw the amount of money per period. Codes call the irr() function in the end.		    
                elif plan == 2:
                    self.first_deposit = int(input("請輸入期初存入金額： "))
                    nwp = int(input("請輸入各按年提領金額： "))
                    self.irr(nwp)
##### if user chooses plan 3, user will be asked to enter the amount of money to pay all at once. Codes call the pay_all() function in the end.			    
                elif plan == 3:
                    self.first_deposit = int(input("請輸入一次性存入金額： "))
                    self.pay_alle()
##### if user chooses plan 4, user will be asked to enter the amount of money to withdraw by the end of hoping saved-years, saving amount  per period Then codes call the present_value() function in the end.			 
                elif plan == 4:
                    future_value = int(input("請輸入最後想領回金額： "))
                    money = int(input("請輸入各按年存入金額： "))
                    self.present_value(money, future_value)
		    

## Run functions			
#### 1. future_value: npf.fv()
	future_value = npf.fv(self.rate, self.saving_year, -self.pmt, -self.first_deposit)
	# 按年繳未來價值淨利計算，計算到小數後第一位
	future_net_income = np.round((future_value-self.first_deposit-(self.saving_year*self.pmt)), 1)
	print('以每年 %d 元投資%.2f%%年利率，%d 年後可領回: \033[1;30;43m %d \033[0m 元'
	      % (self.pmt, self.rate*100, self.saving_year, int(future_value)))
	print('總淨利為: \033[1;30;43m%.1f \033[0m 元' % future_net_income)
        
#### 2. irr: npf.irr()


#### 3. pay_all: npf.fv()


#### 4. present_value: npf.pv()
