import time
import datetime
from datetime import datetime, timedelta
start = datetime.now()
end = datetime(int(2019),int(4), int(28), int(11))
End_of_semester = end-start
print(str(End_of_semester),'Until school is out for summer!')
if start > end : print(str(End_of_semester), 'School is out for summer!!!!!')
