# Challenge 3: Instagram Spam Detection

**Theme:** AI for digital well-being and combating online harassment.

## Description

Social media platforms are often plagued by spam comments, which can range from annoying to malicious. This project focuses on developing an AI model to automatically detect and filter out spam comments on platforms like Instagram, improving the user experience and reducing exposure to unwanted content.

## Project Idea

Students will build a spam detection system using text classification techniques. They will need to identify characteristics of spam comments versus legitimate comments and train a model to distinguish between them. This project can involve exploring different NLP techniques and understanding how to handle imbalanced datasets (more legitimate comments than spam).

## Dataset

### About the Real YouTube Spam Detection Dataset

The dataset (`data/spam_detection_dataset.csv`) contains **1,956 real YouTube comments** from the UCI Machine Learning Repository's YouTube Spam Collection. This authentic dataset was collected from 5 popular YouTube videos and provides genuine examples of spam and legitimate social media interactions.

#### Dataset Source & Authenticity
- **Original Source**: UCI Machine Learning Repository (Dataset ID: 380)
- **Real-World Data**: Actual YouTube comments, not synthetic or generated
- **Collection Method**: Comments extracted from 5 of the most-viewed YouTube videos
- **Research Purpose**: Originally collected for academic spam research
- **Videos Included**: Psy, Katy Perry, LMFAO, Eminem, and Shakira music videos

#### Dataset Structure
- **Total Records**: 1,956 real social media comments
- **Columns**: 2 key features
  - `comment`: Original YouTube comment text
  - `label`: Binary classification (0 = Ham/Legitimate, 1 = Spam)

#### Label Distribution
- **Spam Comments**: 1,005 comments (51.4%) 
- **Ham Comments**: 951 comments (48.6%)
- **Near-Perfect Balance**: Minimal class imbalance for fair model training

#### Content Characteristics
- **Concise Format**: Average comment length of ~29 characters (typical social media brevity)
- **Realistic Language**: Authentic social media communication patterns
- **Diverse Spam Types**: Various spam categories represented in the dataset

#### Real Content Examples

**Authentic SPAM Comments from YouTube:**
- "Hey guys check out my new channel and our first vid THIS IS US THE MONKEYS!!!"
- "me shaking my sexy ass on my channel enjoy ^_^ ﻿"
- "watch?v=vtaRGgvGtWQ   Check this out .﻿"
- "just for test I have to say murdev.com"

**Authentic HAM Comments from YouTube:**
- "i turned it on mute as soon is i came on i just wanted to check the views...﻿"
- "I'm only checking the views﻿"
- "just checking the views﻿"  
- "I dont even watch it anymore i just come here to check on 2 Billion or not﻿"

#### Real-World Patterns
- **Promotion Spam**: Channel promotion, self-advertising
- **Link Spam**: External website references, suspicious URLs
- **Engagement Spam**: Requests for likes, follows, subscriptions
- **Legitimate Comments**: Genuine reactions to video content, view counting, authentic discussions

#### Educational Value
This dataset allows students to explore:
- **Short Text Classification**: Handling brief, informal text typical of social media
- **Pattern Recognition**: Identifying linguistic patterns that distinguish spam from legitimate content
- **Feature Engineering**: Extracting meaningful signals from minimal text data
- **Digital Well-being**: Understanding AI's role in creating safer online spaces
- **Content Moderation**: Learning about automated systems that protect user experience

#### Real-World Applications
- **Social Media Platforms**: Instagram, Twitter, TikTok comment filtering
- **E-commerce Sites**: Product review spam detection
- **Online Forums**: Community moderation and quality control
- **Email Systems**: Advanced spam filtering beyond traditional methods

#### Technical Challenges
- **Limited Context**: Making decisions with very short text snippets
- **Language Evolution**: Staying current with changing spam tactics and slang
- **False Positives**: Avoiding censorship of legitimate but promotional content
- **Multilingual Considerations**: Handling diverse languages and cultural contexts

#### Ethical Considerations
- **Freedom of Expression**: Balancing spam detection with user rights
- **Algorithmic Bias**: Ensuring fair treatment across different user groups
- **Transparency**: Users should understand how content moderation decisions are made
- **Human Oversight**: Maintaining human review for complex edge cases

#### Machine Learning Insights
- **Class Balance**: Perfect 50/50 split eliminates need for resampling techniques
- **High Accuracy Potential**: Well-defined differences between classes enable strong model performance
- **Generalization**: Students learn to build models that work across different social platforms

## Tools and Libraries

- Python
- NLTK
- scikit-learn
- pandas (for data manipulation)
- matplotlib/seaborn (for visualization)

## Estimated Time

3 hours (focus on data preparation, feature extraction, and model building).

## Files

- `data/`: Contains the spam detection dataset
- `notebooks/educational_notebook_3.ipynb`: Guided notebook for students
- `notebooks/solution_notebook_3.ipynb`: Complete solution
- `requirements.txt`: Python dependencies

## Getting Started

1. Install the required packages: `pip install -r requirements.txt`
2. Open the educational notebook: `jupyter notebook notebooks/educational_notebook_3.ipynb`
3. Follow the guided instructions to complete the challenge

