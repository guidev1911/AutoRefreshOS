import customtkinter as ctk
import keyring

# =========================================================
# CONFIGURAÇÕES
# =========================================================

SERVICO = "BOT_DETRAN"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# =========================================================
# FUNÇÕES
# =========================================================

def salvar():
    keyring.set_password(SERVICO, "usuario_intr", entry_intr_user.get())
    keyring.set_password(SERVICO, "senha_intr", entry_intr_pass.get())
    keyring.set_password(SERVICO, "usuario_portal", entry_portal_user.get())
    keyring.set_password(SERVICO, "senha_portal", entry_portal_pass.get())

    status.configure(
        text="✔ Credenciais salvas com sucesso!",
        text_color="#7CFC00"
    )


def limpar():
    entry_intr_user.delete(0, "end")
    entry_intr_pass.delete(0, "end")
    entry_portal_user.delete(0, "end")
    entry_portal_pass.delete(0, "end")

    status.configure(
        text="Campos limpos.",
        text_color="#FFB703"
    )


# =========================================================
# JANELA
# =========================================================

janela = ctk.CTk()

janela.title("Configurar Credenciais - Bot DETRAN")

# Aumentamos a altura para comportar todo o conteúdo
janela.geometry("560x580")
janela.minsize(520, 560)
janela.resizable(False, False)

janela.configure(fg_color="#0f172a")


# =========================================================
# FRAME PRINCIPAL
# =========================================================

main_frame = ctk.CTkFrame(
    janela,
    corner_radius=24,
    fg_color="#111827",
    border_width=1,
    border_color="#334155"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=18,
    pady=18
)

main_frame.grid_columnconfigure(0, weight=1)


# =========================================================
# CABEÇALHO
# =========================================================

header = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

header.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=22,
    pady=(18, 6)
)


ctk.CTkLabel(
    header,
    text="Configuração do Bot DETRAN",
    font=("Segoe UI", 22, "bold"),
    text_color="#F8FAFC"
).pack(anchor="w")


ctk.CTkLabel(
    header,
    text="Guarde suas credenciais com segurança no Windows Credential Manager.",
    font=("Segoe UI", 12),
    text_color="#94A3B8"
).pack(
    anchor="w",
    pady=(3, 0)
)


# =========================================================
# CAMPOS
# =========================================================

fields_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

fields_frame.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=22,
    pady=(4, 0)
)

fields_frame.grid_columnconfigure(0, weight=1)


# ---------------------------------------------------------
# Usuário Intranet
# ---------------------------------------------------------

ctk.CTkLabel(
    fields_frame,
    text="Usuário Intranet",
    font=("Segoe UI", 13, "bold"),
    anchor="w"
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=(4, 3)
)


entry_intr_user = ctk.CTkEntry(
    fields_frame,
    height=28,
    placeholder_text="Digite o usuário da intranet"
)

entry_intr_user.grid(
    row=1,
    column=0,
    sticky="ew",
    pady=(0, 5)
)


# ---------------------------------------------------------
# Senha Intranet
# ---------------------------------------------------------

ctk.CTkLabel(
    fields_frame,
    text="Senha Intranet",
    font=("Segoe UI", 13, "bold"),
    anchor="w"
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=(4, 3)
)


entry_intr_pass = ctk.CTkEntry(
    fields_frame,
    height=28,
    show="*",
    placeholder_text="Digite a senha da intranet"
)

entry_intr_pass.grid(
    row=3,
    column=0,
    sticky="ew",
    pady=(0, 5)
)


# ---------------------------------------------------------
# Usuário Portal
# ---------------------------------------------------------

ctk.CTkLabel(
    fields_frame,
    text="Usuário Portal",
    font=("Segoe UI", 13, "bold"),
    anchor="w"
).grid(
    row=4,
    column=0,
    sticky="w",
    pady=(4, 3)
)


entry_portal_user = ctk.CTkEntry(
    fields_frame,
    height=28,
    placeholder_text="Digite o usuário do portal"
)

entry_portal_user.grid(
    row=5,
    column=0,
    sticky="ew",
    pady=(0, 5)
)


# ---------------------------------------------------------
# Senha Portal
# ---------------------------------------------------------

ctk.CTkLabel(
    fields_frame,
    text="Senha Portal",
    font=("Segoe UI", 13, "bold"),
    anchor="w"
).grid(
    row=6,
    column=0,
    sticky="w",
    pady=(4, 3)
)


entry_portal_pass = ctk.CTkEntry(
    fields_frame,
    height=28,
    show="*",
    placeholder_text="Digite a senha do portal"
)

entry_portal_pass.grid(
    row=7,
    column=0,
    sticky="ew",
    pady=(0, 4)
)


# =========================================================
# CARREGAR CREDENCIAIS SALVAS
# =========================================================

usuario_intr = keyring.get_password(
    SERVICO,
    "usuario_intr"
)

senha_intr = keyring.get_password(
    SERVICO,
    "senha_intr"
)

usuario_portal = keyring.get_password(
    SERVICO,
    "usuario_portal"
)

senha_portal = keyring.get_password(
    SERVICO,
    "senha_portal"
)


if usuario_intr:
    entry_intr_user.insert(0, usuario_intr)

if senha_intr:
    entry_intr_pass.insert(0, senha_intr)

if usuario_portal:
    entry_portal_user.insert(0, usuario_portal)

if senha_portal:
    entry_portal_pass.insert(0, senha_portal)


# =========================================================
# BOTÕES
# =========================================================

buttons_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

buttons_frame.grid(
    row=2,
    column=0,
    sticky="w",
    padx=22,
    pady=(8, 0)
)


btn_salvar = ctk.CTkButton(
    buttons_frame,
    text="Salvar Credenciais",
    width=180,
    height=40,
    corner_radius=12,
    command=salvar
)

btn_salvar.pack(
    side="left",
    padx=(0, 12)
)


btn_limpar = ctk.CTkButton(
    buttons_frame,
    text="Limpar",
    width=120,
    height=40,
    corner_radius=12,
    fg_color="#475569",
    hover_color="#334155",
    command=limpar
)

btn_limpar.pack(
    side="left"
)


# =========================================================
# STATUS
# =========================================================

status = ctk.CTkLabel(
    main_frame,
    text="",
    font=("Segoe UI", 12),
    wraplength=480,
    text_color="#E2E8F0"
)

status.grid(
    row=3,
    column=0,
    sticky="w",
    padx=22,
    pady=(8, 12)
)


# =========================================================
# INICIAR
# =========================================================

janela.mainloop()
