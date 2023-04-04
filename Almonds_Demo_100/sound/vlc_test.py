import vlc, time


thing = vlc.MediaPlayer("game_over.ogg").play()
time.sleep(1)
print("hello")
time.sleep(1)
print(f"exit: {thing}")
