import time
import datetime
from datetime import datetime, timedelta
start = datetime.now() #this will start from the current date and time
end = datetime(int(2019),int(4), int(28), int(11)) #this is the end of spring semester 2019
End_of_semester = end-start
print(str(End_of_semester),'Until school is out for summer!')
if start > end : print(str(End_of_semester), 'School is out for summer!!!!!') #this will print after the semester schedule is over
