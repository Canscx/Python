"""
Number Guess
"""

from module import randint
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  roll_dice(6)
  
def roll_dice(number_of_sides):
  guess = get_user_guess()
  if guess > max_val:
    print "No guessing higher than the maximum possible value!"
  else:
    print "Rolling..."
    sleep(2)
    #在下一行上2秒钟来模拟骰子滚动 数字'2'可以随意更改.
    print "The 1st roll is: %d" % first_roll
    sleep(1)
    #将程序休眠1秒钟.
    print "The 2nd roll is: %d" % second_roll
    sleep(1)
    #程序再次持续1秒.
    
def roll_dice(number_of_sides):
      # ...
      # '#...'缩写以避免冗长的提示，应删除或替换实际代码.
      if guess > max_val:
        # ...
      else:
        # ...没错，我就是那么皮.
        total_roll = first_roll + second_roll
        print "The total value is: %d" % total_roll
        print "Result..."
        sleep(1)
        #该程序为1秒构建悬念.
        if guess == total_roll:
          print "You won!"
        else:
          print "You lost, try again."
          #没错！你可以在else里再搞一个else 骚不骚？
          
def get_user_guess():
  # ...
def roll_dice(number_of_sides):
  # ...
roll_dice(6)
#被遗落的一段代码 猜猜是干什么用的？存在必然有它的理由.
          