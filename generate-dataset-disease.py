""" Module to generate dataset for the health prediction model """

import pandas as pd
import random

df = pd.DataFrame(columns=['pulse', 'systolic_pressure', 'diastolic_pressure', 'oxygen_level', 'glucose', 'temperature', 'weight', 'height', 'age'])

normal_values = {
    'pulse': (60, 90),
    'systolic_pressure': (120, 130),
    'diastolic_pressure': (80, 85),
    'oxygen_level': (95, 100),
    'glucose': (3.3, 5.5),
    'temperature': (35.5, 37.6),
}

for i in range(5000):
    is_anomaly = random.randint(1, 100) <= 6

    if is_anomaly:
        pulse = random.randint(normal_values['pulse'][0], normal_values['pulse'][1])
        systolic_pressure = random.randint(normal_values['systolic_pressure'][0], normal_values['systolic_pressure'][1])
        diastolic_pressure = random.randint(normal_values['diastolic_pressure'][0], normal_values['diastolic_pressure'][1])
        oxygen_level = random.randint(normal_values['oxygen_level'][0], normal_values['oxygen_level'][1])
        glucose = random.uniform(normal_values['glucose'][0], normal_values['glucose'][1])
        temperature = random.uniform(normal_values['temperature'][0], normal_values['temperature'][1])

        pulse += (pulse * (100 + random.choice([-1, 1]) *  random.randint(1, 5))) / 100
        systolic_pressure += (systolic_pressure * (100 + random.choice([-1, 1]) *  random.randint(1, 5))) / 100
        diastolic_pressure += (diastolic_pressure * (100 + random.choice([-1, 1]) *  random.randint(1, 5))) / 100
        oxygen_level += (oxygen_level * (100 + random.choice([-1, 1]) *  random.randint(1, 5))) / 100
        glucose += (glucose * (100 + random.choice([-1, 1]) *  random.randint(1, 5))) / 100
        temperature += (temperature * (100 + random.choice([-1, 1]) *  random.randint(1, 5))) / 100

        weight = random.uniform(50, 100)
        height = random.uniform(150, 200)
        age = random.randint(18, 80)

        df = df._append({
            'pulse': round(pulse, 2),
            'systolic_pressure': round(systolic_pressure, 2),
            'diastolic_pressure': round(diastolic_pressure, 2),
            'oxygen_level': round(oxygen_level, 2),
            'glucose': round(glucose, 2),
            'temperature': round(temperature, 2),
            'weight': weight,
            'height': height,
            'age': age,
            'is_anomaly': 1
        }, ignore_index=True)
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
            'pulse': round(pulse, 2),
            'systolic_pressure': round(systolic_pressure, 2),
            'diastolic_pressure': round(diastolic_pressure, 2),
            'oxygen_level': round(oxygen_level, 2),
            'glucose': round(glucose, 2),
            'temperature': round(temperature, 2),
            'weight': weight,
            'height': height,
            'age': age,
            'is_anomaly': is_a
        }, ignore_index=True)

df.to_csv('dataset.csv', index=False)