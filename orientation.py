from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
  pitch, roll, yaw = sense.get_orientation().values()
  print("pitch = %s, roll = %s, yaw = %s" % (pitch, roll, yaw))
