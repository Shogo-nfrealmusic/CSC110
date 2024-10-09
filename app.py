# x=10
# y=2
# z=x/y
# print(z)

# print("x = ",x)
# print("y = ",y)
# print("z = ",z)

# a=3
# b=2
# print(a, "divided by", b, "=", a/b)

# print("\"What's your idea?\", she asked.")
# print(int(-75.6))

# def inch_to_feet(value):
#     value1 = int(value)
#     feet = value1 // 12  
#     inches = value1 % 12  
#     return f"{feet} feet and {inches} inches"

# result = inch_to_feet(33)
# print(result)  

# in_tot=50
# feet=in_tot//12
# inches=in_tot%12
# print(f'{in_tot} in = {feet} feet and {inches} inches')

# print(16-2*5 // 3 + 1)

# print(2**2**3*3)

# print("z =",100 / (2.7*3.1))

# 正しいPythonコード
# z = (7 * (14/3 + 2.3)**2) / (5 - 2**(3/2))**3
# print("z =", round(z,2))

# town = input("Enter 5the name of your city: ")
# print(town + town)

# Age = input("How old are you?: ")
# next_age = float(Age) + 1
# print(f'Next year you will be {next_age}')

# # Get the number of seconds from the user
# n = input("Enter the number of seconds between lightning and thunder: ")

# # Convert the input to an integer (assuming the input is a whole number)
# n = int(n)

# # Calculate the distance of the storm in miles and round it to two decimal places
# distance = round(n / 5, 2)

# # Output the result
# print(f"The storm is {distance} miles away.")

# radius = input("What is radius?: ")
# to_number = float(radius)
# circumference = to_number*2*3.14
# print(f'Circumference is {circumference}')

# radius = float(input("Enter radius: "))
# circumph = 2*3.14*radius
# print("Radius=", radius, "Circumpherence=", circumph)

# Months = int(input("Enter months: "))  # 月は整数なのでint()を使用
# Years = Months // 12  # 年数の整数部分
# month_left = Months % 12  # 残りの月数

# # 結果を見やすく表示
# print(f"Years = {Years}, Months = {month_left}")

# print('HELLO' * 5)

# age = 20
# print("Jen is", age, "years old")

# cost = 250
# print('That bike costs ' + str(250) + "$")

# n = "12324134123432412343234321431243214312543215"
# print(len(n))

# hr_cyc = float(input("How many hours did you do Cycling?: "))
# hr_run = float(input("How many hours did you do running?: "))
# hr_swim = float(input("How many hours did you do swimming?: "))

# total = (hr_cyc * 200) + (hr_run * 475) + (hr_swim * 275)
# print("total: " ,total)

# weight = total/3500

# print('Weight lost=', round(weight, 1), "lb")

# for j in range(5):
#     print("Welcome to CSC110")

# for j in ["q", 2/3, 3, 4**2, "hello"]:
#     print('j')
#     print(j)
# print('done')

# for j in ['Jen', 'Eli', "Sam"]:
#     print(j + ", how are you?")

# for j in range(2,7,2):
#     print(j)

# for j in range(10,6,-1):
#     print(j)

# for j in range(2,6):
#     print(j ** 2)

# import turtle
# sal=turtle.Turtle()

# for k in range(4):
#     sal.forward(100)
#     sal.left(90)
#     sal.forward(40)
#     sal.left(90)
#     sal.forward(100)
#     sal.right(90)


#1
# s = "Sakura"
# a = "Anh"
# k = "shogo"
# print(f'The students in our team are {s} and {a} and {k}')

# #2
# cents = int(input("How many cents you want to change?: "))
# q = cents//25
# n = (cents - 25 *q) // 5
# p = (cents -25 * q - 5*n)
# print(f'You can receive {q} quarter(s) and {n} Nikel(s) and {p} Penny(s)')

# mylist = [6, -2, 1, 3]
# sum = 0
# for j in mylist:
#     sum = sum + j
#     average = sum / len(mylist)
# print("Sum", sum)  
# print("Average", average)  

# sum = 0
# for j in range(1, 101):
#     sum = sum + j
# print(sum)

# N=100
# sum_acc = 0 
# for j in range(N + 1):
#     sum_acc = sum_acc + j
# print(f'Sum {sum_acc}')

# print(N*(N+1)/2)

# N = 100
# sum_harmonic = 0

# for i in range(1, N+1):
#     sum_harmonic += 1 / i

# result = round(sum_harmonic, 5)
# print(result)

# print(list(range(5,0)))
# a = 1
# for i in range(1,3):
#     a = a + 2
#     b = 3 * i
#     print(i, a, b)
# x = 3
# for i in range(2):
#     y = 3 + x
#     x = x - y
#     print(i, x, y)

# for i in ['hi', 'bye']:
#     print(i)
# for i in ['hi', 'bye']:
#     print('i')

# print(17%3)

# import turtle

# sam=turtle.Turtle()

# sam.left(90)
# sam.forward(100)
# sam.left(90)
# sam.forward(40)
# sam.right(30)
# sam.forward(100)

# myList=["cat", "hamster", "dog"]
# for animal in myList:
#     print(f"I have a {animal}")

# for i in range(2):
#     print('HEllo')

# for i in [2]:
#     print("Hello")

# # ユーザーに整数を入力してもらう
# user_input = int(input("number: "))

# # 入力された数に10を足す
# result = user_input + 10

# # 結果を表示する
# print(result)

# x=3
# y=5
# print("There are ", str(x), "dogs and", str(y), "cats.")

# import turtle

# alex = turtle.Turtle()

# for k in range(4):
#     alex.forward(100)
#     alex.left(90)
    

# import turtle

# alex = turtle.Turtle()

# alex.speed(0)
# for k in range(1,25):
#     alex.forward(k*7)  
#     alex.left(90)  

# turtle.done()

# import turtle
# wn = turtle.Screen()
# gwen = turtle.Turtle()

# wn.bgcolor("light green")
# gwen.shape("turtle")
# gwen.pensize(3)
# gwen.color("blue")

# gwen.stamp()  
# gwen.penup()

# dist = 150

# for i in range(12):
#     gwen.forward(dist)

#     gwen.pendown()
#     gwen.forward(10)  
#     gwen.penup()
#     gwen.forward(10)

#     gwen.stamp()  

#     gwen.goto(0, 0)  

#     gwen.left(360 / 12) 


# import turtle
# wn = turtle.Screen()
# tracy = turtle.Turtle()

# # draw a cross
# long = 100
# short = 40

# # add colors to lines
# for n in ["black", "blue", "red", "lightgreen"]:
#     tracy.color(n)
#     tracy.forward(long)
#     tracy.left(90)
#     tracy.forward(short)
#     tracy.left(90)
#     tracy.forward(long)
#     tracy.right(90)

# import turtle

# # ウィンドウとタートルの設定
# wn = turtle.Screen()
# tracy = turtle.Turtle()

# # 十字架のサイズを定義
# long = 100
# short = 40

# # 塗りつぶしの色をマゼンタに設定
# tracy.fillcolor("magenta")

# # 塗りつぶしの開始
# tracy.begin_fill()

# # 線の色を変えながら十字架を描画
# for n in ["black", "blue", "red", "lightgreen"]:
#     tracy.color(n)
#     tracy.forward(long)
#     tracy.left(90)
#     tracy.forward(short)
#     tracy.left(90)
#     tracy.forward(long)
#     tracy.right(90)

# # 塗りつぶしの終了
# tracy.end_fill()

# # 終了処理（ウィンドウをクリックで閉じる）
# wn.mainloop()




# import turtle

# # ウィンドウとタートルの設定
# wn = turtle.Screen()
# tracy = turtle.Turtle()
# tracy.speed(3)  # 描画速度を調整
# tracy.pensize(3)

# colors = ["blue", "magenta", "yellow", "orange", "green"]

# long_length = 100  
# short_length = 40  
# outer_angle = 30  
# inner_angle = 60  

# tracy.color("black")
# tracy.setheading(180)  
# tracy.forward(long_length)

# for i in range(0, len(colors)):
#     tracy.color(colors[i])
    
#     tracy.right(outer_angle)
#     tracy.forward(short_length)
    
#     tracy.left(inner_angle)
#     tracy.forward(short_length)
# tracy.setheading(0)  
# tracy.color("black")
# tracy.forward(long_length)

# wn.mainloop()

# Got itifasdfdaskfdsa;kfkldsajfljdsaklfjads;kljfkdjsaklf;jdsakljfkldsajfkdasjfadsfkdasjfkl;adsfjdsakf
# import turtle

# wn = turtle.Screen()
# tracy = turtle.Turtle()
# tracy.speed(3)  
# tracy.pensize(3)

# colors = ["blue", "magenta", "yellow", "orange", "green"]

# long_length = 100  # 最初と最後の水平線の長さ
# short_length = 40  # 短い斜めの線の長さ
# outer_angle = 30  # 外側の角度 30度
# inner_angle = 60  # 内側の角度 60度

# tracy.color("black")
# tracy.setheading(180)  
# tracy.forward(long_length)

# # ジグザグ部分を描く（垂直に下方向へ進む）
# # for i in range(len(colors)):
# #     tracy.color(colors[i])
    
# tracy.left(180 - outer_angle)
# tracy.forward(short_length)
    
# tracy.right(180 - inner_angle)
# tracy.forward(short_length)

# tracy.left(180 - inner_angle)
# tracy.forward(short_length)

# tracy.right(180 - inner_angle)
# tracy.forward(short_length)
# tracy.left(180 - inner_angle)
# tracy.forward(short_length)

# tracy.right(180 - inner_angle)
# tracy.forward(short_length)

# tracy.left(180 - inner_angle)
# tracy.forward(short_length)

# tracy.right(180 - inner_angle)
# tracy.forward(short_length)

# tracy.left(180 - inner_angle)
# tracy.forward(short_length)

# tracy.right(180 - inner_angle)
# tracy.forward(short_length)



# tracy.setheading(0)  
# tracy.color("black")
# tracy.forward(long_length)


# wn.mainloop()

# import turtle

# # ウィンドウとタートルの設定
# wn = turtle.Screen()
# tracy = turtle.Turtle()
# tracy.speed(3)  # 描画速度を調整
# tracy.pensize(3)

# # 各ジグザグの色のリスト
# colors = ["blue", "magenta", "yellow", "orange", "green"]

# # 線の長さと角度の設定
# long_length = 100  # 最初と最後の水平線の長さ
# short_length = 40  # 短い斜めの線の長さ
# outer_angle = 30  # 外側の角度 30度
# inner_angle = 60  # 内側の角度 60度

# # 最初の黒い線を左向きに描く（西）
# tracy.color("black")
# tracy.setheading(180)  # 西（左）向きに設定
# tracy.forward(long_length)

# # ジグザグ部分を描く（垂直に下方向へ進む）
# for color in colors:
#     tracy.color(color)
    
#     # 30度で左に傾きながら下に進む
#     tracy.left(180 - outer_angle)
#     tracy.forward(short_length)
    
#     # 60度で右に傾きながらさらに下に進む
#     tracy.right(180 - inner_angle)
#     tracy.forward(short_length)

# # 最後の黒い線を右向きに描く（東）
# tracy.setheading(0)  # 東（右）向きにセット
# tracy.color("black")
# tracy.forward(long_length)

# # ウィンドウを閉じないように待機
# wn.mainloop()

# import turtle

# wn = turtle.Screen()
# tracy = turtle.Turtle()
# tracy.speed(3) 
# tracy.pensize(3)


# colors = ["blue", "magenta", "yellow", "orange", "green"]


# long_length = 100  # 最初と最後の水平線の長さ
# short_length = 40  # 短い斜めの線の長さ
# outer_angle = 30  # 外側の角度 30度
# inner_angle = 60  # 内側の角度 60度


# tracy.color("black")
# tracy.setheading(180)  
# tracy.forward(long_length)

# tracy.color(colors[0])
# tracy.left(180 - outer_angle)  
# tracy.forward(short_length)
# tracy.right(180 - inner_angle)  
# tracy.forward(short_length)

# tracy.color(colors[1])
# tracy.left(180 - inner_angle)  
# tracy.forward(short_length)
# tracy.right(180 - inner_angle)  
# tracy.forward(short_length)

# tracy.color(colors[2])
# tracy.left(180 - inner_angle)  
# tracy.forward(short_length)
# tracy.right(180 - inner_angle)  
# tracy.forward(short_length)

# tracy.color(colors[3])
# tracy.left(180 - inner_angle)  
# tracy.forward(short_length)
# tracy.right(180 - inner_angle)  
# tracy.forward(short_length)

# tracy.color(colors[4])
# tracy.left(180 - inner_angle)  
# tracy.forward(short_length)
# tracy.right(180 - inner_angle)  
# tracy.forward(short_length)

# tracy.setheading(0)  
# tracy.color("black")
# tracy.forward(long_length)

# wn.mainloop()


# import turtle

# wn = turtle.Screen()
# gwen = turtle.Turtle()

# wn.bgcolor("light green")  
# gwen.shape("turtle")  
# gwen.pensize(3)  
# gwen.color("blue")  

# gwen.penup()  

# dist = 150  

# for i in range(10):
#     gwen.forward(dist)  
    
#     gwen.left(90)  
#     gwen.stamp()  
    
#     gwen.right(90)  
#     gwen.goto(0, 0) 
#     gwen.left(360 / 10)  

# gwen.hideturtle()

# turtle.done()

# import turtle
# leo = turtle.Turtle()
# wn = turtle.Screen()
# leo.speed(5) 
# leo.pensize(3)

# l_length = 100  
# m_length = 50
# s_length = 35
# l_angle = 60
# s_angle = 30
# m_angle = 90

# for j in range(1, 5):
#     for k in range(5):
#         leo.left(s_angle)
#         leo.forward(l_length)
#         leo.right(180- l_angle)
#         leo.forward(m_length)
#         leo.right(m_angle)
#         leo.forward(s_length)
#         leo.left(180)
#     leo.penup()
#     leo.goto(0, -60*j)
#     leo.pendown()
    

# wn.mainloop()

# for j in range(5):
#     print(j, end=' ')

# ユーザーに現在の時刻を入力してもらう
# current_time_string = input("What is the current time (in hours)? ")

# # ユーザーに待機時間を入力してもらう
# waiting_time_string = input("How many hours do you have to wait? ")

# # 入力された文字列を整数に変換
# current_time_int = int(current_time_string)
# waiting_time_int = int(waiting_time_string)

# # 現在の時刻に待機時間を足して、新しい時刻を計算
# hours = current_time_int + waiting_time_int

# # 24時間制の時間を計算
# timeofday = hours % 24

# # 計算されたアラーム時刻を出力
# print(timeofday)

# word1 = "All"
# word2 = "work"
# word3 = "and"
# word4 = "no"
# word5 = "play"
# word6 = "makes"
# word7 = "Jack"
# word8 = "a"
# word9 = "dull"
# word10 = "boy."

# print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

# # ユーザーに出発する曜日（0～6）を入力してもらう
# start_day = int(input("出発する曜日の番号を入力してください（0: 日曜日、1: 月曜日、2: 火曜日、... 6: 土曜日）: "))

# # 滞在日数を入力してもらう
# stay_length = int(input("滞在日数を入力してください: "))

# # 帰宅する曜日を計算（曜日の範囲は0～6なので7で剰余を取る）
# return_day = (start_day + stay_length) % 7

# # 結果を出力
# print(f"あなたが帰宅する曜日の番号は {return_day} です。")

# P = 10000
# n = 12
# r = 0.08

# t = int(input("Compound for how many years? "))

# final = P * ((1 + (r/n))**n*t)

# print ("The final amount after", t, "years is", final)

# ( ((1 + (r/n)) ** (n * t)) )

# width = int(input("Width? "))
# height = int(input("Height? "))

# area = width * height

# print("The area of the rectangle is", area)

# import math

# # ユーザーに半径を入力してもらう
# radius = float(input("円の半径を入力してください: "))

# # 円の面積を計算（面積 = π * 半径^2）
# area = math.pi * (radius ** 2)

# # 結果を出力
# print(f"半径 {radius} の円の面積は {area:.2f} です。")

# deg_c = int(input("What is the temperature in Celsius? "))

# # formula to convert C to F is: (degrees Celcius) times (9/5) plus (32)
# deg_f = deg_c * (9 / 5) + 32


# deg_f = int(input("What is the temperature in Farenheit? "))

# deg_c = (deg_f - 32) * (5 / 9) 

# print(deg_f, " degrees Farenheit is", deg_c, " degrees Celsius.")

# for i in range(100):
#     print("We like Python's turtles!")

# for amonth in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']:
#     print("One of the months of the year is", amonth)

# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# # 各数字を新しい行に出力
# for number in numbers:
#     print(number)

# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# # 各数字とその平方を新しい行に出力
# for number in numbers:
#     print(f"{number} - {number**2}")

# draw an equilateral triangle
# import turtle

# wn = turtle.Screen()
# norvig = turtle.Turtle()

# for i in range(3):
#     norvig.forward(100)

#     # the angle of each vertice of a regular polygon
#     # is 360 divided by the number of sides
#     norvig.left(360/3)

# wn.exitonclick()

# draw a square
# import turtle

# wn = turtle.Screen()
# kurzweil = turtle.Turtle()

# for i in range(4):
#     kurzweil.forward(100)
#     kurzweil.left(360/4)

# wn.exitonclick()

# draw a hexagon
# import turtle

# wn = turtle.Screen()
# dijkstra = turtle.Turtle()

# for i in range(6):
#     dijkstra.forward(100)
#     dijkstra.left(360/6)

# wn.exitonclick()

# draw an octogon
import turtle

wn = turtle.Screen()
knuth = turtle.Turtle()

for i in range(8):
    knuth.forward(75)
    knuth.left(360/8)

wn.exitonclick()



