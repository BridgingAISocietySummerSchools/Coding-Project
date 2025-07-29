# AI and Society Summer School Coding Challenges

This repository contains three coding challenges designed for the "Bridging AI and Society" summer school program. Each challenge focuses on a different aspect of AI's societal impact and is designed to be completed within approximately three hours. The challenges include educational notebooks to guide students and **real-world datasets** for authentic learning experiences.

## Challenges

1.  **Challenge 1: Wine Quality Prediction AI Project**
    -   **Theme:** AI for quality assessment and decision-making in agriculture and food industry.
    -   **Description:** Build an AI system to predict wine quality based on physicochemical properties, demonstrating how AI can augment human expertise in specialized domains.
    -   **Dataset:** Real wine quality data from Kaggle (1,143 authentic wine samples) ✅ **Ready to use!**
    -   **Files:** `challenge_1/`
    -   **🚀 Run in Google Colab:**
        - [![Open Educational Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BridgingAISocietySummerSchools/Coding-Project/blob/main/challenge_1/notebooks/educational_notebook_1.ipynb)

2.  **Challenge 2: Fake News Detector Project in AI**
    -   **Theme:** AI for combating misinformation and promoting media literacy.
    -   **Description:** Develop a system to identify and classify news articles as either real or fake using NLP techniques.
    -   **Dataset:** Real fake news data from Kaggle (40,000+ news articles) ✅ **Ready to use!**
    -   **Files:** `challenge_2/`
    -   **🚀 Run in Google Colab:**
        - [![Open Educational Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BridgingAISocietySummerSchools/Coding-Project/blob/main/challenge_2/notebooks/educational_notebook_2.ipynb)

3.  **Challenge 3: Social Media Spam Detection**
    -   **Theme:** AI for digital well-being and combating online harassment.
    -   **Description:** Build an AI model to automatically detect and filter out spam comments on social media platforms using real YouTube data.
    -   **Dataset:** Real YouTube spam data from UCI ML Repository (1,956 comments) ✅ **Ready to use!**
    -   **Files:** `challenge_3/`
    -   **🚀 Run in Google Colab:**
        - [![Open Educational Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BridgingAISocietySummerSchools/Coding-Project/blob/main/challenge_3/notebooks/educational_notebook_3.ipynb)

## Repository Structure

```
summer_school_challenges/
├── challenge_1/
│   ├── data/                  # Dataset for Challenge 1
│   ├── notebooks/             # Jupyter notebooks for Challenge 1
│   │   └── educational_notebook_1.ipynb
│   ├── requirements.txt       # Python dependencies for Challenge 1
│   └── README.md              # Challenge-specific README
├── challenge_2/
│   ├── data/                  # Dataset for Challenge 2
│   ├── notebooks/             # Jupyter notebooks for Challenge 2
│   │   └── educational_notebook_2.ipynb
│   ├── requirements.txt       # Python dependencies for Challenge 2
│   └── README.md              # Challenge-specific README
├── challenge_3/
│   ├── data/                  # Dataset for Challenge 3
│   ├── notebooks/             # Jupyter notebooks for Challenge 3
│   │   └── educational_notebook_3.ipynb
│   ├── create_dataset.py      # Script to generate sample dataset
│   ├── requirements.txt       # Python dependencies for Challenge 3
│   └── README.md              # Challenge-specific README
├── requirements.txt           # Global project dependencies
└── README.md                  # Main repository README
```

## Real-World Datasets Overview

Each challenge now uses **authentic real-world datasets** for meaningful learning experiences:

### Challenge 1: Wine Quality Prediction Dataset ✅ **Ready to Use**
- **Source**: [Kaggle Wine Quality Dataset](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)
- **Size**: 1,143 authentic wine samples with 11 chemical properties
- **Features**: Fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, sulfur dioxide, density, pH, sulphates, alcohol
- **Target**: Quality scores (3-8) from professional wine tasters
- **Key Learning**: Feature engineering, regression vs classification, model interpretation
- **Societal Impact**: Understanding AI's role in augmenting human expertise in specialized domains

### Challenge 2: Real Fake News Detection Dataset ✅ **Ready to Use**
- **Source**: [Kaggle Fake News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- **Size**: 40,000+ real news articles (mix of authentic and fake news)
- **Features**: Article titles, content, publication info
- **Target**: Binary classification (Real vs Fake)
- **Key Learning**: Binary text classification with real misinformation patterns
- **Societal Impact**: Building tools for media literacy and information integrity

### Challenge 3: Real YouTube Spam Detection Dataset ✅ **Ready to Use**
- **Source**: [UCI ML Repository YouTube Spam Collection](https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection)
- **Size**: 1,956 authentic YouTube comments from popular music videos
- **Features**: Comment text from real YouTube users
- **Target**: Binary classification (Ham vs Spam)
- **Key Learning**: Short-text classification with real social media language
- **Societal Impact**: Protecting digital well-being and reducing online harassment

## Getting Started

### Prerequisites
- Python 3.8+ with pip
- Jupyter Notebook or JupyterLab (or use Google Colab - no setup required!)
- Git (for cloning the repository)

### 🚀 Option 1: Run in Google Colab (Recommended for Beginners)

**No installation required!** Click any of the Colab badges above to run the notebooks directly in your browser:

- ✅ **Zero Setup**: No need to install Python, Jupyter, or dependencies
- ☁️ **Cloud Computing**: Free GPU/TPU access for faster training
- 💾 **Auto-Save**: Your work is saved to Google Drive automatically
- 🤝 **Easy Sharing**: Share your results with instructors or classmates
- 📱 **Any Device**: Works on laptops, tablets, and even phones

**How to use Colab:**
1. Click a Colab badge above for any challenge
2. Sign in with your Google account
3. Click "Copy to Drive" to save your own version
4. Start coding immediately!

### 🖥️ Option 2: Local Installation

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd summer_school_challenges
    ```

2.  **Navigate to the desired challenge directory:**
    ```bash
    cd challenge_1 # or challenge_2, challenge_3
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up datasets:**
    - **All Challenges**: All datasets are pre-installed and ready to use! ✅

5.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook notebooks/educational_notebook_1.ipynb # or 2, 3
    ```

Follow the instructions within the educational notebook to complete the challenge.

### Updated Requirements

Core dependencies across all challenges:
```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.5.0
seaborn>=0.11.0
jupyter>=1.0.0
nltk>=3.7
ucimlrepo>=0.0.7
```

## Troubleshooting & Support

### Common Issues

**Missing Dependencies:**
```bash
# Update pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# If issues persist, try creating a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## License & Attribution

- **Educational Use**: These materials are designed for educational purposes
- **Dataset Credits**: 
  - Wine Quality: UCI ML Repository via Kaggle
  - Fake News: Kaggle community dataset
  - YouTube Spam: UCI ML Repository
- **Open Source**: Code and notebooks available for educational use

---

**Ready to explore AI's impact on society? Start with Challenge 1 and dive into the world of machine learning with real data!** 🚀

