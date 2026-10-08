
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/students.csv')
    print(df.head())

if __name__ == "__main__":
    main()