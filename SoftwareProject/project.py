import pygame
import os
import random
import sys

pygame.mixer.init()

def play_song(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def pause_song():
    pygame.mixer.music.pause()


def resume_song():
    pygame.mixer.music.unpause()


def stop_song():
    pygame.mixer.music.stop()


def next_track(file_list, current_track, played_tracks):
    stop_song()
    if len(played_tracks) == len(file_list):
        print("All songs have been played.")
        return

    next_index = random.randint(0, len(file_list) - 1)
    while next_index in played_tracks:
        next_index = random.randint(0, len(file_list) - 1)

    played_tracks.append(next_index)
    music_folder = "/home/shivendraraje004/Music"
    file_path = os.path.join(music_folder, file_list[next_index])
    play_song(file_path)


def shuffle_play(file_list):
    played_tracks = []
    while True:
        next_track(file_list, -1, played_tracks)
        if len(played_tracks) == len(file_list):
            played_tracks.clear()

        choice = input("Enter 1 to play the next song, or 0 to quit: ")
        if choice == "0":
            stop_song()
            break


def userInterface():
    print("1. Play")
    print("2. Pause")
    print("3. Resume")
    print("4. Stop")
    print("5. Next")
    print("6. Shuffle Play")
    print("7. Quit")


def main():
    music_folder = "/home/shivendraraje004/Music"
    files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

    current_track_index = 0
    played_tracks=[]
    # addition1
    #pygame.mixer.init()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
	
    while True:
        userInterface()
        Input = input("Enter your choice: ")

        if Input == "1":
            file_path = os.path.join(music_folder, files[current_track_index])
            play_song(file_path)
            played_tracks.append(current_track_index)

        elif Input == "2":
            pause_song()

        elif Input == "3":
            resume_song()

        elif Input == "4":
            stop_song()

        elif Input == "5":
            next_track(files, current_track_index,played_tracks)
            current_track_index = (current_track_index + 1) % len(files)

        elif Input == "6":
            shuffle_play(files)

        elif Input == "7":
            stop_song()
            break

        else:
            print("Invalid choice.")
            
            #for event in pygame.event.get():
            	#if event.type == pygame.USEREVENT:
                	#current_track_index = next_track(files, current_track_index)



if __name__ == "__main__":
 main()

