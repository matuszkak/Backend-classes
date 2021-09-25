class Date:
  def __init__(self, date):
    self.date = date

  def get_date(self):
    print('getting the date...')
    return self.date


# csak egy fv a classon belül, nem kell hozzá a self, példány

  @staticmethod
  def to_dash_date(date):
    return date.replace('/', '-')

  @classmethod
  def extra_year(cls, date):
    date_parts = date.get_date().split('-')
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]
    new_date = f"{int(year)+1}-{month}-{day}"
    return cls(new_date)

my_date = Date("2020-01-15")

print(my_date.get_date())

date_from_db = '2021/03/23'

converted_date_from_db = Date.to_dash_date(date_from_db)
print(converted_date_from_db)

extra_year_date = Date.extra_year(my_date)
print(extra_year_date.get_date())