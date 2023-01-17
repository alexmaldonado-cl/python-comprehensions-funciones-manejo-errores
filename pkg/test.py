from my_functions import get_totals, calc_total

def get_total(orders):
  # Tu código aquí 👇
  result = get_totals(orders)
  result = calc_total(result)
  return result

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)