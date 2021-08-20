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
