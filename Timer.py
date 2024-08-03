import time


def countdown_timer(duration):
    print(f"Starting countdown for {duration} seconds...")
    for t in range(duration, 0, -1):
        print(f"Countdown in {t}")
        time.sleep(1)  # Wait for 1 second
    print("...Finished!")
