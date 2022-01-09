import random
import streamlit as st

st.set_page_config(
page_title="Besednica",
page_icon="🤔",
layout="wide"
)

st.write("Ugibaj besedo!")
def vrni_slovar(dolzina):
  slovar = open("besede.txt")
  besede = slovar.readlines()
  slovar.close()
  seznam = [i[:-1] for i in besede if len(i[:-1]) == dolzina]
  return seznam

def igraj(n):
  seznam_besed = vrni_slovar(n)
  win=False
  beseda = random.choice(seznam_besed)
  # print(beseda)
  for i in range(1,11):
    oblika = False
    while not oblika:
      ugib = input(f"{i}/10. Ugibaj: ")
      if len(ugib) != n:
        print(f"Beseda ni prave dolžine ({n}). Poskusi ponovno.")
      elif ugib in seznam_besed:
        oblika = True
      else:
        print(f"Besede \"{ugib}\" ni v slovarju. Poskusi ponovno.")
    prikaz = ""
    for poz, letter in enumerate(ugib):
      if ugib[poz] == beseda[poz]:
        prikaz += "💚"
      elif ugib[poz] in beseda:
        prikaz += "💛"
      else:
        prikaz += "🖤"
    if "💛" not in prikaz and "🖤" not in prikaz:
      print("Bravo!")
      win=True
    else:
      print(prikaz)
  if win==False:
      print(f"Pravilen odgovor je bil: \"{beseda}\".")
     

# n = int(input("Ka? "))
igraj(5)


