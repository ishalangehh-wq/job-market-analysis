import pandas as pd

df = pd.read_csv("job_market_dataset.csv")

print(df.head())

print(df.shape)

print(df.columns)

skills = df["skills"]

all_skills = []

for i in skills:

    skill_list = i.split(",")

    for skill in skill_list:

        all_skills.append(skill.strip())

skill_count = pd.Series(all_skills).value_counts()

print(skill_count.head())
avg_salary = df.groupby("job_title")["salary"].mean()

print(avg_salary)
location_count = df["location"].value_counts()
print(location_count)
import matplotlib.pyplot as plt
skill_count.head(5).plot(kind="bar")
plt.title("Top_skils")
plt.savefig("Top_skills.png")
avg_salary.plot(kind="bar")
plt.title("Average salary by job title")
plt.savefig("Average salary by job title.png")
location_count.plot(kind="pie")

plt.title("Jobs by Location")

plt.savefig("Jobs by Location.png")
