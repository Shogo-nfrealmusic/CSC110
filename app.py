# age = 20
# age = 30
# print(age)

# name = input("What is your name? ")
# age = input("How old are you? ")
# print(f'New patient {name} {age}years old')



# import turtle
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)

# a,b,c = 100, 50, 35

# for n in range(1,5):
#     for i in range(5):
#         t.left(30)
#         t.forward(a)
#         t.right(180-60)
#         t.forward(b)
#         t.left(90)
#         t.backward(c)
        
#     t.penup()
#     t.goto(0, -60 * n)
#     t.pendown()
    


# wn.bgcolor("lightgreen")
# t.shape("turtle")
# t.pensize(3)
# t.color("blue")

# t.stamp()
# t.penup()

# dist = 150

# for i in range(12):
#     t.forward(dist)
#     t.pendown()
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.stamp()
#     t.goto(0,0)
#     t.left(360/12)
    

# for i in range(1,25):
#     t.forward(7 * i)
#     t.left(90)



# long = 100
# short = 40

# t.fillcolor("magenta")
# t.begin_fill()

# for i in range(4):
#     t.forward(long)
#     t.left(90)
#     t.forward(short)
#     t.left(90)
#     t.forward(long)
#     t.right(90)

# t.end_fill()






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
# import turtle

# wn = turtle.Screen()
# knuth = turtle.Turtle()

# for i in range(8):
#     knuth.forward(75)
#     knuth.left(360/8)

# wn.exitonclick()

# import turtle

# # ユーザー入力を最初に取得
# num_sides = int(input("Enter the number of sides: "))  # 辺の数
# side_length = int(input("Enter the length of each side: "))  # 辺の長さ
# line_color = input("Enter the color of the polygon's outline: ")  # 枠線の色
# fill_color = input("Enter the fill color of the polygon: ")  # 塗りつぶしの色

# # ウィンドウとタートルの作成を後にする
# wn = turtle.Screen()
# polygon = turtle.Turtle()

# # ペンの色と塗りつぶしの色を設定
# polygon.color(line_color)
# polygon.fillcolor(fill_color)

# # 塗りつぶし開始
# polygon.begin_fill()

# # 正多角形を描画
# for _ in range(num_sides):
#     polygon.forward(side_length)
#     polygon.left(360 / num_sides)

# # 塗りつぶし終了
# polygon.end_fill()

# # ウィンドウをクリックで閉じる
# wn.exitonclick()

# import turtle

# # ウィンドウを設定
# wn = turtle.Screen()

# # タートル（酔っぱらいの海賊）を作成
# pirate = turtle.Turtle()

# # 実験データ（角度のリスト）
# angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# # 海賊が歩き回る
# for angle in angles:
#     pirate.left(angle)  # 左に回転（正の角度は反時計回り、負の角度は時計回り）
#     pirate.forward(100)  # 100ステップ進む

# # 現在のヘッディング（向き）を出力
# print("The pirate's current heading is:", pirate.heading())

# # ウィンドウをクリックで閉じる
# wn.exitonclick()


# import turtle

# turing = turtle.Turtle()

# for i in range(5):
#     turing.forward(110)
#     turing.left(216)

# import turtle
# wn = turtle.Screen()
# k = turtle.Turtle()

# wn.bgcolor("light green")
# k.shape("turtle")
# k.pensize(3)
# k.color("blue")

# k.stamp()
# k.penup()
# dist = 150

# for i in range(12):
#     k.forward(dist)
#     k.pendown()
#     k.forward(10)
#     k.penup()
#     k.forward(10)
#     k.stamp()
#     k.goto(0,0)
#     k.left(360/12)

# import turtle

# tanenbaum = turtle.Turtle()

# tanenbaum.hideturtle()
# tanenbaum.speed(20)

# for i in range(350):
#     tanenbaum.forward(i)
#     tanenbaum.right(9


# import turtle
# sal = turtle.Turtle()
# wn = turtle.Screen()

# d = 100

# for i in range(4):
#     sal.forward(d)
#     sal.right(180-60)
#     sal.forward(2 * d)
#     sal.left(30)
    
# wn.exitonclick()

# import random

# print(random.randrange(6))

# print(random.randint(1,5))

# import random

# print(random.random())

import random

# print(random.randint(1,6))

# for i in range(10):
#     print(random.randint(0,1))

# for i in range(3):
#     print(random.randint(1,6))

# for i in range(10):
#     print(random.random() * 5)
    

# print(random.random() * 10 - 5)

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5 / 9
#     return celsius

# # テスト例
# fahrenheit_temp = 100  # 例えば華氏100度
# celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
# print(f"{fahrenheit_temp}F は {celsius_temp:.2f}C です。")

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(5))  

# def table_of_fact(n_rows):
#     for k in range(1, n_rows+1):
#         print(k, factorial(k))

# table_of_fact(10)

# import turtle

# def triangle(t, side, color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(3):
#         t.forward(side)
#         t.left(120)
#     t.end_fill()
        
# leo = turtle.Turtle()
# length=70
# for k in ["yellow", "blue", "red"]:
#     triangle(leo, length, k)
#     leo.forward(length)

# turtle.done()  # ウィンドウが閉じないようにします

# import math

# def factorial(n):
#     f = 1
#     for j in range(1 , n + 1):
#         f=f*j
#     return f
# def e_x_series(x , n):
#     sum_accu=0
#     for k in range(n):
#         sum_accu=sum_accu + x**k / factorial(k)
#     return sum_accu

# print(e_x_series(1,10))
# print(math.e)

# x = 2
# y = 3
# var = x < y
# print(var)

# x = 5
# print((3 + x) < 7)

# f1 = 0
# f2 = 1
# fList = [f1, f2]
# # print(f1, f2)

# for i in range(8):
#     fsum = f1 + f2
#     f1 = f2
#     f2 = fsum
#     fList.append(fsum)
    
# print(fList)

# def fibonacci(Nfib):
#     f1 = 0
#     f2 = 1
#     fList = [f1, f2]

#     for i in range(8):
#         fsum = f1 + f2
#         f1 = f2
#         f2 = fsum
#         fList.append(fsum)
        
#     return fList

# result = fibonacci(8)
# print(result)
# print(sum(result))

# animals = ["cat", "dog", "rabbit"]
# animals.append("guinea  pig")
# print(f'Update animals list: {animals}')

# def febonacci(num):
#     f1 = 0
#     f2 = 1
#     fList = [f1, f2]
    
#     for i in range(num):
#         fsum = f1 + f2
#         f1 = f2
#         f2 = fsum
#         fList.append(fsum)
    
#     return fList
# result = febonacci(8)
# print(result)

# num1 = float(input("Enter number: "))
# num2 = float(input("Enter number: "))

# if(num1 > num2):
#     print(f'largerValue = {num1}')
# else:
#     print(f'largerValue = {num2}')

# evens = []
# odds = []
# others = []

# for i in range(1, 21):
#     if i % 2 == 0:
#         evens.append(str(i))
#     elif i % 3 == 0:
#         odds.append(str(i))
#     else:
#         others.append(str(i))

# print("even:", " ".join(evens))
# print("odds:", " ".join(odds))
# print("others:", " ".join(others))

# both = []
# either = []
# neither = []

# for n in range(1, 21):
#     if n % 2 == 0 and n % 3 == 0:
#         both.append(str(n))

# for n in range(1, 21):
#     if n % 2 == 0 or n % 3 == 0:
#         either.append(str(n))

# for n in range(1, 21):
#     if not (n % 2 == 0 or n % 3 == 0):
#         neither.append(str(n))

# print("Both (divisible by 2 and 3):", " ".join(both))
# print("--------------------------")
# print("Either (divisible by 2 or 3):", " ".join(either))
# print("--------------------------")
# print("Neither (not divisible by 2 or 3):", " ".join(neither))



# import turtle
# t = turtle.Turtle()
# screen = turtle.Screen()
# t.speed(5)
# sz = 50

# def draw_square(t, sz):
#     for _ in range(4):
#         t.forward(sz)
#         t.right(90)

# def draw_cube_net(t, sz):
    
#     # 中央の正方形を描く
#     draw_square(t, sz)
    
#     # 上の正方形を描く
#     t.penup()
#     t.goto(0, sz)
#     t.pendown()
#     draw_square(t, sz)
    
#     # 下の正方形を描く
#     t.penup()
#     t.goto(0, -sz)
#     t.pendown()
#     draw_square(t, sz)
    
#     # 左の正方形を描く
#     t.penup()
#     t.goto(-sz, 0)
#     t.pendown()
#     draw_square(t, sz)
    
#     # 右の正方形を描く
#     t.penup()
#     t.goto(sz, 0)
#     t.pendown()
#     draw_square(t, sz)
    
#     # 下の下に正方形を描く
#     t.penup()
#     t.goto(0, -2 * sz)
#     t.pendown()
#     draw_square(t, sz)
    

# import turtle
# t = turtle.Turtle()
# screen = turtle.Screen()
# t.speed(5)
# sz = 50

# def draw_square(t, sz):
#     for _ in range(4):
#         t.forward(sz)
#         t.right(90)
        
# def draw_tab(t,sz):
#     t.forward(sz)
#     t.left(120)
#     t.forward()
    

# def draw_cube_net(t, sz):
    
#     # 中央の正方形を描く
#     draw_square(t, sz)
    
#     # 上の正方形を描く
#     t.penup()
#     t.goto(0, sz)
#     t.pendown()
#     draw_square(t, sz)
    
#     # 下の正方形を描く
#     t.penup()
#     t.goto(0, -sz)
#     t.pendown()
#     draw_square(t, sz)
    
#     # 左の正方形を描く
#     t.penup()
#     t.goto(-sz, 0)
#     t.pendown()
#     draw_square(t, sz)
    
#     # 右の正方形を描く
#     t.penup()
#     t.goto(sz, 0)
#     t.pendown()
#     draw_square(t, sz)
    
#     # 下の下に正方形を描く
#     t.penup()
#     t.goto(0, -2 * sz)
#     t.pendown()
#     draw_square(t, sz)
    

# import turtle
# t = turtle.Turtle()
# screen = turtle.Screen()

# def draw_square(t, sz):
#     for _ in range(4):
#         t.forward(sz)
#         t.right(90)

# def draw_cube_net(t, sz):
    
#     draw_square(t, sz)
    
#     t.penup()
#     t.goto(0, sz)
#     t.pendown()
#     draw_square(t, sz)
    
#     t.penup()
#     t.goto(0, -sz)
#     t.pendown()
#     draw_square(t, sz)
    
#     t.penup()
#     t.goto(-sz, 0)
#     t.pendown()
#     draw_square(t, sz)
    
#     t.penup()
#     t.goto(sz, 0)
#     t.pendown()
#     draw_square(t, sz)
    
#     t.penup()
#     t.goto(0, 2 * sz)
#     t.pendown()
#     draw_square(t, sz)

# def cubeTab(t,sz,L):
#     import math
#     t.left(60)
#     t.forward(L)
#     t.right(60)
#     t.forward(sz-2*L*math.cos(math.radians(60)))
#     t.right(60)
#     t.forward(L)
    

# sz = 50
# L = 10
# draw_cube_net(t, sz)
# t.goto(0, sz*2)
# cubeTab(t, sz, L)
# t.right(210)
# t.penup()
# t.goto(0, 0)
# t.pendown()
# cubeTab(t, sz, L)
# t.right(120)
# t.penup()
# t.goto(sz, sz)
# t.pendown()
# cubeTab(t, sz, L)
# t.right(120)
# t.penup()
# t.goto(-sz, -sz)
# t.pendown()
# cubeTab(t, sz, L)
# t.right(120)
# t.penup()
# t.goto(sz * 2, 0)
# t.pendown()
# cubeTab(t, sz, L)
# t.right(120)
# t.penup()
# t.goto(0, -sz * 2)
# t.pendown()
# cubeTab(t, sz, L)
# t.right(120)
# t.penup()
# t.goto(sz, -sz)
# t.pendown()
# cubeTab(t, sz, L)


# turtle.done()



# def square(t,sz):
#     for i in range(4):
#         t.forward(sz)
#         t.left(90)

# def cubeTab(t,sz,L):
#     import math
#     t.goto(0,sz)
#     t.left(60)
#     t.forward(L)
#     t.right(60)
#     t.forward(sz-2*L*math.cos(math.radians(60)))
#     t.right(60)
#     t.forward(L)

# def B_tabs(t,sz,L):
#     # t.speed(5)
#     t.up()
#     t.goto(0,0)
#     t.right(30)
#     t.down()
#     square(t, sz)
#     t.forward(sz)
#     cubeTab(t, sz , L)
#     # t.left(60)
#     # t.down()
#     # for i in range(3):
#     #     t.right(90)
#     #     t.forward(sz)
#     # t.left(120)
#     # t.forward(L)
#     # t.left(60)
#     # t.forward(sz-2*L*math.cos(math.radians(60)))
#     # t.left(60)
#     # t.forward(L)

#     # t.left(30)
#     # t.forward(sz)
#     # t.left(30)
#     # t.forward(L)
#     # t.left(60)
#     # t.forward(sz-2*L*math.cos(math.radians(60)))
#     # t.left(60)
#     # t.forward(L)
    
# import turtle
# import math
# t = turtle.Turtle()
# square(t,100)
# cubeTab(t,100,10)
# B_tabs(t,100,10)
# turtle.done()

# import turtle
# import math

# t = turtle.Turtle()
# screen = turtle.Screen()
# t.speed(0)  

# def draw_square(t, sz):
#     for _ in range(4):
#         t.forward(sz)
#         t.right(90)

# def draw_cube_net(t, sz):
#     draw_square(t, sz)
    
#     positions = [(0, sz), (0, -sz), (-sz, 0), (sz, 0), (0, 2 * sz)]
#     for x, y in positions:
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#         draw_square(t, sz)

# def cubeTab(t, sz, L):
#     t.left(60)
#     t.forward(L)
#     t.right(60)
#     t.forward(sz - 2 * L * math.cos(math.radians(60)))
#     t.right(60)
#     t.forward(L)

# sz = 50
# L = 10

# draw_cube_net(t, sz)

# tab_positions = [
#     (0, sz * 2, 0), (0, 0, 210), (sz, sz, 120),
#     (-sz, -sz, 120), (sz * 2, 0, 120), (0, -sz * 2, 120), (sz, -sz, 120)
# ]

# for x, y, angle in tab_positions:
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.right(angle)
#     cubeTab(t, sz, L)

# turtle.done()

# def fun1(x):
#     return x **2

# x = 6
# print(fun1(3)/fun1(2))
# print(fun1(x/2))

# import turtle

# def squareFun(t, length):
#     for i in range(4):
#         t.forward(length)
#         t.left(90)

# leo = turtle.Turtle()

# for i in range(3):
#     squareFun(leo, 50)
#     leo.forward(50)

# def funct(N):
#     y = 0
#     for i in range(N):
#         rand_num = random.randint(1, 5)
#         print(rand_num)
#         y = y + rand_num
#     return y

# print(funct(3))

# import turtle
# import math

# t = turtle.Turtle()
# screen = turtle.Screen()
# t.speed(0)  

# def draw_square(t, sz):
#     for _ in range(4):
#         t.forward(sz)
#         t.right(90)

# def draw_cube_net(t, sz):
#     draw_square(t, sz)
    
#     positions = [(0, sz), (0, -sz), (-sz, 0), (sz, 0), (0, 2 * sz)]
#     for x, y in positions:
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#         draw_square(t, sz)

# def cubeTab(t, sz, L):
#     t.left(60)
#     t.forward(L)
#     t.right(60)
#     t.forward(sz - 2 * L * math.cos(math.radians(60)))
#     t.right(60)
#     t.forward(L)

# sz = 50
# L = 10

# draw_cube_net(t, sz)

# tab_positions = [
#     (0, sz * 2, 0), (0, 0, 210), (sz, sz, 120),
#     (-sz, -sz, 120), (sz * 2, 0, 120), (0, -sz * 2, 120), (sz, -sz, 120)
# ]

# for x, y, angle in tab_positions:
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.right(angle)
#     cubeTab(t, sz, L)

# turtle.done()

# # 2
# import turtle
# import math

# def square(t, sz):
#     for _ in range(4):
#         t.forward(sz)
#         t.right(90)

# def cubeTab(t, sz, L):
#     t.left(60)  
#     t.forward(L)
#     t.right(60)  
#     t.forward(sz - 2 * L * math.cos(math.radians(60)))  
#     t.right(60)  
#     t.forward(L)


# def B_with_tabs(t, sz, L):
#     square(t, sz)  
#     t.right(90)
#     t.forward(sz)
#     t.right(180)
#     cubeTab(t,sz,L)
#     t.right(30)
#     t.forward(sz)
#     t.right(90)
#     cubeTab(t, sz, L)
    

# t = turtle.Turtle()
# sz = 50  
# L = 10  
# B_with_tabs(t, sz, L)
# turtle.done()



# n1 = float(input("Enter number1: "))
# n2 = float(input("Enter number2: "))
# n3 = float(input("Enter number3: "))

# Max = n1
# if n2 > Max:
#     Max = n2
# if n3 > Max:
#     Max = n3
# print(Max)

# myNum=7
# answer=input("What to play? yes/no: ")
# if answer == 'yes':
#     number = int(input('Number 1-10: '))
#     if number == myNum:
#         print("It's correct")
#     else:
#         print(f"You're wrong. The answer is {myNum}")
# else:
#     print('bye')

# def isFactor(f,n):
#     return n % f == 0

# n = 60
# factors = [f for f in range(2, n) if isFactor(f, n)]
# print("Factors of 60 greater than 1 and less than 60:", factors)

# isFactor関数の定義（前の問題と同様）
def isFactor(f, n):
    return n % f == 0

# listOfFactorsOf関数の定義
def listOfFactorsOf(n):
    return [f for f in range(2, n) if isFactor(f, n)]

# 11から20までの整数とその因数のテーブルを表示
for num in range(11, 21):
    factors = listOfFactorsOf(num)
    print(f"Factors of {num}: {factors}")

    



   


   




        

    

    







