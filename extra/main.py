import streamlit as st
col1, col2, col3 = st.columns(3)
col2.title(":blue[Re]Life")
col_1, col_2, col_3 = st.columns([1,6,1])
col_2.subheader("Ваш новый взгляд на моду и комфорт ")
co, column, c = st.columns([1,1,1])

col, coll, colll = st.columns(3)
coll.image("https://github.com/zarina-0-0/relife/tree/master/materials/relife/materials/mir_white-Photoroom.png")

with st.container(height=480):
    st.subheader(":blue[**Re**]**Life** – это не просто зеркало, это ваш личный помощник в мире моды и технологий")
    st.markdown(
        "Наша инновационная компания объединяет передовые технологии и заботу о вашем удобстве. Мы создали приложение для умных зеркал, позволяющее примерять одежду виртуально, не выходя из дома. Наше решение идеально подходит для пожилых людей, ценящих комфорт, стиль и независимость")
    st.markdown(":blue[**Виртуальная примерка:**] Забудьте о длительных поездках в магазины. Вы можете увидеть, как будет смотреться любая вещь из ассортимента наших партнеров – от брендовых магазинов до эксклюзивного секонд-хенда.")
    st.markdown(":blue[**Широкий выбор:**] ReLife сотрудничает с ведущими магазинами одежды и секонд-хендами, предоставляя доступ к уникальному ассортименту и трендовым коллекциям.")
    st.markdown(":blue[**Универсальность:**] Наше приложение поддерживают платформы Android, Apple, и другие основные опрерационные системы умных зеркал, гарантируя удобство и простоту использования.")
    st.markdown(":blue[**Уход за природой:**] Поддерживая переработку и повторное использование одежды, мы создаем экологически ответственный выбор для модного образа жизни.")

_1,_2,_3 = st.columns([1.85,2,0.9])
_3.link_button("contact us", "https://mail.google.com/mail/u/0/?pli=1#inbox",icon=":material/mail:")
_2.link_button("explore mirrors", "https://ultratrade.ru/products/ymnoe-zerkalo-s-sensornum-ekranom-yousmart-rectangular-smart-touch-screen-mirror-600x1600mm-3100-60160-u-/?srsltid=AfmBOoraDUNNU7Bi0vAQdYxh5EB4CjhYR8DXO6Kqng0kXI4vLR6h4tgS",icon=":material/shopping_cart:")
_1.link_button("try", "",icon=":material/loyalty:")