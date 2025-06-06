import pandas as pd

file1 = r'C:\Users\Anastasia\course\pythonAQA\lesson_13.1\task_1/random-michaels.csv'
file2 = r'C:\Users\Anastasia\course\pythonAQA\lesson_13.1\task_1/random.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
combined = pd.concat([df1, df2])
deduplicated = combined.drop_duplicates()
deduplicated.to_csv('result_kiian.csv', index=False)

print("Entities without duplicates are saved in result_without_duplicates.csv")