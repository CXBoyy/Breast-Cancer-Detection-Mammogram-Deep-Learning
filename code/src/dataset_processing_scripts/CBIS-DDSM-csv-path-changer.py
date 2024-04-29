import os
import pandas as pd
import re
import glob

root_path = "/Code/KEX-Job/Breast-Cancer-Detection-Mammogram-Deep-Learning/code/data"
paths = [root_path + "/CBIS-DDSM/", root_path + "/CBIS-DDSM-mask/"]
target_path = "/Code/KEX-Job/Breast-Cancer-Detection-Mammogram-Deep-Learning/code/data/CBIS-DDSM/"

def change_img_path(file_path, new_path):
    
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Change the "img_path" column
    df['img_path'] = df['img_path'].apply(lambda x: new_path + re.search(r'/CBIS-DDSM/(.*)', x).group(1) if re.search(r'/CBIS-DDSM/(.*)', x) else x)
    df['img_path'] = df['img_path'].str.replace(r"//", "/")
    
    # Save the modified DataFrame back to the CSV file
    df.to_csv(file_path, index=False)
    
def merge_csv(path):
    csv1 = pd.read_csv(path + "calc-test.csv")
    csv2 = pd.read_csv(path + "mass-test.csv")
    df = pd.concat([csv1, csv2])
    df.to_csv(path + "testing.csv")
    
    csv1 = pd.read_csv(path + "calc-training.csv")
    csv2 = pd.read_csv(path + "mass-training.csv")
    df = pd.concat([csv1, csv2])
    df.to_csv(path + "training.csv")

def make_smaller_csv(folderPath, filePath, file_name):
    df = pd.read_csv(folderPath + filePath)
    df = df.drop(list(range(0, 2400, 1)), axis=0)
    df.to_csv(folderPath + file_name)
    
def main():
    """ for path in paths:
        change_img_path(path, target_path) """
    for path in paths:
        merge_csv(path)
        make_smaller_csv(path, "training.csv", "trainingSmaller.csv")
        
if __name__ == "__main__":
    main()