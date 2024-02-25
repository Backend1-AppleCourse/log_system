

import datetime
from datetime import datetime
import re

def log_function_factory(log_level=None):
    def log(msg, date=False):
        if date:
            print(f'{datetime.datetime.now()} - {msg}')
        else:
            print(msg)
        
    if log_level:
        def log(msg, date=False):
            if date:
                print(f'{datetime.datetime.now()} - {msg} - {log_level}')
            else:
                print(f'{msg} - {log_level}')
    return log

# log = log_function_factory('warning')
# log('This is a message')

def log_processing_factory(logs):
    def filter_logs(logs, date=False, start=None, end=None, short=False):
        date_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}') 
        if date:
            logs = [s for s in logs if re.search(date_pattern, s)]
        if start and end:
            datetime_x = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
            datetime_y = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
            logs = [s for s in logs if any( 
                            datetime_x <= datetime.strptime(match.group(), "%Y-%m-%d %H:%M:%S") <= datetime_y
                            for match in date_pattern.finditer(s)
                        )
                    ]
        if short:
            logs = [log for log in logs if len(log) < 10]
        return logs
    return filter_logs

logs = ['This is a message', '2024-02-25 16:29:00.172535 - This is a message', '2024-02-25 16:29:39.340882 - This is a message - info', 'This is a message - error', 'short msg']
filter_logs = log_processing_factory(logs)


print(filter_logs(logs, date=True))
print(filter_logs(logs, start="2024-02-25 16:29:00", end="2024-02-25 16:29:38"))
print(filter_logs(logs, short=True))
