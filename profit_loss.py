from pathlib import Path
import csv
def profit_loss():
    """
    Function does not require parameter
    Function returns the day where the net profit is lower than the previous day and the value of the difference.
    """
    """
    Function does not require parameter
    Function returns the day where the cash on hand is lower than the previous day and the value of the difference.
    """
    file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
    netprofit_list = []
    days_list = []
    with file_path.open(mode = 'r', encoding = 'UTF-8', newline ='' ) as file:
        reader = csv.reader(file)
        next(reader)
        for datas in reader:
            netprofit_list.append(float(datas[4]))
            days_list.append(datas[0])
        print(netprofit_list)
        print(days_list)
    index = 1
    while index <= len(netprofit_list):
        difference = (netprofit_list[index]) - (netprofit_list[index- 1]) 
        if difference <= 0:
            return f"[PROFIT DEFICIT] DAY: {days_list[index]}, AMOUNT: USD{-(difference)}"
        if difference > 0:
            return "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
        index = index + 1  
print(profit_loss())