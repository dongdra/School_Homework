import csv
"""
Name: portfolio.csv,prices.csv
precondition: portfolio.csv 파일에있는 price 값이 prices.csv 에는 값으로 바꿔야합니다.
Method: read_csv, diff(old,new), find_(price)
Post: 28686.10
"""

# portfolio.csv,prices.csv 파일 읽기
def read_csv(file):
    data = []
    with open(file, 'r') as f:
        rdr = csv.reader(f)
        for line in rdr:
            data.append(line)
    return data

portfolio_data = read_csv('portfolio.csv')
prices_data = read_csv('prices.csv')

# price 바뀐 값의 차이를 계산하는 함수
def diff(old, new):
    difference = float(new) - float(old)
    if difference > 0:
        return f"+{difference:.4f}"
    else:
        return f"{difference:.4f}"

# price 값 찾는 함수
def find_price(symbol, prices_data):
    for data in prices_data:
        if data[0] == symbol:
            return data[1]
    return None

# 결과를 저장할 리스트
updated_data = []

# 포트폴리오의 가격을 최신화
total_value_Gain = 0
for data in portfolio_data[1:]:
    symbol, shares, old_price = data
    new_price = find_price(symbol, prices_data)
    if new_price is not None:
        total_value = float(shares) * float(new_price)
        total_value_Gain += total_value
        updated_data.append([symbol, shares, old_price, new_price, diff(old_price, new_price), total_value])

# 출력
print("Name\tShares\tOld Price\tNew Price\tDifference\ttotal cost")
for data in updated_data:
    print(f"{data[0]}\t{data[1]}\t{data[2]}\t\t{data[3]}\t\t{data[4]}\t{data[5]:.2f}")

print(f"total Gain: {total_value_Gain:.2f}")
