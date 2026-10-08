
"""marks tool -print a short report for a list of marks."""
from config import load_env
from stats import average,highest,lowest
MARKS=[72,65,88,91,54]
def main():
          settings=load_env()
          print(settings["APP_NAME"])
          print("count:",len(MARKS))
          print("average:",average(MARKS))
          print("highest:",highest(MARKS))
          print("lowest:",lowest(MARKS))
if __name__== "__main__":
     main()

