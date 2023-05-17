import pygame
import os
import random
import sys
pygame.mixer.init()
def play_music(file_path):
    #pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def resume_music():
    pygame.mixer.music.unpause()


def stop_music():
    pygame.mixer.music.stop()


def next_track(file_list, current_track, played_tracks):
    stop_music()
    if len(played_tracks) == len(file_list):
        print("All songs from the playlist have been played.")
        return

    next_index = random.randint(0, len(file_list) - 1)
    while next_index in played_tracks:
        next_index = random.randint(0, len(file_list) - 1)

    played_tracks.append(next_index)
    music_folder = "/home/shivendraraje004/Music"
    file_path = os.path.join(music_folder, file_list[next_index])
    play_music(file_path)


def shuffle_play(file_list):
    played_tracks = []
    while True:
        next_track(file_list, -1, played_tracks)
        if len(played_tracks) == len(file_list):
            played_tracks.clear()

        choice = input("Enter 'Next' to play the next song, or 'Quit' to quit: ")
        if choice == "Quit":
            stop_music()
            break


def display_menu():
    print("1. Play")
    print("2. Pause")
    print("3. Resume")
    print("4. Stop")
    print("5. Next")
    print("6. Shuffle Play")
    print("7. Quit")


def main():
    music_folder = "/home/shivendraraje004/Music"  # Set the path to your music folder
    files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

    current_track_index = 0
    played_tracks=[]
    # addition1
    #pygame.mixer.init()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
	
    while True:
        display_menu()
        Input = input("Enter your choice: ")

        if Input == "1":
            file_path = os.path.join(music_folder, files[current_track_index])
            play_music(file_path)
            played_tracks.append(current_track_index)

        elif Input == "2":
            pause_music()

        elif Input == "3":
            resume_music()

        elif Input == "4":
            stop_music()

        elif Input == "5":
            next_track(files, current_track_index,played_tracks)
            current_track_index = (current_track_index + 1) % len(files)

        elif Input == "6":
            shuffle_play(files)

        elif Input == "7":
            stop_music()
            break

        else:
            print("Invalid choice. Please try again.")
            
            for event in pygame.event.get():
            	if event.type == pygame.USEREVENT:
                	current_track_index = next_track(files, current_track_index)



if __name__ == "__main__":
 main()

