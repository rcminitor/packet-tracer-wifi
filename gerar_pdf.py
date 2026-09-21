#!/usr/bin/env python3
"""
Gera o PDF da apostila de Wi-Fi Corporativo nas cores azul e laranja.
Utiliza o Google Chrome ou Microsoft Edge headless nativo.
"""
import subprocess
import os
import sys
from pathlib import Path

def gerar_pdf():
    diretorio = Path(__file__).parent.resolve()
    html_file = diretorio / "apostila_wifi_corporativo.html"
    pdf_file = diretorio / "apostila_wifi_corporativo.pdf"

    if not html_file.exists():
        print(f"❌ Arquivo HTML não encontrado: {html_file}")
        return 1

    candidatos_browser = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]

    browser_exe = None
    for b in candidatos_browser:
        if os.path.exists(b):
            browser_exe = b
            break

    if not browser_exe:
        print("❌ Nenhum navegador compatível encontrado (Chrome ou Edge).")
        return 1

    print(f"🖨️ Navegador selecionado: {browser_exe}")
    print(f"📄 Documento de origem: {html_file.name}")
    print(f"📦 Destino: {pdf_file.name}")

    url = html_file.as_uri()

    cmd = [
        browser_exe,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={str(pdf_file)}",
        url
    ]

    print("⏳ Compilando PDF nas cores azul e laranja...")
    res = subprocess.run(cmd, capture_output=True, text=True)

    if pdf_file.exists() and pdf_file.stat().st_size > 0:
        tamanho_kb = pdf_file.stat().st_size / 1024
        print(f"✅ PDF gerado com sucesso!")
        print(f"📁 Arquivo: {pdf_file}")
        print(f"📊 Tamanho: {tamanho_kb:.1f} KB")
        return 0
    else:
        print("❌ Erro ao compilar o PDF.")
        if res.stderr:
            print(f"Detalhes: {res.stderr}")
        return 1

if __name__ == "__main__":
    sys.exit(gerar_pdf())
