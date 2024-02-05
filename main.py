'''bugungi sana va vaqtni chiqarsh'''
from datetime import datetime
bugun = datetime.now()
print(bugun.strftime('%Y-%m-%d %H:%M:%S'))