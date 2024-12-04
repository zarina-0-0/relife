import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

f, sec, t = st.columns([1,5,1], vertical_alignment="center")
sec.title("Анализ затрат")

# Данные для таблиц
data = {
    "Категория затрат": ["Зарплата", "Аренда помещений", "Закупка зеркал", "Закупка одежды"],
    "Затраты за месяц (руб.)": [750000, 100000, 700000, 500000]
}
people = {
    "Должность": ["Директор", "Разработчик", "Аналитик", "Маркетолог", "SMM"],
    "Кол-во": [1, 2, 1, 2, 1],
    "Заработная плата (руб.)": [180000, 120000, 150000, 100000, 90000]
}

# Создание DataFrame
df = pd.DataFrame(data)
pdf = pd.DataFrame(people)

# Расчет доли каждой категории в общем объеме затрат
total_cost_data = df["Затраты за месяц (руб.)"].sum()
df["% в общем объеме"] = (df["Затраты за месяц (руб.)"] / total_cost_data * 100).round(2)

# Расчет итогов в таблице people
pdf["ИТОГО (руб.)"] = pdf["Кол-во"] * pdf["Заработная плата (руб.)"]
total_cost_people = pdf["ИТОГО (руб.)"].sum()
pdf["% в общем объеме"] = (pdf["ИТОГО (руб.)"] / total_cost_people * 100).round(2)

# Построение круговой диаграммы для затрат
fig1, ax1 = plt.subplots()
ax1.pie(df["Затраты за месяц (руб.)"], labels=df["Категория затрат"], autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Круглая диаграмма
ax1.set_title("Распределение затрат")

# Построение круговой диаграммы для зарплат
fig2, ax2 = plt.subplots()
ax2.pie(pdf["ИТОГО (руб.)"], labels=pdf["Должность"], autopct='%1.1f%%', startangle=90)
ax2.axis('equal')  # Круглая диаграмма
ax2.set_title("Распределение заработной платы")

# Отображение диаграмм слева и таблиц справа
st.write("### Затраты и зарплаты компании")
col1, col2, col3 = st.columns([1, 7, 1])  # Задаем соотношение колонок: диаграммы шире, таблицы уже
col2.dataframe(df)
st.pyplot(fig1)
col_1, col_2, col_3 = st.columns([1, 15, 1])
col_2.dataframe(pdf)
st.pyplot(fig2)

