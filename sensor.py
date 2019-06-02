from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print(pressure)

temp = sense.get_temperature()
print(temp)

humidity = sense.get_humidity()
print(humidity)
