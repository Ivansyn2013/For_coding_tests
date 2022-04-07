from datetime import datetime, time, timedelta

def sun_angle(times: str) :
    t1 = time(hour=6, minute=0)
    t2 = time(hour=18,minute=0)
    t3 = datetime.strptime(times,'%H:%M')
    i = 'I don\'t ee the sun!'
    print(t3.hour*60+t3.minute)
    result = 180/(12*60)*((t3.hour-6)*60+t3.minute)

    return result if t1<t3.time()<t2 else i



print(sun_angle('01:23'))


# решения других
def sun_angle(time):
    h, m = list(map(int, time.split(':')))
    angle = 15 * h + m / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"

sun_angle=lambda t:["I don't see the sun!",int(t[:2])*15+int(t[~1:])/4-90][6<=int(t[:2])+int(t[~1:])/60<=18]


def sun_angle(time):
    hh, mm = map(int, time.split(':'))
    tt = hh * 60 + mm

    return "I don't see the sun!" if (tt < 360 or 1080 < tt) else (tt - 360) * 0.25