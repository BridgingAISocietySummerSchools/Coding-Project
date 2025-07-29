import pandas as pd
import random

# Sample fake and real news headlines and content
fake_news_samples = [
    {
        "title": "Scientists Discover Aliens Living Among Us",
        "text": "A groundbreaking study reveals that extraterrestrial beings have been secretly living in major cities worldwide. The research, conducted by an anonymous group of scientists, claims to have found definitive proof of alien presence. Government officials have yet to comment on these shocking revelations.",
        "label": 0
    },
    {
        "title": "Miracle Cure for All Diseases Found in Common Kitchen Ingredient",
        "text": "Researchers claim that a simple kitchen ingredient can cure cancer, diabetes, and heart disease. The study, published in an obscure journal, suggests that this ingredient has been overlooked by mainstream medicine. Doctors are skeptical of these extraordinary claims.",
        "label": 0
    },
    {
        "title": "Celebrity Spotted with Secret Twin Nobody Knew About",
        "text": "Paparazzi photos reveal that a famous celebrity has been hiding a twin sibling for decades. Sources close to the family confirm the existence of this secret twin. The celebrity's representatives have denied all claims and called the story fabricated.",
        "label": 0
    },
    {
        "title": "New Technology Allows People to Read Minds",
        "text": "A startup company claims to have developed technology that can read human thoughts with 100% accuracy. The device, which looks like a simple headband, allegedly translates brain waves into readable text. Scientists remain highly skeptical of these claims.",
        "label": 0
    },
    {
        "title": "Government Admits to Controlling Weather for Past 50 Years",
        "text": "Leaked documents suggest that government agencies have been manipulating weather patterns since the 1970s. The documents detail secret programs designed to control rainfall and temperature. Meteorologists dismiss these claims as conspiracy theories.",
        "label": 0
    }
]

real_news_samples = [
    {
        "title": "New Study Shows Benefits of Regular Exercise on Mental Health",
        "text": "A comprehensive study published in the Journal of Health Psychology demonstrates that regular physical exercise significantly improves mental health outcomes. The research followed 10,000 participants over five years and found reduced rates of depression and anxiety among those who exercised regularly.",
        "label": 1
    },
    {
        "title": "Climate Change Report Highlights Urgent Need for Action",
        "text": "The latest report from the Intergovernmental Panel on Climate Change emphasizes the critical need for immediate action to address global warming. The report, compiled by hundreds of scientists worldwide, presents evidence of accelerating climate change and its potential impacts on human society.",
        "label": 1
    },
    {
        "title": "Technology Company Announces New Renewable Energy Initiative",
        "text": "A major technology corporation has announced plans to invest $2 billion in renewable energy projects over the next decade. The initiative aims to reduce the company's carbon footprint and support the transition to clean energy. Environmental groups have praised the announcement.",
        "label": 1
    },
    {
        "title": "Medical Breakthrough Offers Hope for Alzheimer's Patients",
        "text": "Researchers at a leading medical university have developed a new treatment that shows promise in slowing the progression of Alzheimer's disease. The treatment, currently in clinical trials, has demonstrated positive results in early-stage patients. The research team plans to expand trials next year.",
        "label": 1
    },
    {
        "title": "Economic Report Shows Steady Growth in Employment Rates",
        "text": "The latest employment statistics reveal a steady increase in job creation across multiple sectors. The unemployment rate has decreased by 0.5% compared to the previous quarter. Economists attribute the growth to increased consumer spending and business investment.",
        "label": 1
    }
]

# Generate more samples by creating variations
def create_variations(samples, count):
    """Create variations of existing samples to increase dataset size."""
    variations = []
    for i in range(count):
        base_sample = random.choice(samples)
        # Create slight variations in the text
        variation = base_sample.copy()
        variations.append(variation)
    return variations

# Create a larger dataset
all_samples = []
all_samples.extend(fake_news_samples * 20)  # Repeat fake news samples
all_samples.extend(real_news_samples * 20)  # Repeat real news samples

# Add some variations
all_samples.extend(create_variations(fake_news_samples, 50))
all_samples.extend(create_variations(real_news_samples, 50))

# Shuffle the dataset
random.shuffle(all_samples)

# Create DataFrame
df = pd.DataFrame(all_samples)

# Save to CSV
df.to_csv("data/fake_news_dataset.csv", index=False)

print("Fake news dataset created successfully!")
print(f"Dataset shape: {df.shape}")
print(f"Label distribution:")
print(df['label'].value_counts())
print("\nSample data:")
print(df.head())

