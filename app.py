import streamlit as st
from paginas.login import pagina_login
from paginas.listar_usuarios import pagina_listar
from paginas.criar_usuario import pagina_criar
from paginas.alterar_senha import pagina_alterar_senha
from paginas.alterar_status import pagina_alterar_status    
from paginas.deletar_usuario import pagina_deletar


#
st.set_page_config(page_title="Palete Caixa", 
                   page_icon="📦", 
                   layout="centered")

#
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None
#print(st.session_state)

# 
if st.session_state["usuario"] is None:
    pagina_login()
else:
    usuario = st.session_state.usuario
    is_admin = usuario.get("tipo") == "admin"

    with st.sidebar:
        tipo_badge = ":crow: Admin" if is_admin else \
                        ":bust_in_silhouette: Regular"
        st.markdown(f"**Olá {usuario['razao_social']}!**")
        st.caption(f"Usuário ´{usuario['nome_usuario']}´ - {tipo_badge}")

        #
        st.divider()
        opccoes_menu = (
            ["Modelo Palete Caixa", "Listar Usuários", "Criar Usuários", 
             "Alterar Status", "Alterar Senha", "Deletar Usuários"
            ]
            if is_admin else ["Modelo Palete Caixa", "Alterar Senha"]       
        )

        pagina = st.radio("Menu", opccoes_menu, index=0,
                          label_visibility="collapsed" )

        #
        st.divider()

        if st.button(":door: Sair"):
            st.session_state.usuario = None
            st.rerun()

    if pagina == "Listar Usuários":
        pagina_listar()
    elif pagina == "Criar Usuários":
        pagina_criar()
    elif pagina == "Alterar Senha":
        pagina_alterar_senha()
    elif pagina == "Alterar Status":
        pagina_alterar_status() 
    elif pagina == "Deletar Usuários":
        pagina_deletar()
        
        

    



#
 