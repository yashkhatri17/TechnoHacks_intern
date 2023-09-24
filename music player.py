import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []  # List to store the paths to MP3 files
        self.current_song = None

    def add_to_playlist(self, song_path):
        self.playlist.append(song_path)

    def play(self, song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        self.current_song = song_path

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        current_index = self.playlist.index(self.current_song)
        next_index = (current_index + 1) % len(self.playlist)
        self.play(self.playlist[next_index])

    def previous_song(self):
        current_index = self.playlist.index(self.current_song)
        prev_index = (current_index - 1) % len(self.playlist)
        self.play(self.playlist[prev_index])

if __name__ == "__main__":
    player = MusicPlayer()

    while True:
        print("Music Player Menu:")
        print("1. Add to Playlist")
        print("2. Play")
        print("3. Pause")
        print("4. Resume")
        print("5. Stop")
        print("6. Next Song")
        print("7. Previous Song")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            song_path = input("Enter the path to an MP3 file: ")
            if os.path.exists(song_path):
                player.add_to_playlist(song_path)
                print(f"Added '{song_path}' to the playlist.")
            else:
                print("Invalid file path.")
        elif choice == '2':
            if player.playlist:
                player.play(player.playlist[0])
            else:
                print("Playlist is empty. Add songs first.")
        elif choice == '3':
            player.pause()
        elif choice == '4':
            player.resume()
        elif choice == '5':
            player.stop()
        elif choice == '6':
            player.next_song()
        elif choice == '7':
            player.previous_song()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
