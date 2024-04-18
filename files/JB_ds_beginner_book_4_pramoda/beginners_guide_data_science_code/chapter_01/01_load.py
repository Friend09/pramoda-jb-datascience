# Load the Ames dataset
import pandas as pd
Ames = pd.read_csv('/Users/vamsi_mbmax/Library/CloudStorage/OneDrive-Personal/01_vam_PROJECTS/SIDE_PROJECTS/proj_Pramoda_python/subproj_jb_datascience/files/JB_ds_beginner_book_4_pramoda/beginners_guide_data_science_code/chapter_01/Ames.csv')
print(Ames)
# Ames = pd.read_csv('Ames.csv')

# Dataset shape
print(Ames.shape)

rows, columns = Ames.shape
print(f"The dataset comprises {rows} properties described across {columns} attributes.")
