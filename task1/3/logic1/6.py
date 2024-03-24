def alarm_clock(day, is_vacation):
    if is_vacation:
        if day == 0 or day == 6:
            return "off"
        else:
            return "10:00"  
    else:
        if day == 0 or day == 6:  
            return "10:00"
        else:
            return "7:00"
