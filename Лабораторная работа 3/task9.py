salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(10):
    need_money = need_money + salary - spend
    spend *= 1.03
need_money = -need_money

print(round(need_money))
