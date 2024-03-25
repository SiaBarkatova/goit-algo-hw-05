import re

t = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    pattern = r'(?<!\d)(?<!\d\.)\d{1,4}(?:\.\d{1,2})?(?!\.?\d)' # finding real numbers with decimals
    numbers = re.findall(pattern, text, re.ASCII)

    for number in numbers: # iterate trought found numbers
        yield number


def sum_profit(text: str, func: callable): 
    sum = 0
    for value in func(text):
        sum += float(value)
    
    return sum


total_income = sum_profit(t, generator_numbers)

print(f"Загальний дохід: {total_income}")