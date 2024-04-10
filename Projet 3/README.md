# Projet 3 : Analyse de Sentiments d'avis Amazon

## Description projet
Dans ce projet, on s'intéresse aux émotions et au feedback d'avis Amazon sur différents produits comestibles raffinés. Pour ce faire, on réalise une Analyse de Sentiments (Sentiment Analysis) dans laquelle on développe un algorithme de Machine Learning de Traitement du Langage Naturel (NLP) pour identifier les émotions derrière le texte des d'avis et analyser si les produits sont appréciés par le public. Pour ce modèle, on utilisera 2 approches et donc 2 modèles : 
- Modèle 1 : approche "bag of words" avec usage du VADER (Valence Aware Dictionary and sEntiment Reasoner) Sentiments Scoring (de C.J. Hutto et Eric Gilbert)
- Modèle 2 : approche "Transformer" avec usage du Roberta Pretrained Model (de Hugging Face)

Enfin, on analysera comment chaque modèle performe pour déterminer quel est le plus optimal à utiliser.

## Dataset
Le Dataset est disponible sur Kaggle : [Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews). Il contient un ensemble de critiques d'aliments comestibles raffinés en vente sur la plateforme Amazon. Les données couvrent une période de plus de 10 ans, incluant les quelque 500 000 avis jusqu'en octobre 2012. Les avis incluent des informations sur les produits et les utilisateurs, des évaluations et un avis en texte brut. Il comprend également des avis de toutes les autres catégories Amazon.

## Compétences et techniques utilisées
- [x] Machine Learning
- [X] Développer un modèle d'Intelligence Artificielle
- [X] Traitement du Langage Naturel / Natural Language Processing (NLP)
- [x] VADER (Valence Aware Dictionary and sEntiment Reasoner) Sentiments Scoring / Bag of Words
- [X] Roberta Pretrained Model / Transformer
- [x] Analyser un jeu de données
- [X] Evaluation des performances d'un modèle

> [!NOTE]
> Pour fonctionner sur votre machine, ce projet nécessite que vous possediez une version de Python 3.10.6 minimum ainsi que les librairies numpy, pandas, matplotlib, seaborn, nltk, tqdm, transformers et scipy.
