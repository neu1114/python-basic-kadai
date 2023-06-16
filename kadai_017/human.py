class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}は{self.age}歳で大人です。")
    else:
      print(f"{self.name}は{self.age}歳で大人ではないです。")
  
human1 = Human("太郎", 30)
human2 = Human("次郎", 25)
human3 = Human("三郎", 19)

humans = [human1, human2, human3]
for human in humans:
  human.check_adult()
