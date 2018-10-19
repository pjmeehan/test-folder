# Is it Tuesday. Taken from Ian's example for the use to testing.

import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()
 
if dayofweek == 1:
    print("It's Tuesday")
else:
    print("unfortunately, it's not tuesday")   
