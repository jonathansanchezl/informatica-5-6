def main():

    face = input(" ")
    face = face.replace(":)","🙂", count=-1)
    face = face.replace(":(","🙁", count=-1)
    print(face)
if __name__ == "__main__":
     main()
