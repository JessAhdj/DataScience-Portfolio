################################
#           Projet 1           #
#     Chess Game (Lichess)     #
#   Author : Jessim Ahdjoudj   #
################################

##################
### 1) Imports ###
##################

import pandas as pd

#######################
### 2) Get the data ###
#######################

df = pd.read_csv('chessgames.csv')

###########################
### 3) Date exploration ###
###########################
print('\n--- Data exploration ---\n')

# Get summary infos of the data
print('- Data infos -')
df.info()
print('\n')
print(df.describe())
print('\n')
print(df.isnull().sum())

# Get numbers of rows and columns in dataset
print('\n')
print('Data shape infos :', df.shape)
print('\n')

# See what the dataset looks like
print('- Dataset overview -')
print(df)

##############################
### 4) Data transformation ###
##############################
print('\n--- Data transformation ---\n')
# Transforming the data for simpler analysis

print('\n- Data cleaning -\n')
# Cleaning the data : remove columns with weird data and the non usefull ones
df.drop(['id', 'created_at', 'last_move_at', 'white_id', 'black_id'],axis=1,inplace=True) 
print(df)

print('\n- Data modification -\n')
# Create new columns for more information on the players

level_list=[]
def level_creator(rating):
    level=str()
    if rating<=1200:
        level='Class E Player'
    elif 1200<rating<=1400:
        level='Class D player'
    elif 1400<rating<=1600:
        level='Class C player'
    elif 1600<rating<=1800:
        level='Class B player'
    elif 1800<rating<=2000:
        level='Class A player'
    elif 2000<rating<=2200:
        level='Expert'
    elif 2200<rating<=2300:
        level='FIDE candidate master'
    elif 2300<rating<=2400:
        level='FIDE master'
    elif 2400<rating<=2500:
        level='International masters'
    elif rating>2500:
        level='Grandmasters'
    level_list.append(level)

df['white_rating'].map(level_creator) # use map for interact  values
df['white level']=level_list # add new column

level_list=[]    # recreate this list beacuse we will use it for blacks

df['black_rating'].map(level_creator)
df['black level']=level_list # add new column

print('White players \n', df['white level'].value_counts())
print('\n')
print('Black players \n', df['black level'].value_counts())

# Rearrange columns using list rather than typing columns one by one
print('Rearrange')
columns = list(df.columns.values)
df = df[[columns[0]] + [columns[5]] +[columns[6]] + columns[1:5] + columns[7:13]]
print('\n')
print(df)

print('\n- Data filtering -\n')
# Removing short games
df = df.loc[df.turns > 2]

# Filtering data based on game type played
# Less than 3 minutes: Bullet
# Between 3 and 9: Blitz
# Between 9 and 16: Rapid
# More than 16 minutes: Classical

# Filtering data based on color played
print('Black')
black_players = df[df.winner == 'black']
print(black_players)

print('White')
white_players = df[df.winner == 'white']
print(white_players)

# Filtering data based on ranking or not
print('Ranked')
ranked_players = df[df['rated']] #for True
print(ranked_players)

print('Unranked')
unranked_players = df[~df['rated']] #for False
print(unranked_players)

# Filtering data based on opening move
print('E4 openings')
king_pawn_opening = df[df['moves'].str.startswith('e4')]
print(king_pawn_opening)

print('D4 openings')
queen_pawn_opening = df[df['moves'].str.startswith('d4')]
print(queen_pawn_opening)
