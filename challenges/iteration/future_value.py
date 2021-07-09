'''
    Determines the future value of an investement using the range
    function.  This is similar to the following on C or Java:
        for(int i = 1; i <= 10; i++)
'''

original_investment = 10000
investment = original_investment
interest = .05
years_invested = 20

for i in range(years_invested):
    yearly_interest = investment * interest
    investment = investment + yearly_interest
investment = round(investment, 2)

print("Orignal Investment: ", original_investment)
print("Interest: ", interest)
print("Years: ", years_invested)
print("Future value:", investment)
