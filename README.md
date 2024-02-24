# Download youtube audio as .mp3 based on a text file

In order to use the application:

python3 ytmp3.py music.txt

The application fetches five results from youtube for each row found in music.txt and tries to download its audio if its available.
In the first success download ignores the remaining results.

In addition FeedSdCard.py is created in order to rename .mp3 files recursively or in a specific folder. Since some cars use filename to sort the songs, this script renames based on the number of all songs in that folder and continues to fill the first part with numbers then the name of the song as follows:

001_Rihanna_TeAmo
...

If there are more than 99 songs in that folder

Usage:
python3 FeedSdCard.py path_to_root_folder -r(for recursive modification)
