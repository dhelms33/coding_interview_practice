import math
class SensorThrottler():
    def __init__(self, timestamps:list[float], sensor_ids:list[str]):
        self.timestamps = timestamps
        self.sensor_ids = sensor_ids
        self.last_seen = {}
    
    def should_process(self, timestamps:list[float], sensor_ids:list[str]) -> bool:
        timestamps_modified = {
            
        }
        for timestamp, sensor_id in zip(timestamps, sensor_ids):
            if timestamp < 10:
                return False
            elif timestamp > 10:
                return True
            timestamps_modified.update(sensor_id)
            timestamps_modified.update(timestamp)
        return timestamps_modified
    
    def should_process_alt(self, sensor_id:str, timestamp:float) -> bool:
        """ Takes incoming timestamps and sensor ids and inputs them into a dict for easier lookup. Then returns a bool if the item should process the entry."""
        if sensor_id not in self.last_seen or timestamp - self.last_seen[sensor_id] >= 10:
            #if the sensor_id is brand new or if the timestamp - sensor_id is greater than 10
            return True
        #less than 10 seconds, throttle the log
        return False