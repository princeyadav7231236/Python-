import time
from pygame import mixer

total_amount_of_water = 3500


def repeat(audio_name):
    mixer.init()
    mixer.music.load(audio_name)
    mixer.music.set_volume(0.7)
    mixer.music.play(loops=-1, start=0.0, fade_ms=0)


repeat("water.mp3")

# while True:
#     print("Press 'p' to pause, 'r' to Resume ")
#     print("'e' to exit the program ")
#     query = input()
#     if query == "p":
#         mixer.music.pause()
#     elif query == "r":
#         mixer.music.unpause()
#     elif query == "e":
#         mixer.music.stop()
#         break

#     mixer.init()
#     mixer.music.load("activity.mp3")
#
#     mixer.music.set_volume(0.7)
#     mixer.music.play()

# while True:
#     print(repeat("water.mp3"))
#     print("Press 'p' to pause, 'r' to Resume ")
#     print("'e' to exit the program ")
#
#     query = input()
#     if query == "p":
#         mixer.music.pause()
#     elif query == "r":
#         mixer.music.unpause()
#     elif query == "e":
#         mixer.music.stop()
#         break
# time.sleep(9)
#
#     mixer.init()
#     mixer.music.load("time_to_exercise.mp3")
#
#     mixer.music.set_volume(0.7)
#     mixer.music.play()
#
#     while True:
#         print("Press 'p' to pause, 'r' to Resume ")
#         print("'e' to exit the program ")
#
#         query = input()
#         if query == "p":
#             mixer.music.pause()
#         elif query == "r":
#             mixer.music.unpause()
#         elif query == "e":
#             mixer.music.stop()
#             break
#     time.sleep(10)
#
#
# repeat()
#
#
# def again():
#     repeat()
#     return again()
#
#
# again()
