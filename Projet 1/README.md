# Projet 1 : Analyse Exploratoire de Données (EDA) des chansons Spotify les plus écoutés (steams) en 2023

## Description projet
Dans ce projet, on s’intéresse aux chansons les plus écoutés (càd avec le plus de steams) sur la plateforme Spotify en 2023. Pour ce faire, réalisons une Analyse Exploratoire de Données (EDA) complète afin de savoir quels artistes sont les plus écoutés et quelles sont les caractéristiques qu'une chanson doit avoir pour être beaucoup écoutée.

### Dataset
Le Dataset est joint au repository et trouvable ici : [spotify_2023.csv](https://github.com/JessAhdj/DataScience-Portfolio/blob/main/Projet%201/spotify_2023.csv). Il contient la liste des chansons les plus écoutés de 2023 répertoriées sur Spotify. Le Dataset offre une multitude de fonctionnalités au-delà de ce qui est généralement disponible dans des ensembles de données similaires : il donne un aperçu des attributs, de la popularité et de la présence de chaque chanson sur diverses plateformes musicales. Ainsi, le Dataset comprend des informations telles que le nom de la chanson, le nom du ou des artistes, la date de sortie, les listes de lecture et les graphiques Spotify, les statistiques de streaming, la présence d'Apple Music, la présence de Deezer, les graphiques Shazam et diverses fonctionnalités audio ; informations intéressantes et pertinantes pour une analyse de données approfondie.

### Conclusion de l'analyse
L'analyse de ce Dataset montre qu'il semble que les chansons les plus écoutées sur Spotify ont des points communs. Si vous souhaitez créer une chanson et qu'elle soit la plus populaire possible, le mode (Majeur/Mineur), la clé d'écriture et le BPM jouent un rôle plus important que les autres paramètres :
- Mode : on constate que le mode Majeur est préférable ; 70% dans le top 10 et 59.5% dans les autres top en moyenne.
- Clé : on constate que Do Majeur (C#) est la clé la plus utilisée ; 30% dans le top 10 et 15.158% dans les autres top en moyenne.
- BPM : on constate que le BPM est important ; un rythme supérieur à la fréquence cardiaque, mais pas trop rapide, compris entre 90 BPM et 120 BPM est le plus adéquat.

Pour une conclusion complète, voir le Pdf joint au repository : [Conclusion_EDA_Spotify.pdf](https://github.com/JessAhdj/DataScience-Portfolio/blob/main/Projet%201/Conclusion_EDA_Spotify.pdf).

## Compétences et techniques utilisées
- [x] Nettoyer un jeu de données
- [x] Décrire un jeu de données par statistique descriptive
- [x] Identifier les variables d'intérêts
- [x] Interpréter et donner un regard critique sur des données graphiques
- [x] Analyser un jeu de données
- [x] Partagez les découvertes et conclusion de l'analyse
- [x] Permettre aux entreprises du secteur musical de prendre des décisions basées sur les données analysées

> [!NOTE]
> Pour fonctionner sur votre machine, ce projet nécessite que vous possediez une version de Python 3.10.6 minimum ainsi que les libraires numpy, pandas, matplotlib et seaborn.
