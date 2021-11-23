import os


def cut_video(start, cut):
    # Exercise 1
    # first we limit the cut within the video length
    if start > 596:
        print("The BBB short cut is smaller than the time introduced \n")
    elif start + cut > 596:
        print("The BBB short cut is smaller than the time where to finish the cut \n")

    start_time = time_standard(start)
    cut_time = time_standard(cut)
    print("Start_time", start_time, "Cut time: ", cut_time)

    cmd = str("ffmpeg -ss " + start_time + " -i BBB.mp4 -ss " + cut_time + " -t " + cut_time + " -c copy cut_BBB.mp4")
    os.system(cmd)


def time_standard(time):
    # auxiliary function design to transform into correct format the time
    minutes = time // 60
    min_str = str("0" + str(minutes))

    sec = time % 60
    if sec < 10:
        sec_str = str("0" + str(sec))

    else:
        sec_str = str(sec)
    output_time = str("00:{0}:{1}".format(min_str, sec_str))
    return output_time


def get_yuv():
    # Exercise 2
    cmd = 'ffmpeg -i BBB.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" hist_BBB.mp4 '
    os.system(cmd)


def resize(option_):
    # Exercise 3
    if option_ == 1:
        size = str("1280:720")
    elif option_ == 2:
        size = str("640:480")
    elif option_ == 3:
        size = str("360:240")
    elif option_ == 4:
        size = str("160:120")

    cmd = str("ffmpeg -i BBB.mp4 -filter:v scale=" + str(size) + " -c:a copy size" + str(option_) + '_BBB.mp4')
    os.system(cmd)


def mono_audio_mp3_codec():
    # Exercise 4
    cmd = str("ffmpeg -i BBB.mp4 -ac 1 -acodec mp3 mono_mp3_codec_BBB.mp4")
    os.system(cmd)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    option = int(input("Choose your action:\n\n  "
                       "1. Cut video\n  "
                       "2. Extract YUV histogram\n  "
                       "3. Resize video\n  "
                       "4. Change "
                       "audio into mono, change codec\n "
                       "exit. To end the program\n\n Your action: "))
    while option != 'exit':

        if option == 1:
            start_ = int(input("Enter the sec where to start the cut: "))
            cut_ = int(input("Enter N sec to cut: "))

            cut_video(start_, cut_)

        elif option == 2:
            get_yuv()

        elif option == 3:
            validation = False
            while not validation:
                size_ = int(input("\n Chose between the different sizes: \n "
                                  "1. 720p\n "
                                  "2. 480p\n "
                                  "3. 360x240\n "
                                  "4. 160x120 "
                                  "\n\n Enter your option: "))
                if 1 <= size_ <= 4:
                    resize(size_)
                    validation = True
                else:
                    print("The option introduced is not valid. Try again.\n\n")

        elif option == 4:
            mono_audio_mp3_codec()

        else:
            print("\n The option introduced is not valid. Try again.\n\n")

        option = int(input("\n Choose your action:\n\n  "
                           "1. Cut video\n  "
                           "2. Extract YUV histogram\n  "
                           "3. Resize video\n  "
                           "4. Change "
                           "audio into mono, change codec"
                           "exit. To end the program\n\n Your action: "))


