import datetime as datetime

time = datetime.datetime.now()
hour = time.strftime("%H")

def traffic_criteria():
    if (hour >= "07" and hour <= "09") or (hour >= "18" and hour <= "23"):
        trafficFactor = 1
    elif hour >= "10" and hour <= "17":
        trafficFactor = 0.5
    else:
        trafficFactor = 0.25
    return trafficFactor