import matplotlib.pyplot as plt
import numpy as np

# Unit of loan time: year
# kind of amortization: equal loan payments and equal principal payments

loans=[[1000000,3.25,27],[990000,4.65,30]] # year1 <= year2
total1,interest1,year1=loans[0][0],loans[0][1],loans[0][2]
total2,interest2,year2=loans[1][0],loans[1][1],loans[1][2]

def equal_principal_payments(total_borrowing,annual_interest_ratio,loan_time,order_of_current_month):
    monthly_principal=total_borrowing/(loan_time*12) 
    monthly_interest_ratio=annual_interest_ratio*0.01/12.0
    total_month_num=loan_time*12
    remain_total=total_borrowing*(1-(order_of_current_month-1)/total_month_num)
    current_month_interest=remain_total*monthly_interest_ratio
    amount_repayment_current_month=monthly_principal+current_month_interest
    return amount_repayment_current_month

def equal_loan_payments(total_borrowing, annual_interest_ratio, loan_time):
    # unit of annual_interest_ratio and monthly_interest_ratio: %
    total_month_num=loan_time*12
    monthly_interest_ratio=annual_interest_ratio*0.01/12.0
    amount_repayment_every_month=monthly_interest_ratio*total_borrowing*(1+monthly_interest_ratio)**total_month_num/((1+monthly_interest_ratio)**total_month_num-1.0)
    return amount_repayment_every_month

def principal_in_equal_loan_payments(total_borrowing, annual_interest_ratio, loan_time, month_num):
    monthly_repayment=equal_loan_payments(total_borrowing, annual_interest_ratio, loan_time)
    monthly_interest_ratio=annual_interest_ratio*0.01/12.0
    remain_total_borrowing_current=total_borrowing*(1+monthly_interest_ratio)**month_num+monthly_repayment*(1-(1+monthly_interest_ratio)**month_num)/monthly_interest_ratio
    last_month_num=month_num-1
    remain_total_borrowing_last=total_borrowing*(1+monthly_interest_ratio)**last_month_num+monthly_repayment*(1-(1+monthly_interest_ratio)**last_month_num)/monthly_interest_ratio
    principal=remain_total_borrowing_last-remain_total_borrowing_current
    return principal

def brief_summary():
    print('Equal loan payments (Equal for every month): \n')
    print(equal_loan_payments(total1,interest1,year1)+equal_loan_payments(total2,interest2,year2),'\n')

    print('Equal principal payments (first 50 months): \n')
    for i in range(50):
        print('the ', i,'-th month: ', np.round(equal_principal_payments(total1,interest1,year1,i)+equal_principal_payments(total2,interest2,year2,i),0))


def monthly_comparsion():

    el1=equal_loan_payments(total1,interest1,year1)+equal_loan_payments(total2,interest2,year2)
    el2=equal_loan_payments(total2,interest2,year2)
    month_num1=year1*12
    month_num2=year2*12
    equal_loans=[el1 if i<=month_num1 else el2 for i in range(1,month_num2+1)]
    equal_prins=[equal_principal_payments(total1,interest1,year1,i)+equal_principal_payments(total2,interest2,year2,i) if i<=month_num1 else equal_principal_payments(total2,interest2,year2,i) for i in range(1,month_num2+1)]

    prin1=total1/(year1*12)+total2/(year2*12)
    prin2=total2/(year2*12)
    principals_EPP=[prin1 if i<=month_num1 else prin2 for i in range(1,month_num2+1)]

    elp1=lambda i: principal_in_equal_loan_payments(total1,interest1,year1,i)+principal_in_equal_loan_payments(total2,interest2,year2,i)
    elp2=lambda i: principal_in_equal_loan_payments(total2,interest2,year2,i)
    principals_ELP=[elp1(i) if i<=month_num1 else elp2(i) for i in range(1,month_num2+1)]

    for i in range(month_num2):
        print('|',i+1,'|', int(equal_loans[i]),'|',int(principals_ELP[i]),'|',int(equal_prins[i]),'|', int(principals_EPP[i]),'|')

    fig,ax=plt.subplots(figsize=(12,9))

    x=range(1,month_num2+1)

    ax.plot(x, equal_loans,'r',label='Monthly payment by Equal Loan Payments')
    ax.plot(x, principals_ELP, 'r--', label='Paid principal for Equal Loan Payments current month')

    ax.plot(x, equal_prins,'b',label='Monthly payment by Equal Principal Payments')
    ax.plot(x, principals_EPP, 'b--', label='Paid principal for Equal Principal Payments current month')

    ax.grid()
    ax.set_xticks([i for i in range(1, month_num2+11) if i%10==0])
    ax.set_yticks([i for i in range(2500,13000) if i%500==0])
    ax.set_xlim(1,360)
    ax.set_xlabel('Month Number')
    ax.set_ylabel('Monthly Payment')
    plt.legend()
    plt.tight_layout()
    plt.savefig('comparsion.png',dpi=600)
    

#brief_summary()

monthly_comparsion()

