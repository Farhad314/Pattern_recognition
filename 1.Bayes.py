import pandas as pd
import matplotlib.pyplot as plt
# Read the excel file
data = pd.read_excel('1.bayes.xlsx')
print(data)

# Iterate over each row in the dataframe
for index, row in data.iterrows():
    pA = row['P(A)']
    pB = row['P(B)']
    pBgA = row['P(B/A)']

    pAgB = (pBgA * pA) / pB

    # Print the result
    print(f"P(A|B) for row {index + 1}: {pAgB:.2f}")
x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Create a scatter plot
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Excel Data')
plt.show()