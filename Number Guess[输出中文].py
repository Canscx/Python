"""
数字猜猜
"""

from module import randint
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("猜一个数字: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "最大可能值为: %d" % max_val
  guess = get_user_guess()
  roll_dice(6)
  
def roll_dice(number_of_sides):
  guess = get_user_guess()
  if guess > max_val:
    print "你个傻X 别tm乱输数字!"
  else:
    print "骰子滚动中..."
    sleep(2)
    #在下一行上2秒钟来模拟骰子滚动 数字'2'可以随意更改.
    print "第一次是: %d" % first_roll
    sleep(1)
    #将程序休眠1秒钟.
    print "第二次是: %d" % second_roll
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
        print "总值为: %d" % total_roll
        print "结果..."
        sleep(1)
        #该程序为1秒构建悬念.
        if guess == total_roll:
          print "恭喜你赢了!man!"
        else:
          print "你个辣鸡 这都会输 别再试一次了 下次照样输."
          #没错！你可以在else里再搞一个else 骚不骚？
          
def get_user_guess():
  # ...
def roll_dice(number_of_sides):
  # ...
roll_dice(6)
#被遗落的一段代码 猜猜是干什么用的？存在必然有它的理由.
          