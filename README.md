# 🎬 Netflix Show Analyzer

A Data Science project to explore and visualize trends in Netflix's global content catalog using **Python**, **Pandas**, and **Seaborn**.

![Top Genres on Netflix](output/top_netflix_genres.png)

---

## 📌 Project Objectives

- Understand Netflix’s content distribution by type (Movie vs TV Show)
- Analyze content addition trends over time
- Identify top content-producing countries
- Discover the most common genres on Netflix

---

## 📂 Dataset

- **Name**: [netflix_titles.csv](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Size**: ~8,800 titles
- **Columns**:
  - `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`

---

## 🛠️ Technologies Used

- **Python 3.12**
- **Pandas** for data wrangling
- **Matplotlib & Seaborn** for visualization
- **VS Code** as development environment

---

## 📈 Key Visualizations

### 1️⃣ Content Type Distribution
![Content Type](output/distribution of content type on.png)

---

### 2️⃣ Netflix Content Added Over the Years
![Content Added](output/Netflix Content Added Over the Years.png)

---

### 3️⃣ Top Countries with Most Titles
![Top Countries](output/top_countries_netflix.png)

---

### 4️⃣ Top 10 Most Common Genres
![Genres](output/top_netflix_genres.png)

---

## 🧠 Learnings

- Preprocessing datetime features and handling missing values
- Extracting insights from multivalued columns like `listed_in`
- Saving visualizations programmatically
- Writing clean, modular code using `# %%` blocks in VS Code

---

## 🚀 How to Run

1. Clone the repo or download the files  
2. Make sure Python 3 is installed  
3. Run `MAIN.py` in VS Code or from terminal:
   ```bash
   python MAIN.py
