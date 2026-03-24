
ten_min = 600 
difference = 0

time_in_sec = int(input("Type time in seconds: " ))

if(time_in_sec < ten_min):
    difference = ten_min - time_in_sec

    print(f"More seconds are needed: {difference}")

elif(time_in_sec > ten_min):
    print("The number of seconds given is more then required")

else:
    print("The number of seconds given equal the minutes")
