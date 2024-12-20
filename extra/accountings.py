import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

f, sec, t = st.columns([1,5,1], vertical_alignment="center")
sec.title("Анализ затрат")

# Данные для таблиц
data = {
    "Категория затрат": ["Зарплата", "Аренда помещений", "Закупка зеркал", "Закупка одежды"],
    "Затраты за месяц (руб.)": [860000, 100000, 700000, 500000]
}
people = {
    "Должность": ["Директор", "Разработчик", "Аналитик", "Маркетолог", "SMM"],
    "Кол-во": [1, 2, 1, 2, 1],
    "Заработная плата (руб.)": [180000, 120000, 150000, 100000, 90000]
}

econ = {
    "Категория": ["Зарплата", "Аренда", "Зеркала", "Одежда"],
    "Затраты, тыс. руб": [860, 100, 700, 500],
    "Размер сокращения, %": [10, 20, 34, 24],
    "Экономия, тыс. руб": [86, 20, 120, 100]
}

once = {
    "Категория": ["Госпошлина за регистрацию ООО", "Приобретение и установка онлайн кассы", "Разработка AR приложения", "Закупка оборудования(камеры, датчики)", "Регистрация товарного знака"],
    "Затраты, тыс. руб.": [4, '20-40', '500-2000', 500, 50]
}

# Создание DataFrame
df = pd.DataFrame(data)
pdf = pd.DataFrame(people)
edf = pd.DataFrame(econ)
dfo = pd.DataFrame(once)


total_cost_data = df["Затраты за месяц (руб.)"].sum()
df["% в общем объеме"] = (df["Затраты за месяц (руб.)"] / total_cost_data * 100).round(2)


pdf["ИТОГО (руб.)"] = pdf["Кол-во"] * pdf["Заработная плата (руб.)"]
total_cost_people = pdf["ИТОГО (руб.)"].sum()
pdf["% в общем объеме"] = (pdf["ИТОГО (руб.)"] / total_cost_people * 100).round(2)


fig1, ax1 = plt.subplots()
ax1.pie(df["Затраты за месяц (руб.)"], labels=df["Категория затрат"], autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.set_title("Распределение затрат")


fig2, ax2 = plt.subplots()
ax2.pie(pdf["ИТОГО (руб.)"], labels=pdf["Должность"], autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.set_title("Распределение заработной платы")


fig3, ax3 = plt.subplots()
ax3.pie(edf['Размер сокращения, %'], labels=edf["Категория"], autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
ax3.set_title("Сокращение затрат")


st.write("### Затраты и зарплаты компании")
col1, col2, col3 = st.columns([1, 7, 1])
col2.dataframe(df)
st.markdown(":blue[**Общая сумма затрат: 2 160 000 руб.**]")
st.pyplot(fig1)
col_1, col_2, col_3 = st.columns([1, 15, 1])
col_2.dataframe(pdf)
st.markdown(":blue[**Общая сумма затрат: 640 000 руб.**]")
st.pyplot(fig2)

_1, _2, _3 = st.columns([1, 15, 1])
_2.dataframe(edf)
st.markdown(":blue[**Общая сумма экономии: 326 000 руб.**]")
st.markdown("Круговая диаграмма показывает процентное отношение экономии по категории на общую сумму экономии.")
st.pyplot(fig3)
st.subheader("Обоснование сокращений")
st.markdown(":blue[**Зарплата:**] Уменьшение фонда оплаты труда на 10% минимально влияет на мотивацию, а перераспределение задач позволит сохранить производительность")
st.markdown(":blue[**Аренда:**] Рынок коммерческой недвижимости в большинстве случаев позволяет пересмотреть ставку аренды, особенно при заключении долгосрочного договора")
st.markdown(":blue[**Закупка зеркал:**] Анализ рынка поставщиков зеркал может выявить более экономичные варианты. Сокращение объема закупок позволит временно перераспределить ресурсы.")
st.markdown(":blue[**Закупка одежды:**] Заказ у производителей напрямую исключает наценки посредников. Пересмотр ассортимента на менее дорогие бренды снижает затраты без потери качества одежды.")

__1, __2, __3 = st.columns([1, 15, 1])
__2.subheader("Единоразовые затраты")
__2.dataframe(dfo)
st.subheader("Цены на которые мы ориентировались:")
st.markdown("[Касса](https://online-kassa.ru/kupit/cat/kassy/)")
st.markdown("[Аренда помещений](https://spb.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&maxprice=105000&offer_type=offices&office_type%5B0%5D=1&region=2)")
st.markdown("[Зеркала](https://ultratrade.ru/products/ymnoe-zerkalo-s-sensornum-ekranom-yousmart-rectangular-smart-touch-screen-mirror-600x1600mm-3100-60160-u-/?srsltid=AfmBOoraDUNNU7Bi0vAQdYxh5EB4CjhYR8DXO6Kqng0kXI4vLR6h4tgS)")

st.subheader("Зарплаты на которые мы ориентировались:")
st.markdown("[Директор](https://spb.hh.ru/vacancies/direktor)")
st.markdown("[Разработчик](https://spb.hh.ru/vacancies/razrabotchik)")
st.markdown("[Аналитик](https://spb.hh.ru/vacancies/analitik)")
st.markdown("[Маркетолог](https://spb.hh.ru/vacancies/marketolog)")
st.markdown("[SMM](https://spb.hh.ru/search/vacancy?text=smm&salary=&ored_clusters=true&area=2&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line )")