#!/usr/bin/python
#encoding=utf8
# 石头0 剪刀1 布2
import random
while 1: 
	#玩家输入
	playerInput = raw_input("石头0 剪刀1 布2 :")
	player = int(playerInput)
	#电脑随机数
	mac = random.randint(0,2)

	if player>2:
		print("输入不合法!")
		#exit()
		continue
	print("player: %d  mac: %d"%(player, mac))
	if player==0 and mac==1 or player==1 and mac==2 or player==2 and mac==0 :
		print("恭喜你💐，赢了！！")
	elif player == mac :
		print("不要走，决战到天亮, 平局")
	else:
		print("再接再厉，输了！")
