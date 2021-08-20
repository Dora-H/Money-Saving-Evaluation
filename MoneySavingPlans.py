import time
import numpy_financial as npf
import numpy as np
import warnings
import string
import matplotlib.pyplot as mp


class SavingEvaluate(object):
    def __init__(self):
        self.all_charts = string.punctuation + string.whitespace
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        warnings.filterwarnings('ignore', category=RuntimeWarning)

        self.saving_year = 0
        self.rate = 0
        self.pmt = 0
        self.first_deposit = 0

    def future_value(self):
        future_value = npf.fv(self.rate, self.saving_year, -self.pmt, -self.first_deposit)
        future_net_income = np.round((future_value-self.first_deposit-(self.saving_year*self.pmt)), 1)
        print('以每年 %d 元投資%.2f%%年利率，%d 年後可領回: \033[1;30;43m %d \033[0m 元'
              % (self.pmt, self.rate*100, self.saving_year, int(future_value)))
        print('總淨利為: \033[1;30;43m%.1f \033[0m 元' % future_net_income)

        money = self.first_deposit
        fvs = [self.first_deposit]
        for i in range(1, self.saving_year+1):
            money += money*self.rate + self.pmt
            fvs.append(money)

        mp.figure('Future Value', facecolor='lightgray')
        mp.title('Future Value', fontsize=24)
        mp.xlabel('Year', fontsize=20)
        mp.ylabel('Money', fontsize=20)
        mp.grid(":")
        mp.tick_params(labelsize=12)
        mp.plot(fvs, 'o-', label='Cash Flows')
        for x, y in zip(range(self.saving_year+1), fvs):
            mp.text(x+0.1, y+30, '%.3f' % y, ha='center', va='bottom', fontsize=13)
        mp.legend(loc='upper left', fontsize= 14)
        mp.show()

    def irr(self, nwp):
        cash_flows = [-self.first_deposit]
        for i in range(self.saving_year):
            cash_flows.append(nwp)
        solution = npf.irr(cash_flows) * 100
        print("依照您輸入的相關數據，本存錢方案的 IRR 為 : \033[1;30;43m %.3f%% \033[0m 元" % solution)
        print('最後可領回 : \033[1;30;43m %.3f \033[0m 元' %
              (((self.first_deposit*(1+self.rate)-nwp)*(1+self.rate)-nwp)*(1+self.rate)-nwp))

        money = self.first_deposit
        irrs = [self.first_deposit]
        for i in range(1, self.saving_year+1):
            money += money*self.rate - nwp
            irrs.append(money)

        mp.figure('IRR', facecolor='lightgray')
        mp.title('IRR', fontsize=24)
        mp.xlabel('Year', fontsize=20)
        mp.ylabel('Money', fontsize=20)
        mp.grid(":")
        mp.tick_params(labelsize=12)
        mp.plot(irrs, 'o-', label='Cash Flows')
        for x, y in zip(range(self.saving_year+1), irrs):
            mp.text(x+0.1, y, '%.3f' % y, ha='center', va='bottom', fontsize=13)
        mp.legend(loc='upper right', fontsize=14)
        mp.show()

    def pay_all_at_once(self):
        all_in = npf.fv(self.rate, self.saving_year, 0, -self.first_deposit)
        all_in_net_income = np.round(all_in-self.first_deposit, 3)
        print('以每年 %d 元投資%.2f%%年利率，%d 年後可領回: \033[1;30;43m %.3f \033[0m 元'
              % (self.pmt, self.rate*100, self.saving_year, all_in))
        print('總淨利為: \033[1;30;43m%.3f \033[0m 元' % all_in_net_income)

        money = self.first_deposit
        plio = [self.first_deposit]
        for i in range(1, self.saving_year+1):
            money += money*self.rate
            plio.append(money)

        mp.figure('Pay All In Once', facecolor='lightgray')
        mp.title('Pay All In Once', fontsize=24)
        mp.xlabel('Year', fontsize=20)
        mp.ylabel('Money', fontsize=20)
        mp.grid(":")
        mp.tick_params(labelsize=12)

        mp.plot(plio, 'o-', label='Cash Flows')
        for x, y in zip(range(self.saving_year+1), plio):
            mp.text(x+0.1, y, '%.3f' % y, ha='center', va='bottom', fontsize=13)
        mp.legend(loc='upper left', fontsize=14)
        mp.show()

    def present_value(self, money, future_value):
        present_value = npf.pv(self.rate, self.saving_year, -money, future_value)
        print("如果要拿回 %d 元，%.2f%%年利率, 為期%d年。" % (future_value, self.rate*100, self.saving_year))
        print('須先始存:\033[1;30;43m %d \033[0m 元。' % abs(np.floor(present_value)))

    def start(self):
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
        while True:
            try:
                plan = int(input('請選擇存錢方案\n'
                                 '【1】期初存一筆，各按年存入\n'
                                 '【2】期初存一筆，各按年提領\n'
                                 '【3】一次繳清 \n'
                                 '【4】想知道如果想賺多少，剛開始須存入之金額 \n: '))
            except ValueError as e:
                print('請輸入1~4的數字，非文字或其他。\n')
                continue
            else:
                if 1 <= plan <= 4:
                    self.saving_year = int(input("請輸入存錢總年期數： "))
                    if self.saving_year < 1:
                        print('存錢總年期數須大於1年。\n')
                        continue
                    self.rate = float(input("請輸入欲查詢的年利率(大於或是等於1)： ")) / 100
                    print('\n您好:%s，您選擇【%d】方式。為期 %d年 存錢方案，%.2f%% 年利率。' % (username, plan, self.saving_year, self.rate*100))

                    if plan == 1:
                        self.first_deposit = int(input("請輸入期初存入金額： "))
                        self.pmt = int(input("請輸入各按年存入金額： "))
                        cash_flows = [-self.first_deposit]
                        for i in range(self.saving_year):
                            cash_flows.append(self.pmt)
                        npv = npf.npv(self.rate, cash_flows)
                        print('本存錢方案的淨現值: \033[1;30;43m%.1f \033[0m 元' % npv)
                        self.future_value()
                    elif plan == 2:
                        self.first_deposit = int(input("請輸入期初存入金額： "))
                        nwp = int(input("請輸入各按年提領金額： "))
                        self.irr(nwp)
                    elif plan == 3:
                        self.first_deposit = int(input("請輸入一次性存入金額： "))
                        self.pay_all_at_once()
                    elif plan == 4:
                        future_value = int(input("請輸入最後想領回金額： "))
                        money = int(input("請輸入各按年存入金額： "))
                        self.present_value(money, future_value)


if __name__ == "__main__":
    run = SavingEvaluate()
    run.start()
