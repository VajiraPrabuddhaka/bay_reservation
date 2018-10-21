while True:
           if (GPIO.input(RELE1) == True):
                print('3.3')
                GPIO.setup(RELE360, GPIO.OUT)

                alarm = 0
                while 1:
                    if (GPIO.input(RELE0) == True):
                        alarm += 1
                        if(alarm == 1 ):
                            print('alarm')
                    else:
                        alarm = 0

           else:
                print('0')
                GPIO.setup(RELE360, GPIO.IN)
                sleep(1);