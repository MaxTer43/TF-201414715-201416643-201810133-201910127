import main
import datetime

main.time = datetime.datetime.now()
main.hour = main.time.strftime("%H")
print("hora: " + main.hour)

def traffic_criteria():
    if (main.hour >= "07" and main.hour <= "09") or (main.hour >= "18" and main.hour <= "23"):
        trafficFactor = 1
    elif main.hour >= "10" and main.hour <= "17":
        trafficFactor = 0.5
    else:
        trafficFactor = 0.25
    return trafficFactor

print("Factor de tráfico: " + str(traffic_criteria()))