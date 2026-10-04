import streamlit as st
from banco_dados.db import alterar_senha

def pagina_alterar_senha():
    st.header("🔑 Alterar Senha")

    usuario = st.session_state.usuario  # Obtém o usuário logado do estado da sessão
    st.caption(f"Alterando senha de: **{usuario['razao_social']}** " \
               f"(´{usuario['nome_usuario']}´**)")

    with st.form("form_mudar_senha"):
        nova_senha = st.text_input("Nova Senha", type="password")
        confirmar = st.text_input("Confirmar Senha", type="password")
        salvar = st.form_submit_button("Salvar")

    if salvar:
        if len(nova_senha) < 6:
            st.error("A senha deve ter pelo menos 6 caracteres.")
        elif nova_senha != confirmar:
            st.error("As senhas não coincidem.")
        else:
            alterar_senha(usuario_id=usuario["id"],
                          nova_senha=nova_senha)
            st.success(":white_check_mark: Senha alterada com sucesso!")

            st.session_state.usuario = None  # Limpa o estado da sessão para forçar o login novamente
            st.rerun()


