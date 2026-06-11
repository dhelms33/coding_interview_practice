import math
class SensorThrottler():
    def __init__(self, timestamps:list[float], sensor_ids:list[str]):
        self.timestamps = timestamps
        self.sensor_ids = sensor_ids
    
    def should_process(self, timestamps:list[float], sensor_ids:list[float]) -> bool:
        timestamps_modified = {
            
        }
        for timestamp, sensor_id in zip(timestamps, sensor_ids):
            pass
        return timestamps_modified