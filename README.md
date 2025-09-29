# 📊 Social Media Trend Detection

This project analyzes **viral social media datasets** to identify which hashtags are gaining traction. Using **Python (Pandas)**, it maps engagement levels into numeric values and classifies hashtags into **Low, Medium, or High trending** categories.

---

## 🚀 Features

* Works with multiple datasets (`Viral`, `Engagement`, `Cleaned`)
* Maps `Engagement_Level` → numeric values (`Low=0, Medium=1, High=2`)
* Normalizes engagement categories into lowercase (`low, medium, high`)
* Extracts only **Medium** and **High trending hashtags**
* Prints results with hashtag, engagement level, and category

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries:** Pandas

---

## 📂 Project Structure

```
social-media-trend-detection/
│── .idea/                                 # IDE config files (can be ignored)  
│── Cleaned_Viral_Social_Media_Trends.csv  # Pre-cleaned dataset  
│── Social Media Engagement Dataset.csv    # Raw engagement dataset  
│── Viral_Social_Media_Trends.csv          # Raw viral dataset  
│── social_media_trending_content.py       # Main Python script  
│── README.md                              # Project documentation  
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Tharun-dot/social-media-trend-detection.git
   ```
2. Navigate into the project:

   ```bash
   cd social-media-trend-detection
   ```
3. Install dependencies:

   ```bash
   pip install pandas
   ```
4. Run the script:

   ```bash
   python social_media_trending_content.py
   ```

---

## 📊 Example Output

**Trending Hashtags:**

```
#SummerVibes
#FoodieLife
#TechTrends
```

**Detailed View:**

```
       Hashtag    Engagement_Level   is_trending
0   #SummerVibes         High           high
1   #FoodieLife         Medium         medium
2   #TechTrends        High           high
```

---

## 🎯 Future Enhancements

* Add **data visualization** for engagement levels
* Support **real-time trend detection** from APIs
* Build a **Streamlit dashboard** to explore trends interactively

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

---

