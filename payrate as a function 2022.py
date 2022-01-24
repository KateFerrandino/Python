def computepay(rate, hours):
    total_base_wages= rate * hours
    if hours > 40:
        overtime_hours = hours - 40
        overtime_wages = overtime_hours * (rate * .5)
        return overtime_wages + total_base_wages
    return total_base_wages

rate = float(input("How much per hour?"))
hours = float(input("How many hours did you work?"))
wages = computepay(rate, hours)
print("Pay",wages)
