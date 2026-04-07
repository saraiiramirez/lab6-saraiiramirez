def trigger_alarm(temperatures, threshold=80):
    sensors_above_limit = []

    for sensor, temp in temperatures.items():
        if temp > threshold:
            sensors_above_limit.append(sensor)

    return sensors_above_limit