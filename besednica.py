import random
import streamlit as st

st.set_page_config(
page_title="Besednica",
page_icon="🤔",
layout="wide"
)

st.write("Ugibaj besedo!")
st.write("pozor: samo male črke...")
def vrni_slovar(dolzina):
  slovar = open("besede.txt")
  besede = slovar.readlines()
  slovar.close()
  seznam = [i[:-1] for i in besede if len(i[:-1]) == dolzina]
  return seznam

def igraj(n,m):
  seznam_besed = vrni_slovar(n)
  win=False
  beseda = seznam_besed[m]
  # st.write(beseda)
  for i in range(1,11):
    oblika = False
    while not oblika:
      # ugib = input(f"{i}/10. Ugibaj: ")
      ugib = st.text_input(f"{i}/10. Ugibaj: ","")
      if ugib!="":
          if len(ugib) != n:
            st.write(f"Beseda ni prave dolžine ({n}). Poskusi ponovno.")
          elif ugib in seznam_besed:
            oblika = True
          else:
            st.write(f"Besede \"{ugib}\" ni v slovarju. Poskusi ponovno.")
    
    prikaz = ""
    for poz, letter in enumerate(ugib):
      if ugib[poz] == beseda[poz]:
        prikaz += "💚"
      elif ugib[poz] in beseda:
        prikaz += "💛"
      else:
        prikaz += "🖤"
    if "💛" not in prikaz and "🖤" not in prikaz:
      st.write("Bravo!")
      win=True
    else:
      st.write(prikaz)
  if win==False:
      st.write(f"Pravilen odgovor je bil: \"{beseda}\".")

agree = st.checkbox('Poskusimo...')
številka=int(st.number_input("Uganka številka koliko? Med 0 in 12862",value=5000))

if agree:
    igraj(5,številka)
# igraj(5)


