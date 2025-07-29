# Challenge 2: Fake News Detector Project in AI

**Theme:** AI for combating misinformation and promoting media literacy.

## Description

The spread of fake news is a significant societal challenge, especially during critical events like elections or public health crises. This project aims to build a system that can identify and classify news articles as either real or fake, contributing to a more informed public discourse.

## Project Idea

Students will work with a dataset of news articles labeled as real or fake. They will apply machine learning techniques, particularly natural language processing (NLP), to analyze the text content of these articles and develop a classification model. The challenge involves feature engineering from text data and training a robust classification model.

## Dataset

### About the Fake News Detection Dataset

The dataset (`data/fake_news_dataset.csv`) contains 300 news articles specifically designed to teach students about misinformation detection using AI. This educational dataset reflects real-world challenges in distinguishing credible journalism from false information.

#### Dataset Structure
- **Total Records**: 300 news articles
- **Columns**: 3 essential features
  - `title`: News article headline
  - `text`: Complete article body content
  - `label`: Binary classification (0 = Fake News, 1 = Real News)

#### Label Distribution
- **Perfectly Balanced**: 150 fake news articles (50%) and 150 real news articles (50%)
- **Prevents Model Bias**: Equal representation ensures fair learning without class imbalance issues

#### Content Characteristics
- **Average Article Length**: ~277 characters per article
- **Diverse Topics**: Climate science, technology, economics, health, politics, and conspiracy theories
- **Realistic Language Patterns**: Both fake and real articles use believable journalistic language
- **Distinguishable Features**: Fake news often includes:
  - Sensational or extraordinary claims ("Miracle cure", "Aliens among us")
  - Vague sourcing ("anonymous scientists", "leaked documents")
  - Emotional manipulation tactics
  - Conspiracy-oriented content

#### Real News Examples
- Climate change reports with scientific backing
- Economic employment statistics with verifiable data
- Corporate announcements from legitimate sources
- Technology industry developments

#### Fake News Examples
- Unsubstantiated medical miracle claims
- Government conspiracy theories
- Extraordinary scientific discoveries without peer review
- Sensational discoveries with anonymous sources

#### Educational Value
This dataset enables students to explore:
- **Text Classification**: Binary classification using NLP techniques
- **Feature Engineering**: Extracting meaningful patterns from article text
- **Critical Thinking**: Understanding how language patterns reveal misinformation
- **Societal Impact**: Learning about AI's role in combating misinformation
- **Evaluation Metrics**: Using precision, recall, and F1-score for sensitive classification tasks

#### Real-World Applications
- **Social Media Platforms**: Automated content moderation systems
- **News Aggregators**: Credibility scoring for articles
- **Browser Extensions**: Real-time fact-checking tools
- **Educational Tools**: Media literacy training platforms

#### Ethical Considerations
- Highlights the responsibility of AI developers in information integrity
- Demonstrates potential for both beneficial applications and harmful misuse
- Emphasizes the need for human oversight in automated fact-checking systems
- Teaches students about algorithmic transparency and accountability

## Tools and Libraries

- Python
- scikit-learn
- TensorFlow/Keras (for BERT, optional)
- NLTK
- pandas (for data manipulation)
- matplotlib/seaborn (for visualization)

## Estimated Time

3 hours (focus on data preprocessing, model training, and evaluation).

## Files

- `data/`: Contains the fake news dataset
- `notebooks/educational_notebook_2.ipynb`: Guided notebook for students
- `notebooks/solution_notebook_2.ipynb`: Complete solution
- `requirements.txt`: Python dependencies

## Getting Started

1. Install the required packages: `pip install -r requirements.txt`
2. Open the educational notebook: `jupyter notebook notebooks/educational_notebook_2.ipynb`
3. Follow the guided instructions to complete the challenge

