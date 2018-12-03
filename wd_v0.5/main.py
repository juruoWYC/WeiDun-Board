import connect
import time
import spi

#inital
#connect.NB_IOT_INIT()
spi.SPI_init()

while True:
                #SPI read
	st,at,h=spi.SPI_read([0xA0])
	print('soil temp:',st)
	print('air temp:',at)
	print('humidity:',h)

                #display
                
	#NBIOT updata
	#connect.Send('hello')
	#print('send:hello')
	#print(connect.Recv())
	
	time.sleep(5) #at least 2s  10s is ok
