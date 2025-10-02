import math 
def trig_values():

  degrees = 45
  
  angle_radians = math.radians(degrees)

  
  sine_result = math.sin(angle_radians)
  cosine_result = math.cos(angle_radians)
  tangent_result = math.tan(angle_radians)

  print(sine_result)
  print(cosine_result)
  print(tangent_result)
print(f"For 45 degrees:")
trig_values()