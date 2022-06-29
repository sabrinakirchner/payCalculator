hours = float(input("Enter your hours "))
rate = float(input("Enter your rate "))

hoursWeek = 40
overtime = 1.5
extra = (hours - hoursWeek)*overtime*rate

if hours > hoursWeek:
    normalPay = rate* hoursWeek
    print("Your Pay is ", extra+normalPay)

else:
    normalPay = hours*rate
    print("Your pay will be  ")