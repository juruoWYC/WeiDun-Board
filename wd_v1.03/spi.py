#
# for stm32 
# adding light sensor 
import spidev
import time
import connect

spi=spidev.SpiDev()


def SPI_init():
    spi.open(0,0)
    spi.max_speed_hz=122000
    spi.mode=0b00  #must match the slave!!!!
    spi.xfer([0xA0])
    
def SPI_read():
    #print('reading')
    
    #send head to trigger the slave stm32 only
    spi.xfer([0xA0])
    
    #recv data while sending the beats
    data=spi.xfer([0xA0, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F]) #sensor node 1
    #              head  h1    t1-i  -f    h2    t2-i  -f    l-k   l-g                            
    #              h-humidity  t-temp l-light         -i interger part -f friction part            
    print(data)

    #calc 
    h=data[1]             #humidity sensor 1
    t=data[2]+data[3]/100 #temp 1
    l=data[4]*100+data[5] #light
    
    
    #nbiot transmit
    connect.Send([data[1],data[2],data[3],data[4],data[5]])

    return h, t, l
    #if adding sensors


      
# test code
##SPI_init()
##while(1):
##       #a=spi.xfer([0xA0,0x02,0x02,0x02,0x02])
##       #print(a)
##       h1,t1,h2,t2,l1=SPI_read()
##       print('humi1',h1)
##       print('temp1',t1)
##       print('humi2',h2)
##       print('temp2',t2)
##       print('light1',11)
##    


##    print(spi.xfer([0xA0, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F]))
##    time.sleep(4) #3 first change 
    
       #print(spi.xfer([0xA0,0xA0]))
    
