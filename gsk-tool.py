##################################################################################################################
### SCRIPT TO READ IN CSV FILES AND CREATE A CSV TEMPLATE ###

### SUMMARY OF STEPS:
### STEP 1: READ IN ALL CSV FILES AND BIND 'name_v' COLUMNS TOGETHER
### STEP 2: SORT VALUES IN EACH COLUMN ALPHABETICALLY
### STEP 3: CHANGE COLUMN NAMES AND SORT COLUMNS BY SPECIFIC ORDER
### STEP 4: BIND LEFT SIDE OF TEMPLATE
### STEP 5: WRITE OUT TABLE AS CSV FILE

##################################################################################################################
import pandas as pd

##### CHANGE FILE NAME/DIRECTORY within the '' #####
# read-in file directory (folder)
file_path = ''

# write-out file directory
out_file = ''


##################################################################################################################


##### CHANGE FILE NAME/DIRECTORY within the '' #####
# read in matching and order key table
c_order = pd.read_excel('C:\\Users\\CeciliaLuna\\Documents\\Daelight Tool Box Helpful Documents\\Stephens Helpful Documents\\Consumer Template CodeCSVs\\Consumer Template Code_CSVs\\consumer_template_matchkey.csv')

# read in left side of template to bind later
temp_left = pd.read_excel('C:\\Users\\CeciliaLuna\\Documents\\Daelight Tool Box Helpful Documents\\Stephens Helpful Documents\\Consumer Template CodeCSVs\\Consumer Template Code_CSVs\\consumer_template_LEFT.csv')


##################################################################################################################