import services.datasql as db
import streamlit as st

def checklogin(username, password):
    count = db.cursor.execute("select Nome from usuarios where Nome = " + username)
    use = count.fetchone()
    if user:
        return True, user[0]
    else:
        return False, None
    
@st.cache_data()
def loadall():
    count = db.cursor.execute('select nome, email, password from usuarios')
    data = count.fethall()
    datanames= [nome[0].strip() for nome in data]
    dataemail= [email[1].strip() for email in data]
    datapassword= [password[2].strip() for password in data]
    if datanames:
        return datanames, dataemail, datapassword
    else: 
        return None
