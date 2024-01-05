# Create a new column 'Salary' in the DataFrame 'df' with random integer values
# between 50000 and 80000 (inclusive).

df['Salary']=np.random.randint(5000,80001,len(df))