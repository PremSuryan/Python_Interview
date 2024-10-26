# Given list and target sum
# numbers = [1, 2, 3, 9]
numbers = [1, 2 ,4 ,4]
target_sum = 8

# Initialize an empty list to store pairs
pairs = []

# Loop through each number in the list
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            pairs.append((numbers[i], numbers[j]))

# Print the pairs
print("Pairs that sum to", target_sum, ":", pairs)
