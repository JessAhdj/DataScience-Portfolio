################################
#           Projet 1           #
#     Chess Game (Lichess)     #
#   Author : Jessim Ahdjoudj   #
################################

##################
### 1) Imports ###
##################

import pandas as pd
import zipfile
import kaggle

###############################
### 2) Get the data, 2 ways ###
###############################

# Choose one way by either commenting Way 1 or uncommenting Way 2

# Way 1 - classic #
data = pd.read_csv('chessgames.csv')

# Way 2 - to be more fancy #
# download dataset from kaggle using the Kaggle API
# kaggle datasets download -d datasnaek/chess

# extract the file from the downloaded zip file
# zipfile_name = 'Chess.zip'
# with zipfile.ZipFile(zipfile_name, 'r') as file:
#    file.extractall()

# data = pd.read_csv('chessgames.csv')

###########################
### 3) Date exploration ###
###########################
print('\n----- Data exploration -----\n')

# Get summary and preliminary infos of the dataset
print('--- Data infos ---')
print('\n Summary :\n') 
data.info()
print('\n Descriptive statistics :\n', data.describe())
print('\n Data shape infos :\n', data.shape)
print('\n Check for missing values :\n', data.isnull().sum())

# See what the dataset looks like
print('\n--- Dataset overview ---\n')
print(data)

##############################
### 4) Data transformation ###
##############################
print('\n----- Data transformation -----\n')
# Transforming the data for a simpler analysis

print('\n--- Data cleaning ---\n')
# Cleaning the data : remove columns with weird data and the non usefull ones
data.drop(['id', 'created_at', 'last_move_at', 'white_id', 'black_id'],axis=1,inplace=True) 
print('Cleaned data :\n', data)

# Removing short games
data = data.loc[data.turns > 2]

print('\n--- Data modification ---\n')
# Modifying the data to have more infos

print('\n- Adding columns -\n')
# Create new columns for more information on the players
# Raking definition
def level_creator(rating):
    level = str() #official FIDE rating levels
    if rating<=1200:
        level = 'Class E Player'
    elif 1200<rating<=1400:
        level = 'Class D player'
    elif 1400<rating<=1600:
        level = 'Class C player'
    elif 1600<rating<=1800:
        level = 'Class B player'
    elif 1800<rating<=2000:
        level = 'Class A player'
    elif 2000<rating<=2200:
        level = 'Expert'
    elif 2200<rating<=2300:
        level = 'FIDE candidate master'
    elif 2300<rating<=2400:
        level = 'FIDE master'
    elif 2400<rating<=2500:
        level = 'International masters'
    elif rating>2500:
        level = 'Grandmasters'
    level_list.append(level)

# Add new column for white
level_list = []
data['white_rating'].map(level_creator)
data['white level'] = level_list # add new column

# Add new column for black
level_list = [] # recreate this list to be used for black
data['black_rating'].map(level_creator)
data['black level'] = level_list # add new column

print('Number of white players per rating \n', data['white level'].value_counts())
print('\n Number of black players per rating \n', data['black level'].value_counts())

print('\n- Rearrange columns -\n')
# Rearrange columns using list rather than typing columns one by one
columns = list(data.columns.values)
data = data[[columns[0]] + [columns[5]] +[columns[6]] + columns[1:5] + columns[7:13]]
print('Rearranged data :\n', data)

print('\n--- Data filtering ---\n')
# Filtering data based on color played
black_wins = data[data.winner == 'black']
print('Games with black win', black_wins)

white_wins = data[data.winner == 'white']
print('Games with white win', white_wins)

# Filtering data based on rated or not
Rated_players = data[data['rated']] #for True
print('Games with rated players', Rated_players)

Unrated_players = data[~data['rated']] #for False
print('Games with unrated players', Unrated_players)

# Filtering data based on opening move
king_pawn_opening = data[data['moves'].str.startswith('e4')]
print('Games with E4 openings', king_pawn_opening)

queen_pawn_opening = data[data['moves'].str.startswith('d4')]
print('Game with D4 openings', queen_pawn_opening)
