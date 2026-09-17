"""marks tool -print a short report for a list of marks."""
from config impport load-env
from stats import acerage,highest
MARKS=[72,65,88,91,54]
def main():
          settings=load_env()
          print(settings["APP_NAME"])
          print("count:",len(MARKS))
          print("avaerage:",avearge(MARKS))
          print("highest:",highest(MARKS))
if __name__=="__main__":
     main()
