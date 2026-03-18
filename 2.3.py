import math
from datetime import datetime, timedelta
# 1: Thể tích hình cầu bán kính 5
r = 5
volume = (4/3) * math.pi * r**3
print("Bài 1 - Thể tích hình cầu:", round(volume, 2))
# 2: Tổng chi phí bán buôn cho 60 bản
cover_price = 24.95
discount_rate = 0.40
wholesale_price = cover_price * (1 - discount_rate)
copies = 60
total_books_cost = wholesale_price * copies
shipping_first = 3.00
shipping_additional = 0.75
shipping_cost = shipping_first + shipping_additional * (copies - 1)

total_cost = total_books_cost + shipping_cost
print("Bài 2 - Tổng chi phí bán buôn:", round(total_cost, 2))

# 3: Thời gian chạy
start_time = datetime.strptime("6:52", "%H:%M")
easy_pace = 8 + 15/60  
tempo_pace = 7 + 12/60  
total_minutes = easy_pace*2 + tempo_pace*3
run_duration = timedelta(minutes=total_minutes)
end_time = start_time + run_duration
print("Bài 3 - Thời gian về nhà:", end_time.strftime("%H:%M"))