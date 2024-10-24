import pandas as pd

data = {
    'ism': ['Asadbek', 'Esonali', 'Madinaxon', 'Maxsudjon', 'Zuxriddin', 
            'Shoxjahon', 'Kozimjon', 'Furqatbek', 'Saidakbar', 'Azamjon', 'Diyorbek'],
    'Yoshi': [19, 19, 25, 19, 21, 22, 21, 23, 23, 19, 19],
    'Shaxar': ['Fargona', 'Fargona', 'Namangan', 'Fargona', 'Toshkent', 
               'Fargona', 'Fargona', 'Namangan', 'Andijon', 'Fargona', 'Fargona']
}

df = pd.DataFrame(data)
print(df)

# Filter for ages less than 20
yoshlar = df[df['Yoshi'] < 20]
print("20 dan kichik:\n", yoshlar)

# Increment ages by 1 using the correct column name
df['Yoshi'] += 1
print("Yangilangan yosh:\n", df)

# Save the DataFrame to an Excel file
df.to_excel('541.xlsx', index=False, sheet_name="541")
