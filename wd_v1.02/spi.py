import spidev
import connect

spi=spidev.SpiDev()


def SPI_init():
    spi.open(0,0)
    spi.max_speed_hz=122000
    spi.mode=0b00

def SPI_read():
    #print('reading')
    #send head to trigger the slave 
    
    #recv data while sending the beats
    data_1=spi.xfer([0x02,0x02,0x02,0x02])
    data_2=spi.xfer([0x01,0x01,0x01,0x01])
    data_3=spi.xfer([0x01,0x01,0x01,0x01])
    
    data_4=spi.xfer([0x02,0x02,0x02,0x02])
    data_5=spi.xfer([0x01,0x01,0x01,0x01])
    data_6=spi.xfer([0x01,0x01,0x01,0x01])
    
    connect.Send([0x01,data_1[0],data_1[1],data_1[2],data_1[3],data_2[0],data_2[1],data_2[2],data_2[3],data_3[0],data_3[1],data_3[2],data_3[3]])
    
    connect.Send([0x02,data_4[0],data_4[1],data_4[2],data_4[3],data_5[0],data_5[1],data_5[2],data_5[3],data_6[0],data_6[1],data_6[2],data_6[3]])
    #print(data_1)
    #print(data_2)
    #print(data_3)
   
    #process orig data
    st1=data_1[1]+data_1[3]/100
    at1=data_2[1]+data_2[3]/100
    h1=data_3[1]+data_3[3]/100
    
    st2=data_4[1]+data_4[3]/100
    at2=data_5[1]+data_5[3]/100
    h2=data_6[1]+data_6[3]/100
    
    #if adding sensors
    return st1,at1,h1,st2,at2,h2
    
#SPI_init()
#while(1):
#        SPI_read([0xA0])
