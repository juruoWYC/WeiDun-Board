import serial
import re
import time

author='maiti,Xidian University maiti@stu.xidian.edu.cn'


port=serial.Serial('/dev/ttyAMA0',baudrate=9600)#,timeout=3.0

def str_cmp(str1,str2):
	return str1.lower()==str2.lower()	
	

def connect_init():	
	aa=True
	port.flushInput()  #clear memory
	while(aa):
		if(port.inWaiting() > 10):
			_input=port.read(11)  	
			print(_input)
			#new_str=_input[:len(_input)-2]		
			#if(str_cmp(new_str,'Connected')==True):	
			if _input.find('Connected'):	
				print ('Connection established')
				aa=False

def cmd_1():
	port.flushInput()  #clear memory
	port.write('+++')
	aa=True
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(1)  #once most read 20 character 			
			print(_input)       #'a'
			#new_str=_input[:len(_input)-2]	#remove the two last char	
			if(str_cmp(_input,'a')==True):  #/x61 is 'a'	
				#port.write('a')  #'/x61'
				print('ok_1')     # 'a' is matched	
				aa=False

def cmd_2():    #+ok
	aa=True
	port.write('a')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(5)
			print(_input)
			if _input.find('+ok'):  #/x61 is 'a'	
				print('+ok matched') 
				aa=False           
		
def cmd_AT_1():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+WKMOD\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_1') 
				aa=False	

def cmd_AT_2():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+SOCKA\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_2') 
				aa=False

def cmd_AT_3():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+SOCKPORTA\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_3') 
				aa=False

def cmd_AT_4():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+SOCKBEN\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_4') 
				aa=False

def cmd_AT_5():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+SOCKPORTA\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_5') 
				aa=False

def cmd_AT_6():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+SOCKB\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_6') 
				aa=False

def cmd_AT_7():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+SOCKPORTB\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_7') 
				aa=False

def cmd_AT_8():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+HEARTEN\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_8') 
				aa=False

def cmd_AT_9():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+HEARTTM\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_9') 
				aa=False

def cmd_AT_10():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+HEARTTP\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_10') 
				aa=False


def cmd_AT_11():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+HEARTDT\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_11') 
				aa=False

def cmd_AT_12():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+REGEN\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_12') 
				aa=False

def cmd_AT_13():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+REGTCP\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_13') 
				aa=False

def cmd_AT_14():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+REGUSR\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_14') 
				aa=False

def cmd_AT_15():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+NCDP\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_15') 
				aa=False

def cmd_AT_16():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+COAPRPY\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_16') 
				aa=False

def cmd_AT_17():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+UART\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_17') 
				aa=False

def cmd_AT_18():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+UARTTL\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_18') 
				aa=False

def cmd_AT_19():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+UATEN\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_19') 
				aa=False

def cmd_AT_20():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+CMDPW\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_20') 
				aa=False

def cmd_AT_21():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+STMSG\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_21')
				aa=False

def cmd_AT_22():
	aa=True
	port.flushInput()  #clear memory
	port.write('AT+S\x0D\x0A')
	while(aa):
		if(port.inWaiting() > 0):
			_input=port.read(20)  #once most read 20 character 			
			print(_input)	
			if _input.find('OK'):
				print('AT_22')
				aa=False

def Send(data):  
	port.flushInput()  #clear memory
	port.write(data)

def Recv():
	aa=True
	while(aa):
		if(port.inWaiting() > 0):
			return port.read(20)  			
			aa=False	


def NB_IOT_INIT():
	connect_init()  #connected
	time.sleep(0.5)  #0.5s  
	cmd_1()      #'+++' 'a'
	time.sleep(0.5)  #0.5s  
	cmd_2()         
	time.sleep(0.5)  #0.5s  
	cmd_AT_1()
	time.sleep(0.5)  #0.5s
	cmd_AT_2()
	time.sleep(0.5)  #0.5s
	cmd_AT_3()
	time.sleep(0.5)  #0.5s
	cmd_AT_4()
	time.sleep(0.5)  #0.5s
	cmd_AT_5()
	time.sleep(0.5)  #0.5s
	cmd_AT_6()
	time.sleep(0.5)  #0.5s
	cmd_AT_7()
	time.sleep(0.5)  #0.5s
	cmd_AT_8()
	time.sleep(0.5)  #0.5s
	cmd_AT_9()
	time.sleep(0.5)  #0.5s
	cmd_AT_10()
	time.sleep(0.5)  #0.5s
	cmd_AT_11()
	time.sleep(0.5)  #0.5s
	cmd_AT_12()
	time.sleep(0.5)  #0.5s
	cmd_AT_13()
	time.sleep(0.5)  #0.5s
	cmd_AT_14()
	time.sleep(0.5)  #0.5s
	cmd_AT_15()
	time.sleep(0.5)  #0.5s
	cmd_AT_16()
	time.sleep(0.5)  #0.5s
	cmd_AT_17()
	time.sleep(0.5)  #0.5s
	cmd_AT_18()
	time.sleep(0.5)  #0.5s
	cmd_AT_19()
	time.sleep(0.5)  #0.5s
	cmd_AT_20()
	time.sleep(0.5)  #0.5s
	cmd_AT_21()
	time.sleep(0.5)  #0.5s
	cmd_AT_22()
	time.sleep(0.5)  #0.5s
