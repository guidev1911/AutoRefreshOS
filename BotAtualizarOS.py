from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import ctypes
import winsound
import keyring
from urllib.parse import quote

SERVICO = "BOT_DETRAN"

USUARIO_INTR = keyring.get_password(SERVICO, "usuario_intr")
SENHA_INTR = keyring.get_password(SERVICO, "senha_intr")

USUARIO_PORTAL = keyring.get_password(SERVICO, "usuario_portal")
SENHA_PORTAL = keyring.get_password(SERVICO, "senha_portal")

if not USUARIO_INTR or not SENHA_INTR or not USUARIO_PORTAL or not SENHA_PORTAL:

    ctypes.windll.user32.MessageBoxW(
        0,
        "Credenciais não configuradas.\nExecute o Configurar.exe primeiro.",
        "Erro",
        1
    )

    exit()

options = Options()
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service()
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()

wait = WebDriverWait(driver, 15)

senha_url = quote(SENHA_INTR)
usuario_url = quote(USUARIO_INTR)

url_intranet = f"http://{usuario_url}:{senha_url}@intranet.detran.gov-se/novo_inicio.asp"
driver.get(url_intranet)

token_element = wait.until(
    EC.presence_of_element_located((By.ID, "divNumeroToken"))
)

wait.until(lambda d: token_element.text.strip() != "")
token = token_element.text.strip()

driver.get("http://portal.detran.gov-se/default.asp?pg=login&redir=ordem_servico_fila")

wait.until(EC.presence_of_element_located((By.ID, "nscUser")))

driver.find_element(By.ID, "nscUser").send_keys(USUARIO_PORTAL)
driver.find_element(By.ID, "nscPwd").send_keys(SENHA_PORTAL)
driver.find_element(By.ID, "nrToken").send_keys(token)

botao_confirmar = wait.until(
    EC.element_to_be_clickable((By.ID, "btSubmeter"))
)

botao_confirmar.click()

wait.until(lambda d: d.current_url != "http://portal.detran.gov-se/default.asp?pg=login&redir=ordem_servico_fila")

wait.until(
    EC.presence_of_element_located((By.ID, "fsOrdemServico"))
)

select_element = wait.until(
    EC.element_to_be_clickable((By.ID, "codAtendimento"))
)

select = Select(select_element)

select.select_by_visible_text("Suporte de Equipamentos")

botao_confirmar = wait.until(
    EC.element_to_be_clickable((By.ID, "btSubmeter"))
)

driver.execute_script("arguments[0].click();", botao_confirmar)

os_anteriores = set()

try:
    while True:

        if not driver.service.process:
            break

        try:

            botao_fila = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "btFila"))
            )

            driver.execute_script("arguments[0].click();", botao_fila)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#tblForm > tbody > tr"))
            )

            linhas = driver.find_elements(By.CSS_SELECTOR, "#tblForm > tbody > tr")

            os_atual = set()

            for linha in linhas:
                try:

                    colunas = linha.find_elements(By.TAG_NAME, "td")

                    if len(colunas) == 7:

                        numero = colunas[0].text.strip()

                        if numero.isdigit():
                            os_atual.add(numero)

                except:
                    continue

            novas = os_atual - os_anteriores

            if novas:

                lista_os = "\n".join(sorted(novas))

                print(f"🚨 NOVAS OS DETECTADAS:\n{lista_os}")

                winsound.MessageBeep()

                ctypes.windll.user32.MessageBoxW(
                    0,
                    f"Novas Ordens de Serviço detectadas:\n\n{lista_os}",
                    "ALERTA DETRAN",
                    1
                )

            os_anteriores = os_atual

        except:
            break

        time.sleep(60)

finally:
    driver.quit()