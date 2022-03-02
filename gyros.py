
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
 
bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect
 
# Aktivieren, um das Modul ansprechen zu koennen
bus.write_byte_data(address, power_mgmt_1, 0)
 
print("Gyroskop")
print("--------")
while True: 
  gyroskop_xout = read_word_2c(0x43)
  gyroskop_yout = read_word_2c(0x45)
  gyroskop_zout = read_word_2c(0x47)
  
  print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 131))
  print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 131))
  print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 131))
   
  print
  print("Beschleunigungssensor")
  print("---------------------")
   
  beschleunigung_xout = read_word_2c(0x3b)
  beschleunigung_yout = read_word_2c(0x3d)
  beschleunigung_zout = read_word_2c(0x3f)
   
  beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
  beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
  beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0
   
  print("beschleunigung_xout: ", ("%6d" % beschleunigung_xout), " skaliert: ", beschleunigung_xout_skaliert)
  print("beschleunigung_yout: ", ("%6d" % beschleunigung_yout), " skaliert: ", beschleunigung_yout_skaliert)
  print("beschleunigung_zout: ", ("%6d" % beschleunigung_zout), " skaliert: ", beschleunigung_zout_skaliert)
   
  print("X Rotation: " , get_x_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
  print("Y Rotation: " , get_y_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
