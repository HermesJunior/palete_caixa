import streamlit as st
from banco_dados.db import (criar_usuario, listar_tipos_status, listar_tipos_usuario)

#
def pagina_criar():
    st.header(":heavy_plus_sign: Criar Usuário")

    opcoes_tipos_usuario = listar_tipos_usuario()

    with st.form("form_criar"):
        col1, col2 = st.columns(2)
        cnpj = col1.text_input("CNPJ (14 dígitos, sem pontuação - apenas números)", 
                               placeholder="12345678901234", max_chars=14)  
        razao_social = col2.text_input("Razão Social", max_chars=100)
        nome_fantasia = col1.text_input("Nome Fantasia", max_chars=100)
        nome_contato = col2.text_input("Nome do Contato", max_chars=100)
        telefone = col1.text_input("Telefone (apenas números)", autocomplete="tel", placeholder="11999999999", max_chars=11)  #type="phone"
        email = col2.text_input("E-mail", max_chars=100)

        st.divider()
        
        col1, col2 = st.columns(2)
        nome_usuario = col1.text_input("Nome de Usuário", max_chars=50)
        tipo = col2.selectbox("Tipo de Usuário", opcoes_tipos_usuario)
        senha = col1.text_input("Senha", type="password", placeholder="Mínimo 6 caracteres", max_chars=50)
        confirmar = col2.text_input("Confirmar Senha", type="password", placeholder="Confirme sua senha", max_chars=50)

        criar = st.form_submit_button("Criar Usuário")

    if criar:
        erros = []
        if not cnpj or len(cnpj) != 14 or not cnpj.isdigit():
            erros.append("CNPJ inválido. Deve conter 14 dígitos numéricos.")

        if not razao_social:
            erros.append("Razão Social é obrigatória.")

        if not nome_usuario:
            erros.append("Nome de Usuário é obrigatório.")

        if not senha:
            erros.append("Senha é obrigatória.")
        elif len(senha) < 6:
            erros.append("Senha deve ter pelo menos 6 caracteres.")
        elif senha != confirmar:
            erros.append("As senhas não coincidem.")

        if erros:
            for e in erros:
                st.warning(f":warning: {e}")
            return  # Sai da função se houver erros

        dados = {
            "cnpj": cnpj,
            "razao_social": razao_social,
            "nome_fantasia": nome_fantasia,
            "nome_contato": nome_contato,
            "telefone_contato": telefone,
            "nome_usuario": nome_usuario,
            "status": "ativo",
            "tipo": tipo,
        }
        erro = criar_usuario(dados, senha)
        if erro:
            st.error(erro)
        else:
            st.success(f"Usuário **{nome_usuario}** criado com sucesso!")
    
        """ #outra opção:
        if not all([cnpj, razao_social, nome_fantasia, nome_contato, telefone, email, nome_usuario, tipo, senha, confirmar]):
            st.warning("Preencha todos os campos obrigatórios.")
        elif senha != confirmar:
            st.warning("As senhas não coincidem.")
        else:
            sucesso = criar_usuario(cnpj, razao_social, nome_fantasia, nome_contato, telefone, email, nome_usuario, tipo, senha)
            if sucesso:
                st.success("Usuário criado com sucesso!")
            else:
                st.error("Erro ao criar usuário. Verifique se o CNPJ ou Nome de Usuário já existe.")
        """
        
        
        #st.divider()
