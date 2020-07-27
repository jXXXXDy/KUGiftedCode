# 기울기센서를 이용해서 기울기 정도를 측정합니다.

import time
import Adafruit_ADXL345
import csv

# 모듈을 읽어옵니다.
accel = Adafruit_ADXL345.ADXL345()

print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
fTiltT = open('TiltTime.csv', 'w', encoding='utf-8', newline='')


# 아래의 코드를 시도합니다.
try:
    # while문 안에 있는 코드를 계속 시행합니다.
    while True:
        # 센서를 통해 x, y, z축의 기울기 정도를 읽어옵니다.
        x, y, z = accel.read()
        now = datetime.datetime.now()
        nowTime = now.strftime('%H:%M:%S')        
        
        # 읽어온 기울기의 정도를 형식에 맞추어 출력합니다.
        print('X={0}, Y={1}, Z={2}, t{3}'.format(x, y, z, nowTime))
        
        write.writerow([nowTime, x, y, z])

        # 1초의 텀을 줍니다.
        time.sleep(1.0)
       
# 키 인터럽트가 발생하면 종료합니다.
except KeybordInterrupt:
    print("done")

# GPIO 핀 설정을 모두 초기화 해줍니다.
GPIO.cleanup()
