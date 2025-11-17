class Logger:
  name = ""
  def __init__(self, name):
    self.name = name
  def log(self,*texts):
    if len(texts) != 0:
      print(f"[{self.name}]: {texts[0]}")
      if len(texts) != 1:
        for i in texts[1:]:
          print((" "*(len(texts[0])+5))+i)
def log(name,*texts):
  if len(texts) != 0:
    print(f"[{name}]: {texts[0]}")
    if len(texts) != 1:
      for i in texts[1:]:
        print((" "*(len(texts[0])+5))+i)
log("Module","hello","world!")
module = Logger("Module2")
module.log("hello2","world!2")