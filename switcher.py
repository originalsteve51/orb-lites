import subprocess, time
import datetime


# Hour and minute when it is dark. After this time, we only show xmastree
# and branch_paint. 
evening_hour = 16
evening_minute = 30

sleep_time = 60



dir_name = '/home/pi/mycode/pi-lights/'

try:
    while True:
        now = datetime.datetime.now()
    
        if (now.hour == evening_hour and now.minute >= evening_minute) or now.hour > evening_hour:
            process_names = ('xmastree.py', 'branch_paint.py', 'fill_up.py', 'spinny.py')
            sleep_time = 90
        else:
            process_names = ('spinny.py', 'xmastree.py', 'branch_paint.py', 'fill_up.py')
            sleep_time = 60
    
        for name in process_names:
            p = subprocess.Popen(['python3',
                            dir_name+name],
                            stdin=subprocess.PIPE,
                            stdout=None,
                            stderr=None)
            time.sleep(sleep_time)
            p.kill()
            p.communicate()
finally:
    # After a keyboard interrupt or anything else that shuts things down,
    # turn off the LED strand
    print("BYE!")
    p.kill()
    p.communicate()
