import datetime
from dateutil import relativedelta


def calculate_subscription(expiry_date, months_to_buy, monthly_cost):
    if months_to_buy == 1:
        cost = (monthly_cost / 30) * 26
        date = datetime.datetime.strptime(expiry_date, '%d/%m/%Y').date()
        new_expiry_date = date + relativedelta.relativedelta(days=26)
        #print(new_expiry_date.strftime('%d/%m/%Y'))
        #print(round(cost, 2), "")
        return new_expiry_date.strftime('%d/%m/%Y'), round(cost, 2)





def main():
    print(calculate_subscription('19/06/2022', 1, 1000))

if __name__ == "__main__":
    main()


# output
# ('15/07/2022', 866.67)

