import string
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Step 1: Generate a frequency table of all the words in the first text file
filename1 = 'english_novel.txt' # replace with your file name
with open(filename1, 'r') as file:
    text1 = file.read()

# remove punctuation and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
text1 = text1.translate(translator).lower()

# split the text into words and count their frequencies
words1 = text1.split()
freq1 = {}
for word in words1:
    if word in freq1:
        freq1[word] += 1
    else:
        freq1[word] = 1

# Step 2: Rank the words in the frequency table according to their frequency, from most to least frequent
ranked_words1 = sorted(freq1, key=freq1.get, reverse=True)

# Step 3: Plot the word frequency against their rank on a logarithmic scale. Use matplotlib to display this plot on a log scale and make it look nice.
x1 = np.arange(1, len(ranked_words1)+1)
y1 = [freq1[word] for word in ranked_words1]

# repeat steps 1-3 for the second text file
filename2 = 'combined_genlangs.txt' # replace with your file name
with open(filename2, 'r') as file:
    text2 = file.read()

text2 = text2.translate(translator).lower()

words2 = text2.split()
freq2 = {}
for word in words2:
    if word in freq2:
        freq2[word] += 1
    else:
        freq2[word] = 1

ranked_words2 = sorted(freq2, key=freq2.get, reverse=True)

x2 = np.arange(1, len(ranked_words2)+1)
y2 = [freq2[word] for word in ranked_words2]

# plot both lines on the same graph
fig, ax = plt.subplots()
ax.plot(x1, y1, color='royalblue', label='English Novel (n=42,004)')
ax.plot(x2, y2, color='blueviolet', label='Combined Genlangs (n=3,497)')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Rank')
ax.set_ylabel('Frequency')
ax.set_title('Zipf\'s Law Plot, Text from "Tom Swift and His Electric \n Runabout\" and Combined Generated Languages')
ax.legend()

# plot ideal Zipf's law line
N1 = len(ranked_words1)
ideal_x1 = np.arange(1, N1+1)
ideal_y1 = N1 / ideal_x1
ax.plot(ideal_x1, ideal_y1, color='lightsteelblue', linestyle='--')

N2 = len(ranked_words2)
ideal_x2 = np.arange(1, N2+1)
ideal_y2 = N2 / ideal_x2
ax.plot(ideal_x2, ideal_y2, color='plum', linestyle='--')

# calculate the correlation coefficients and display them in the graph
log_x1 = np.log(x1)
log_y1 = np.log(y1)
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(log_x1, log_y1)
ax.text(0.491, 0.8, f'Correlation (English Novel): {r_value1:.3f}', transform=ax.transAxes)
# calculate the correlation coefficients and display them in the graph
log_x2 = np.log(x2)
log_y2 = np.log(y2)
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(log_x2, log_y2)
ax.text(0.4, 0.75, f'Correlation (Combined Genlangs): {r_value1:.3f}', transform=ax.transAxes)
plt.show()
