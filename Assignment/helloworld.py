import time
import random

list_text = ["Hello World","log_details","concurrent"]
end_time = time.time() + 180
while time.time() < end_time:
        word = random.choice(list_text)
        print(word)
        time.sleep(1)  
