adjective=$(shuf -n 1 adjectives.txt)
animal=$(shuf -n 1 animals.txt)
activity=$(shuf -n 1 activities.txt)
club=$(shuf -n 1 clubs.txt)

python tweet.py $adjective $animal $activity $club