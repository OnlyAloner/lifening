""" Module to generate dataset for the health prediction model """

import pandas as pd
import random

df = pd.DataFrame(columns=['date', 'pulse', 'systolic_pressure', 'diastolic_pressure', 'oxygen_level', 'glucose', 'temperature'])

normal_values = {
    'pulse': (60, 90),
    'systolic_pressure': (120, 130),
    'diastolic_pressure': (80, 85),
    'oxygen_level': (95, 100),
    'glucose': (3.3, 5.5),
    'temperature': (35.5, 37.6),
}

date = pd.to_datetime('1/1/2020')
for cnt in range(20000):
    is_anomaly = random.randint(1, 100) <= 1

    if is_anomaly:
        origin_pulse = random.randint(normal_values['pulse'][0], normal_values['pulse'][1])
        origin_systolic_pressure = random.randint(normal_values['systolic_pressure'][0], normal_values['systolic_pressure'][1])
        origin_diastolic_pressure = random.randint(normal_values['diastolic_pressure'][0], normal_values['diastolic_pressure'][1])
        origin_oxygen_level = random.randint(normal_values['oxygen_level'][0], normal_values['oxygen_level'][1])
        origin_glucose = random.uniform(normal_values['glucose'][0], normal_values['glucose'][1])
        origin_temperature = random.uniform(normal_values['temperature'][0], normal_values['temperature'][1])

        loop_range = random.randint(3, 10)
        side = random.choice([-1, 1])
        for i in range(loop_range):
            is_anomaly = int((i + 1) > loop_range / 2)
            pulse = (origin_pulse * (100 + side *  i)) / 100
            systolic_pressure = (origin_systolic_pressure * (100 + side *  i)) / 100
            diastolic_pressure = (origin_diastolic_pressure * (100 + side *  i)) / 100
            oxygen_level = (origin_oxygen_level * (100 + side *  i)) / 100
            glucose = (origin_glucose * (100 + side *  i)) / 100
            temperature = (origin_temperature * (100 + side *  i)) / 100
            
            df = df._append({
                'date': date,
                'pulse': round(pulse, 2),
                'systolic_pressure': round(systolic_pressure, 2),
                'diastolic_pressure': round(diastolic_pressure, 2),
                'oxygen_level': round(oxygen_level, 2),
                'glucose': round(glucose, 2),
                'temperature': round(temperature, 2),
                'is_anomaly': i
            }, ignore_index=True)
            date += pd.Timedelta(days=1)
        for i in range(loop_range):
            is_anomaly = int((i + 1) <= loop_range / 2)
            pulse = (origin_pulse * (100 + side *  (loop_range - i - 1))) / 100
            systolic_pressure = (origin_systolic_pressure * (100 + side *  (loop_range - i - 1))) / 100
            diastolic_pressure = (origin_diastolic_pressure * (100 + side *  (loop_range - i - 1))) / 100
            oxygen_level = (origin_oxygen_level * (100 + side *  (loop_range - i - 1))) / 100
            glucose = (origin_glucose * (100 + side *  (loop_range - i - 1))) / 100
            temperature = (origin_temperature * (100 + side *  (loop_range - i - 1))) / 100

            df = df._append({
                'date': date,
                'pulse': round(pulse, 2),
                'systolic_pressure': round(systolic_pressure, 2),
                'diastolic_pressure': round(diastolic_pressure, 2),
                'oxygen_level': round(oxygen_level, 2),
                'glucose': round(glucose, 2),
                'temperature': round(temperature, 2),
                'is_anomaly': loop_range - i - 1
            }, ignore_index=True)
            date += pd.Timedelta(days=1)

    else:
        is_unnormally_anomal = random.randint(1, 100) <= 2
        is_a = 0
        if is_unnormally_anomal:
            is_a = 1

        pulse = random.randint(normal_values['pulse'][0], normal_values['pulse'][1])
        systolic_pressure = random.randint(normal_values['systolic_pressure'][0], normal_values['systolic_pressure'][1])
        diastolic_pressure = random.randint(normal_values['diastolic_pressure'][0], normal_values['diastolic_pressure'][1])
        oxygen_level = random.randint(normal_values['oxygen_level'][0], normal_values['oxygen_level'][1])
        glucose = random.uniform(normal_values['glucose'][0], normal_values['glucose'][1])
        temperature = random.uniform(normal_values['temperature'][0], normal_values['temperature'][1])
        weight = random.uniform(50, 100)
        height = random.uniform(150, 200)
        age = random.randint(18, 80)

        df = df._append({
            'date': date,
            'pulse': round(pulse, 2),
            'systolic_pressure': round(systolic_pressure, 2),
            'diastolic_pressure': round(diastolic_pressure, 2),
            'oxygen_level': round(oxygen_level, 2),
            'glucose': round(glucose, 2),
            'temperature': round(temperature, 2),
            'is_anomaly': is_a
        }, ignore_index=True)
        date += pd.Timedelta(days=1)

df.to_csv('time_series.csv', index=False)