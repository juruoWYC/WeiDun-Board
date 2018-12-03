import spidev
spi=spidev.SpiDev()





def SPI_init():
        spi.open(0,0)
        spi.max_speed_hz=122000
        spi.mode=0b00
        
	


def SPI_read(head):
        print('reading')
        #send head to trigger the slave 
        
        #recv data while sending the beats
        data_1=spi.xfer([0x02,0x02,0x02,0x02])
        data_2=spi.xfer([0x01,0x01,0x01,0x01])
        data_3=spi.xfer([0x01,0x01,0x01,0x01])
        print(data_1)
        print(data_2)
        print(data_3)
   
        #process orig data
        st=data_1[1]+data_1[3]/100
        at=data_2[1]+data_2[3]/100
        h=data_3[1]+data_3[3]/100

     
        #...if adding sensors

        return st,at,h
#SPI_init()
#while(1):
#        SPI_read([0xA0])                
                
         	




        

