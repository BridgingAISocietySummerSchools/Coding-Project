# Challenge 1: Wine Quality Prediction AI Project

**Theme:** AI for quality assessment and decision-making in agriculture and food industry.

## Description

Wine quality assessment is traditionally done by expert sommeliers, but this process can be subjective and time-consuming. This project involves building an AI system that can predict wine quality based on physicochemical properties, helping wineries maintain consistent quality standards and optimize their production processes. This demonstrates how AI can augment human expertise in specialized domains.

## Project Idea

Students will develop a machine learning model that analyzes wine chemical properties to predict quality scores. They'll explore feature relationships, handle imbalanced datasets, and build both regression and classification models. The challenge involves understanding how different chemical properties interact to determine wine quality and creating interpretable models for domain experts.

## Dataset

### About the Wine Quality Dataset

The dataset (`data/wine_quality_dataset.csv`) contains 1,599 wine samples with physicochemical properties and quality ratings. This dataset is inspired by the famous UCI Wine Quality dataset and provides realistic examples of wine chemistry and quality assessment challenges.

#### Dataset Structure
- **Total Records**: 1,599 wine samples  
- **Features**: 11 physicochemical properties + wine type
- **Target Variables**: Quality score (4-6) and quality category (poor/average/good)

#### Chemical Properties (Features)
- `fixed_acidity`: Tartaric acid concentration (affects taste)
- `volatile_acidity`: Acetic acid concentration (vinegar taste in high amounts)
- `citric_acid`: Freshness and flavor enhancer
- `residual_sugar`: Remaining sugar after fermentation (sweetness)
- `chlorides`: Salt concentration
- `free_sulfur_dioxide`: SO2 preventing microbial growth
- `total_sulfur_dioxide`: Total SO2 (wine preservation)
- `density`: Wine density (related to alcohol and sugar content)
- `pH`: Acidity level (affects taste and stability)
- `sulphates`: Wine preservative and antioxidant
- `alcohol`: Alcohol percentage by volume
- `type`: Wine type (red or white)

#### Target Variables
- `quality`: Quality score from 4-6 (regression target)
- `quality_category`: Categorical quality (poor/average/good) for classification

#### Quality Distribution
- **Average Quality**: 1,184 wines (74.1%) - Most common quality level
- **Poor Quality**: 355 wines (22.2%) - Below average wines
- **Good Quality**: 60 wines (3.8%) - Premium quality wines

#### Educational Value
This dataset allows students to explore:
- **Regression vs Classification**: Predict numerical scores or categorical quality
- **Feature Engineering**: Understanding chemical property relationships
- **Imbalanced Data**: Handling uneven quality distributions
- **Model Interpretability**: Explaining predictions to domain experts
- **Real-world Applications**: Quality control in manufacturing industries

#### Wine Type Analysis
- **Red Wines**: 964 samples (60.3%)
- **White Wines**: 635 samples (39.7%)
- Students can explore if wine type affects quality prediction models

#### Real-World Applications
- **Quality Control**: Automated wine quality assessment in production
- **Process Optimization**: Understanding which chemical properties to control
- **Cost Reduction**: Reducing reliance on expensive expert tasters
- **Consistency**: Maintaining uniform quality standards across batches

#### Ethical Considerations
- **Expert Augmentation**: AI as a tool to support, not replace, human expertise
- **Transparency**: Ensuring wine quality decisions are explainable
- **Cultural Sensitivity**: Respecting traditional wine-making practices
- **Economic Impact**: Effects on employment in quality assessment roles

## Tools and Libraries

- Python
- pandas (for data manipulation and analysis)
- scikit-learn (for machine learning models and evaluation)
- matplotlib/seaborn (for data visualization)
- numpy (for numerical computations)
- Optional: XGBoost or LightGBM (for advanced ensemble methods)

## Estimated Time

3 hours (focus on exploratory data analysis, feature engineering, and model building).

## Files

- `data/`: Contains the resume dataset
- `notebooks/educational_notebook_1.ipynb`: Guided notebook for students
- `notebooks/solution_notebook_1.ipynb`: Complete solution
- `requirements.txt`: Python dependencies

## Getting Started

1. Install the required packages: `pip install -r requirements.txt`
2. Generate the wine dataset: `python create_wine_dataset.py` (if not already present)
3. Open the educational notebook: `jupyter notebook notebooks/educational_notebook_1.ipynb`
4. Follow the guided instructions to complete the wine quality prediction challenge

