from textblob import TextBlob

analysis = TextBlob("TextBlob is my favorite!")

pos_count = 0
pos_correct = 0

with open("positive.txt", "r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity >= 0.0001:
            if analysis.sentiment.polarity >= 0:
                pos_correct += 1
            pos_count += 1

neg_count = 0
neg_correct = 0

with open("negative.txt", "r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity <= -0.0001:
            if analysis.sentiment.polarity <= 0:
                neg_correct += 1
            neg_count += 1

print("positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
