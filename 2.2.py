import time
current_time = time.time()
days_since_epoch = int(current_time // (24 * 3600))
seconds_today = int(current_time % (24 * 3600))
hours = seconds_today // 3600
minutes = (seconds_today % 3600) // 60
seconds = seconds_today % 60

print("Số ngày từ epoch:", days_since_epoch)
print(f"Thời gian hiện tại: {hours:02d}:{minutes:02d}:{seconds:02d}")