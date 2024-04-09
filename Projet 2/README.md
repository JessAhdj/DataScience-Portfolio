# Projet 2 : Classification (Classifier) de cartes de jeu par réseau neuronal convolutif (CNN)

## Description projet
Dans ce projet, on cherche à développer un modèle de Machine Learning simple, un classificateur d'images capable de détecter des cartes à jouer. Pour ce faire, on développe un réseau neuronal convolutif (CNN) avec la librairie PyTorch qui est capable de prendre des images, puis de détecter quelle carte est dans cette image après traitement par le modèle (notre CNN).

## Dataset
Le Dataset est disponible sur Kaggle : [Cards Image Dataset-Classification](https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification). Il contient un ensemble d’images de cartes à jouer de très haute qualité. Toutes les images ont une taille de 224 X 224 X 3 au format jpg qui ont été recadrées de sorte que seule l'image d'une seule carte soit présente et que la carte occupe bien plus de 50 % des pixels de l'image. Le Dataset comporte 7 624 images d'entrainement, 265 images de test et 265 images de validation. Les dossiers d'entrainement, test et validation sont divisés en 53 sous-dossiers, un pour chacun des 53 types de cartes. Le Dataset comprend également un fichier csv qui peut être utilisé pour charger les ensembles de données.

## Compétences et techniques utilisées
- [x] Machine Learning / Deep Learning
- [X] Développer un modèle d'Intelligence Artificielle
- [X] Classification automatique
- [x] Développer un réseau neuronal convolutif (CNN)
- [x] Analyser un jeu de données
- [X] Evaluation des performances d'un modèle

> [!NOTE]
> Pour fonctionner sur votre machine, ce projet nécessite que vous possediez une version de Python 3.10.6 minimum ainsi que les librairies numpy, pandas, matplotlib, timm, tqdm, PIL et torch.
