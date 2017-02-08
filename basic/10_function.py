#!/usr/bin/python
#encoding=utf8

def displayMenu():
	print("-"*30)
	print("    名片管理系统   V1.0.1")
	print("      1. 添加名片")
	print("      2. 删除名片")
	print("      3. 修改名片")
	print("      4. 查询名片")
	print("      5. 遍历所有名片")
	print("      6. 退出系统")
	print("-"*30)

def appRun():
	displayMenu();
	while(True):
		selectFun = input("请输入序号：");
		selectFun = int(selectFun);
		if(selectFun == 1):
			addProfile();
		elif(selectFun==2):
			delProfile();
		elif(selectFun==3):
			modifyProfile();
		elif(selectFun==4):
			selProfile();
		elif(selectFun==5):
			selAllProfile();
		else:
			break;

def addProfile():
	print("add profile")

def delProfile():
	print("delete profile")

def modifyProfile():
	print("modify profile")

def selProfile():
	print("select profile")

def selAllProfile():
	print("select all profile")

#def exitApp():
#	break;

appRun();
