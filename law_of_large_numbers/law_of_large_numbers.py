import matplotlib.pyplot as plt
import numpy as np


population_size =2.3e5
sample_size = 50
number_of_samples = 500

skip = int(1e3)

# generate data
population = np.logspace(np.log10(0.001), np.log10(5), int(population_size))
np.random.shuffle(population)
true_mean = population.mean()

samplemeans = np.zeros(number_of_samples)

# calculate and store sample means
for i in range(number_of_samples):
    sample = np.mean(np.random.choice(population, sample_size))
    samplemeans[i] = sample

# central limit theorem
plt.hist(samplemeans)
plt.xlabel('Sample mean')
plt.ylabel('Number of samples')
plt.legend()
plt.show()

plt.plot(samplemeans, 'ko', label = 'Sample means')
plt.plot([0, number_of_samples], [true_mean, true_mean], 'r', linewidth=4, label = 'True mean')
plt.legend()
plt.show()

# calculate and store average cumulative sample means
cumave = np.zeros(number_of_samples)
for i in range (0, number_of_samples):
    cumave[i] = np.mean(samplemeans[:i+1])

# plot the relationship between the number of samples and the true mean
plt.plot(cumave, 'o', label='Cumulative mean')
plt.plot([1, number_of_samples], [true_mean, true_mean], label='Population mean', linewidth=4)
plt.xlabel('Number of Samples')
plt.ylabel('Cumulative mean')
plt.legend()
plt.show()
print(cumave[-1])
print(true_mean)



number_of_meta_samples = 100
cumaves = np.zeros((number_of_meta_samples, number_of_samples))
for n in range(number_of_meta_samples):
    for i in range(number_of_samples):
        sample = np.mean(np.random.choice(population, sample_size))
        samplemeans[i] = sample
    temp = np.cumsum(samplemeans)/np.arange(1, number_of_samples+1)
    cumaves[n, :] = (temp - true_mean)**2

plt.plot(cumaves.T)
plt.ylim([-0.001, 0.01])
plt.show()