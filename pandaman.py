import pandas as pd

def parse_file(file_path):
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            data = pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            data = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format")
        
        print(data)
    except Exception as e:
        print(f"Error parsing file: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    parse_file(file_path)
