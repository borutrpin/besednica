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



agree = st.checkbox('Poskusimo...')
številka=int(st.number_input("Uganka številka koliko? Med 0 in 12862",value=110))

if agree:
    # igraj(5,številka)
    n=5
    m=številka
    seznam_besed = vrni_slovar(n)
    win=False
    beseda = seznam_besed[m]
    oblika= False
    nadaljuj=0
    while oblika==False:
        ugib1 = st.text_input("1/6. Ugibaj: ","",key="1")
        if ugib1!="":
            if len(ugib1) != n:
                st.write(f"Beseda ni prave dolžine ({n}). Poskusi ponovno.")
            elif ugib1 in seznam_besed:
                oblika = True
            else:
                st.write(f"Besede \"{ugib1}\" ni v slovarju. Poskusi ponovno.")
    ugib=ugib1
    prikaz=""
    for poz, letter in enumerate(ugib):
        if ugib[poz] == beseda[poz]:
            prikaz += "💚"
        elif ugib[poz] in beseda:    
            prikaz += "💛"
        else:
            prikaz += "🖤"
    if "💛" not in prikaz and "🖤" not in prikaz:
        st.write("Bravo!")
        st.write(beseda)
        st.write("💚💚💚💚💚")
        win=True
        
    else:
        st.write(ugib)
        st.write(prikaz)
        nadaljuj=1
    if nadaljuj==1:
        oblika= False
        nadaljuj=0
        while oblika==False:
            ugib2 = st.text_input("2/6. Ugibaj: ","",key="2")
            if ugib2!="":
                if len(ugib2) != n:
                    st.write(f"Beseda ni prave dolžine ({n}). Poskusi ponovno.")
                elif ugib2 in seznam_besed:
                    oblika = True
                else:
                    st.write(f"Besede \"{ugib2}\" ni v slovarju. Poskusi ponovno.")
        ugib=ugib2
        prikaz=""
        for poz, letter in enumerate(ugib):
            if ugib[poz] == beseda[poz]:
                prikaz += "💚"
            elif ugib[poz] in beseda:    
                prikaz += "💛"
            else:
                prikaz += "🖤"
        if "💛" not in prikaz and "🖤" not in prikaz:
            st.write("Bravo!")
            st.write(beseda)
            st.write("💚💚💚💚💚")
            win=True
            
        else:
            st.write(ugib)
            st.write(prikaz)
            nadaljuj=1
    if nadaljuj==1:
        oblika= False
        nadaljuj=0
        while oblika==False:
            ugib3 = st.text_input("3/6. Ugibaj: ","",key="3")
            if ugib3!="":
                if len(ugib3) != n:
                    st.write(f"Beseda ni prave dolžine ({n}). Poskusi ponovno.")
                elif ugib3 in seznam_besed:
                    oblika = True
                else:
                    st.write(f"Besede \"{ugib3}\" ni v slovarju. Poskusi ponovno.")
        ugib=ugib3
        prikaz=""
        for poz, letter in enumerate(ugib):
            if ugib[poz] == beseda[poz]:
                prikaz += "💚"
            elif ugib[poz] in beseda:    
                prikaz += "💛"
            else:
                prikaz += "🖤"
        if "💛" not in prikaz and "🖤" not in prikaz:
            st.write("Bravo!")
            st.write(beseda)
            st.write("💚💚💚💚💚")
            win=True
            
        else:
            st.write(ugib)
            st.write(prikaz)
            nadaljuj=1

    if nadaljuj==1:
        oblika= False
        nadaljuj=0
        while oblika==False:
            ugib4 = st.text_input("4/6. Ugibaj: ","",key="4")
            if ugib4!="":
                if len(ugib4) != n:
                    st.write(f"Beseda ni prave dolžine ({n}). Poskusi ponovno.")
                elif ugib4 in seznam_besed:
                    oblika = True
                else:
                    st.write(f"Besede \"{ugib4}\" ni v slovarju. Poskusi ponovno.")
        ugib=ugib4
        prikaz=""
        for poz, letter in enumerate(ugib):
            if ugib[poz] == beseda[poz]:
                prikaz += "💚"
            elif ugib[poz] in beseda:    
                prikaz += "💛"
            else:
                prikaz += "🖤"
        if "💛" not in prikaz and "🖤" not in prikaz:
            st.write("Bravo!")
            st.write(beseda)
            st.write("💚💚💚💚💚")
            win=True
            
        else:
            st.write(ugib)
            st.write(prikaz)
            nadaljuj=1
    if nadaljuj==1:
        oblika= False
        nadaljuj=0
        while oblika==False:
            ugib5 = st.text_input("5/6. Ugibaj: ","",key="5")
            if ugib5!="":
                if len(ugib5) != n:
                    st.write(f"Beseda ni prave dolžine ({n}). Poskusi ponovno.")
                elif ugib5 in seznam_besed:
                    oblika = True
                else:
                    st.write(f"Besede \"{ugib5}\" ni v slovarju. Poskusi ponovno.")
        ugib=ugib5
        prikaz=""
        for poz, letter in enumerate(ugib):
            if ugib[poz] == beseda[poz]:
                prikaz += "💚"
            elif ugib[poz] in beseda:    
                prikaz += "💛"
            else:
                prikaz += "🖤"
        if "💛" not in prikaz and "🖤" not in prikaz:
            st.write("Bravo!")
            st.write(beseda)
            st.write("💚💚💚💚💚")
            win=True
            
        else:
            st.write(ugib)
            st.write(prikaz)
            nadaljuj=1
    if nadaljuj==1:
        oblika= False
        nadaljuj=0
        while oblika==False:
            ugib6 = st.text_input("6/6. Ugibaj: ","",key="6")
            if ugib6!="":
                if len(ugib6) != n:
                    st.write(f"Beseda ni prave dolžine ({n}). Poskusi ponovno.")
                elif ugib6 in seznam_besed:
                    oblika = True
                else:
                    st.write(f"Besede \"{ugib6}\" ni v slovarju. Poskusi ponovno.")
        ugib=ugib6
        prikaz=""
        for poz, letter in enumerate(ugib):
            if ugib[poz] == beseda[poz]:
                prikaz += "💚"
            elif ugib[poz] in beseda:    
                prikaz += "💛"
            else:
                prikaz += "🖤"
        if "💛" not in prikaz and "🖤" not in prikaz:
            st.write("Bravo!")
            st.write(beseda)
            st.write("💚💚💚💚💚")
            win=True
            
        else:
            st.write(ugib)
            st.write(prikaz)
            nadaljuj=1
            st.write("Prava beseda je bila \"{beseda}\".")
# igraj(5)


