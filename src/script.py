import pandas as pd

def read_excel_file(file_path):
    return pd.read_excel(file_path)

def get_columns(dataframe):
    return dataframe.columns.to_list()

def sort_data(dataframe, columns):
    return dataframe.sort_values(by=columns)

def write_excel_file(file_path, sorted_data):
    sorted_data.to_excel(file_path, index=False)
    print(f"\nWritten to {file_path}..")

def process_data(input_file, output_file):
    df = read_excel_file(input_file)
    columns = get_columns(df)
    sorted_data = sort_data(df, columns)
    write_excel_file(output_file, sorted_data)

def main():
    with open("src/files.txt", 'r') as files:
        files = files.readlines()
    while files: # while not empty list
        input_file = files.pop().strip() # removes whitespaces and newline characters
        output_file = input_file
        process_data(input_file, output_file)

    print("\nFinished!")

if __name__ == "__main__":
    main()