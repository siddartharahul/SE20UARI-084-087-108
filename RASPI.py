import Adafruit_DHT

sensor = Adafruit_DHT.DHT22

pin = 4  

try:
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature:.2f}°C')
        print(f'Humidity: {humidity:.2f}%')
    else:
        print('Failed to retrieve data from the DHT22 sensor.')

except KeyboardInterrupt:
    print('Measurement stopped by user')

except Exception as e:
    print(f'Error: {e}')

finally:
    
    GPIO.cleanup()
