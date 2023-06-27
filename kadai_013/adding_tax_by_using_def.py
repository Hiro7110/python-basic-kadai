# 課題の提出
def add_tax (price, tax):
  total = price + tax

  print(f"The total cost is {total} yen.")

add_tax(500, 50)

# 課題とは関係ないですが、別の方法でも計算してみました。
# ただtotalのtypeがfloatになってしまったのが気になりました。
def add_tax (price):
  tax = price / 10
  total = price + tax

  print(f"The total cost is {total} yen.")

add_tax(500)
