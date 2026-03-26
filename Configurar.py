import tkinter as tk
import keyring

# serviço usado para armazenar no Windows Credential Manager
SERVICO = "BOT_DETRAN"


def salvar():

    keyring.set_password(SERVICO, "usuario_intr", entry_intr_user.get())
    keyring.set_password(SERVICO, "senha_intr", entry_intr_pass.get())

    keyring.set_password(SERVICO, "usuario_portal", entry_portal_user.get())
    keyring.set_password(SERVICO, "senha_portal", entry_portal_pass.get())

    status.config(text="✔ Credenciais salvas com sucesso!", fg="green")


# =========================
# JANELA
# =========================

janela = tk.Tk()
janela.title("Configurar Credenciais - Bot DETRAN")
janela.geometry("420x280")
janela.resizable(False, False)

frame = tk.Frame(janela, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# =========================
# CAMPOS
# =========================

tk.Label(frame, text="Usuário Intranet").grid(row=0, column=0, sticky="w", pady=5)
entry_intr_user = tk.Entry(frame, width=35)
entry_intr_user.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Senha Intranet").grid(row=1, column=0, sticky="w", pady=5)
entry_intr_pass = tk.Entry(frame, show="*", width=35)
entry_intr_pass.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Usuário Portal").grid(row=2, column=0, sticky="w", pady=5)
entry_portal_user = tk.Entry(frame, width=35)
entry_portal_user.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Senha Portal").grid(row=3, column=0, sticky="w", pady=5)
entry_portal_pass = tk.Entry(frame, show="*", width=35)
entry_portal_pass.grid(row=3, column=1, pady=5)

# =========================
# CARREGAR CREDENCIAIS SALVAS
# =========================

usuario_intr = keyring.get_password(SERVICO, "usuario_intr")
senha_intr = keyring.get_password(SERVICO, "senha_intr")

usuario_portal = keyring.get_password(SERVICO, "usuario_portal")
senha_portal = keyring.get_password(SERVICO, "senha_portal")

if usuario_intr:
    entry_intr_user.insert(0, usuario_intr)

if senha_intr:
    entry_intr_pass.insert(0, senha_intr)

if usuario_portal:
    entry_portal_user.insert(0, usuario_portal)

if senha_portal:
    entry_portal_pass.insert(0, senha_portal)

# =========================
# BOTÃO
# =========================

btn_salvar = tk.Button(frame, text="Salvar Credenciais", width=20, command=salvar)
btn_salvar.grid(row=4, column=0, columnspan=2, pady=20)

status = tk.Label(frame, text="")
status.grid(row=5, column=0, columnspan=2)

janela.mainloop()