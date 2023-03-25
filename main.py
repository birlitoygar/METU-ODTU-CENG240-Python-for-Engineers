#Average speed of the 1st interval
avgSpeed_1stInterval = float(
  input("What's your speed for the first interval? "))

#Duration of 1st interval
duration_1stInterval = float(
  input("What's your duration for the first interval? "))

#Average speed for 2nd interval
avgSpeed_2ndInterval = float(
  input("What's your speed for the second interval? "))

#Duration of 2nd interval
duration_2ndInterval = float(
  input("What's your duration for the second interval? "))

#Average speed for 3rd interval
avgSpeed_3rdInterval = float(
  input("What's your speed for the third interval? "))

#Duration of 3rd interval
duration_3rdInterval = float(
  input("What's your duration for the third interval? "))

#Average speed for 4th interval
avgSpeed_4thInterval = float(
  input("What's your speed for the fourth interval? "))

#Duration of 4th interval
duration_4thInterval = float(
  input("What's your duration for the fourth interval? "))

#Length of one lap
lap_length = float(input("How long is one lap? "))

#let's calculate the laps
laps = float(((avgSpeed_1stInterval * duration_1stInterval) +
              (avgSpeed_2ndInterval * duration_2ndInterval) +
              (avgSpeed_3rdInterval * duration_3rdInterval) +
              (avgSpeed_4thInterval * duration_4thInterval)) / lap_length)

print("{:.1f}".format(laps))