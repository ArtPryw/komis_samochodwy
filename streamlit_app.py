import streamlit as st
from osobowe import *
from main import *

komis = Komis()
lista_osobowych = []
lista_ciezarowych = []
lista_motocyki =[]

st.title("KOMIS")
container1 = st.container()
container2 = st.container()
container3 = st.container()

with container1:
    if st.checkbox('Chce stworzyć nowy samochód'):
        cena = st.number_input('Wpisz cenę')
        max_paliwo = st.number_input('Wpisz pojemność baku')
        typ = st.radio("Wybierz typ: ",['osobowe', 'ciężarowe'])
        if typ == 'ciężarowe':
            ladownosc = st.number_input("Podaj ładowność w kg.")
        if st.checkbox('UTWÓRZ SAMOCHÓD:'):
            if typ == 'osobowe':
                a = Osobowy(cena, max_paliwo)
                lista_osobowych.append(a)
                st.write("Stworzono pomyślnie pojazd osobowy")
            if typ == 'ciężarowe':
                a = Osobowy(cena, max_paliwo, ladownosc)
                lista_ciezarowych.append(a)
                st.write("Stworzono pomyślnie pojazd ciężarowy")

with container2:
    if st.checkbox('Chce stworzyć nowy motocykl'):
        cena = st.number_input('Wpisz cenę motocykla')
        silnik_typ = st.number_input('Wpisz typ silnika')
        liczba_miejsc = st.number_input("Podaj liczbę miejsc")
        if st.checkbox("UTWÓRZ MOTOCYKL:"):
            a = Motocykl(cena,silnik_typ,liczba_miejsc)
            lista_motocyki.append(a)

column1, column2, column3 = st.columns(3)
with column1:
    st.title("Dostępne samochody osobowe do zakupu")
    for i,j in enumerate(lista_osobowych):
        st.write(f"{i}: {j.opis()}")
with column2:
    st.title("Dostępne samochody ciężarowe do zakupu")
    for i,j in enumerate(lista_ciezarowych):
        st.write(f"{i}: {j.opis()}")
with column3:
    st.title("Dostępne motocykle do zakupu")
    for i,j in enumerate(lista_motocyki):
        st.write(f"{i}: {j.opis()}")
