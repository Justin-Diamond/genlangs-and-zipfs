import string
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Step 1: Generate a frequency table of all the words in multiple text files
filenames = ['/Users/justindiamond/Desktop/Python/ZipfGPT/lumivoxa.txt', '/Users/justindiamond/Desktop/Python/ZipfGPT/voxphera.txt', '/Users/justindiamond/Desktop/Python/ZipfGPT/vivenzia.txt'] # replace with your file names
freq = {}
for filename in filenames:
    with open(filename, 'r') as file:
        text = file.read()
        # remove punctuation and convert to lowercase
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator).lower()

        # split the text into words and count their frequencies
        words = text.split()
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

# Step 2: Rank the words in the frequency table according to their frequency, from most to least frequent
ranked_words = sorted(freq, key=freq.get, reverse=True)

# Step 3: Plot the word frequency against their rank on a logarithmic scale. Use matplotlib to display this plot on a log scale and make it look nice.
x = np.arange(1, len(ranked_words)+1)
y = [freq[word] for word in ranked_words]
fig, ax = plt.subplots()
ax.plot(x, y, color='blue')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Rank')
ax.set_ylabel('Frequency')
ax.set_title('Zipf\'s law plot')

# plot ideal Zipf's law line
N = len(ranked_words)
ideal_x = np.arange(1, N+1)
ideal_y = N / ideal_x
ax.plot(ideal_x, ideal_y, color='red', linestyle='--')

# Step 4: Calculate the correlation coefficient between the logarithm of the word frequency and the logarithm of their rank. A high correlation coefficient indicates that the text follows Zipf's law. Display this correlation in the graph please.
log_x = np.log(x)
log_y = np.log(y)
slope, intercept, r_value, p_value, std_err = linregress(log_x, log_y)
ax.text(0.1, 0.9, f'Correlation: {r_value:.3f}', transform=ax.transAxes)
plt.show()
