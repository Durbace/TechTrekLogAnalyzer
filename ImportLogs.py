import os
import random
from datetime import datetime, timedelta

LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'Output.txt')

def random_log_time():
    random_seconds = random.randint(0, 86399)
    random_time = (datetime.combine(datetime.today(), datetime.min.time()) + timedelta(seconds=random_seconds))
    return random_time.strftime('%H:%M:%S')

def random_log_type():
    return random.choice(['INFO', 'DEBUG', 'ERROR'])

def random_app_log():
    return random.choice(['BackendApp', 'FrontendApp', 'API', 'SYSTEM'])

def random_ms():
    return random.randrange(10, 30)

def random_success_log_message_running(app):
    return '{} has started running... \n'.format(app)

def random_success_log_message_ms(app, ms):
    return '{} has ran successfully in {}ms'.format(app, ms)

def random_fail_log_message():
    return '{} has failed after {}ms. Retrying... '.format(random_app_log(), random_ms())

def random_debug_log_message():
    return '{} is still running, please wait... '.format(random_app_log())

def generate_logs():
    with open(LOG_FILE_PATH, 'w') as f:
        for _ in range(10000):
            log_type = random_log_type()
            if log_type == 'ERROR':
                to_write = f"{random_log_time()} - [{log_type}] - {random_fail_log_message()}\n"
                f.write(to_write)
            elif log_type == 'DEBUG':
                to_write = f"{random_log_time()} - [{log_type}] - {random_debug_log_message()}\n"
                f.write(to_write)
            else:
                log_time = random_log_time()
                app = random_app_log()
                to_write_running = f'{log_time} - [{log_type}] - {random_success_log_message_running(app)}'
                to_write_finish = f'{log_time} - [{log_type}] - {random_success_log_message_ms(app, random_ms())}\n'
                f.write(to_write_running)
                f.write(to_write_finish)

if __name__ == "__main__":
    generate_logs()
