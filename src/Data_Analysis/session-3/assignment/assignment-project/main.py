from config.config import cols_to_drop
from preprocessing import(Read_data_file, Drop_unnecessary_features, Check_data_type)

file_path = input("Enter file path: ")

df = Read_data_file(file_path)

if df is not None:

    print("Data before preprocessing:\n")
    print(Check_data_type(df))

    df = Drop_unnecessary_features(df, cols_to_drop)

    print('\n'+"=" * 50)
    print("\nData after removing unnecessary features:\n")
    print(Check_data_type(df))