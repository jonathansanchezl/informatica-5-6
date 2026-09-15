import time
def main():
    playlist = ["Boston", "Dracula", "I knew it I knwe you", "hate that I made you love me", "Risk it all"]
    playlist.append("Be by you")
    print(playlist)
    playlist.insert(0, "Bohemian Rhapsody")
    playlist.pop(4)
    print(playlist)
    print(playlist.index("Risk it all"))
    print("Number of songs in playlist:", len(playlist))
    playlist.reverse()
    print(playlist)
    playlist.sort()
    print(playlist)


    repeat = len(playlist)
    while repeat > 0:
        print(playlist)
        song = playlist[0]
        playlist.pop(0)
        playlist.append(song)
        repeat -= 1
        time.sleep(3)

if __name__ == "__main__":
    main()
