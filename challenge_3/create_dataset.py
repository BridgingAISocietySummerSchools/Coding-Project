import pandas as pd
import random

# Sample spam comments (typical patterns found in social media spam)
spam_comments = [
    "Check out my profile for amazing deals!!!",
    "Click here to win $1000 now! Link in bio",
    "Follow me for follow back! F4F",
    "Buy followers cheap! DM me now",
    "Amazing weight loss pills! Click link",
    "Free iPhone giveaway! Comment to win",
    "Make money from home! Easy work",
    "Hot singles in your area! Click now",
    "Congratulations! You've won a prize",
    "Limited time offer! Act now or miss out",
    "Get rich quick scheme! 100% guaranteed",
    "Lose 20 pounds in 1 week! Miracle pill",
    "Work from home! Earn $5000/month",
    "Free gift cards! No purchase necessary",
    "Amazing crypto investment opportunity",
    "Follow for follow! Like for like!",
    "Check out my OnlyFans! Link in bio",
    "Cheap designer bags! Best prices",
    "Bitcoin investment! Double your money",
    "Free vacation! You've been selected",
    "Diet pills that actually work! Order now",
    "Get verified on Instagram! DM me",
    "Followers for sale! Cheap prices",
    "Win a new car! Enter now",
    "Make $1000 daily! No experience needed"
]

# Sample legitimate comments (normal social media interactions)
legitimate_comments = [
    "Great photo! Love the lighting",
    "This looks delicious! Recipe please?",
    "Beautiful sunset! Where was this taken?",
    "Congratulations on your achievement!",
    "Thanks for sharing this inspiring story",
    "Your dog is so cute! What breed?",
    "Love your outfit! Where did you get it?",
    "This made my day! Thank you",
    "Amazing artwork! Very talented",
    "Hope you had a great vacation",
    "Happy birthday! Have a wonderful day",
    "This is so funny! Made me laugh",
    "Great advice! Thanks for sharing",
    "Beautiful family photo!",
    "Love this song! Who's the artist?",
    "Your garden looks amazing!",
    "Thanks for the recommendation",
    "This is exactly what I needed to hear",
    "Stunning photography! Well done",
    "Hope you feel better soon",
    "Congratulations on your new job!",
    "This recipe looks amazing",
    "Love your new haircut!",
    "Great workout tips! Thanks",
    "This place looks incredible"
]

# Generate more variations
def create_spam_variations():
    """Create variations of spam comments with common spam patterns."""
    variations = []
    
    # Add emoji spam
    emoji_spam = [
        "🔥🔥🔥 AMAZING DEAL 🔥🔥🔥",
        "💰💰 MAKE MONEY FAST 💰💰",
        "🎁 FREE GIFT 🎁 CLICK NOW",
        "⚡ URGENT ⚡ LIMITED TIME",
        "🚨 ALERT 🚨 SPECIAL OFFER"
    ]
    variations.extend(emoji_spam)
    
    # Add repetitive character spam
    repetitive_spam = [
        "AMAZING DEAL!!!!!!!!",
        "CHECK THIS OUT NOW!!!",
        "BEST OFFER EVER!!!!",
        "DONT MISS OUT!!!!!",
        "CLICK HERE NOW!!!!!"
    ]
    variations.extend(repetitive_spam)
    
    # Add promotional spam
    promo_spam = [
        "Use code SAVE50 for discount",
        "Limited time 90% off everything",
        "Flash sale ends tonight!",
        "Exclusive offer just for you",
        "Last chance to save big"
    ]
    variations.extend(promo_spam)
    
    return variations

def create_legitimate_variations():
    """Create variations of legitimate comments."""
    variations = []
    
    # Add supportive comments
    supportive = [
        "You're doing great! Keep it up",
        "This is so inspiring! Thank you",
        "Love seeing your progress",
        "You always brighten my day",
        "Such a positive message"
    ]
    variations.extend(supportive)
    
    # Add question comments
    questions = [
        "How did you learn to do this?",
        "What camera did you use?",
        "Can you share more details?",
        "Where can I find this?",
        "What's your secret?"
    ]
    variations.extend(questions)
    
    # Add casual comments
    casual = [
        "Nice!",
        "Cool pic",
        "Love it",
        "Awesome",
        "So good"
    ]
    variations.extend(casual)
    
    return variations

# Create the dataset
all_comments = []

# Add original spam comments (multiply to create more samples)
for comment in spam_comments * 8:
    all_comments.append({"comment": comment, "label": 1})  # 1 = spam

# Add spam variations
spam_variations = create_spam_variations()
for comment in spam_variations * 6:
    all_comments.append({"comment": comment, "label": 1})

# Add original legitimate comments (multiply to create more samples)
for comment in legitimate_comments * 8:
    all_comments.append({"comment": comment, "label": 0})  # 0 = legitimate

# Add legitimate variations
legit_variations = create_legitimate_variations()
for comment in legit_variations * 6:
    all_comments.append({"comment": comment, "label": 0})

# Shuffle the dataset
random.shuffle(all_comments)

# Create DataFrame
df = pd.DataFrame(all_comments)

# Save to CSV
df.to_csv("data/spam_detection_dataset.csv", index=False)

print("Spam detection dataset created successfully!")
print(f"Dataset shape: {df.shape}")
print(f"Label distribution:")
print(df['label'].value_counts())
print(f"Spam percentage: {(df['label'].sum() / len(df)) * 100:.1f}%")
print("\nSample data:")
print(df.head(10))

