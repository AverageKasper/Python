staff = int(input("Enter staff amount: "))
m_pay = float(input("Enter medium monthly pay: "))
pay_increase = float(input("Enter yearly salary increase prosentage: "))
years = int(input("how many years to employ: "))

def pay_calc(stf,pay,prc,year):
    #Yearly pay
    y_pay = pay * 12
    #Prosentage
    pros = prc / 100  
    yearly_inc = y_pay * (1 + pros) ** year
    total_stf_pay = yearly_inc * stf
    total_money = total_stf_pay * year 
    return(total_money)

print(f"Total money spent: {pay_calc(staff,m_pay,pay_increase,years):2f}")