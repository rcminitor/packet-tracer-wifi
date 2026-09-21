#!/usr/bin/env python3
"""
Abre o tutorial Wi-Fi Corporativo no browser.
Uso:
    python abrir_tutorial.py           # Abre no browser padrão
    python abrir_tutorial.py --chrome  # Força Chrome
    python abrir_tutorial.py --firefox # Força Firefox
    python abrir_tutorial.py --server  # Inicia servidor HTTP local (porta 8000)
"""
import argparse
import webbrowser
import sys
import subprocess
import time
from pathlib import Path


def abrir_browser_padrao(caminho: Path) -> bool:
    """Abre no browser padrão do sistema."""
    try:
        webbrowser.open(caminho.as_uri())
        print(f"✅ Aberto no browser padrão: {caminho}")
        return True
    except Exception as e:
        print(f"❌ Erro ao abrir no browser padrão: {e}")
        return False


def abrir_chrome(caminho: Path) -> bool:
    """Tenta abrir especificamente no Chrome."""
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\Application\chrome.exe",
    ]
    for chrome in chrome_paths:
        chrome_expanded = Path(chrome).expandvars()
        if chrome_expanded.exists():
            try:
                subprocess.Popen([str(chrome_expanded), caminho.as_uri()])
                print(f"✅ Aberto no Chrome: {caminho}")
                return True
            except Exception as e:
                print(f"❌ Erro ao abrir no Chrome: {e}")
                return False
    print("❌ Chrome não encontrado nos caminhos padrão")
    return False


def abrir_firefox(caminho: Path) -> bool:
    """Tenta abrir especificamente no Firefox."""
    firefox_paths = [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
    ]
    for ff in firefox_paths:
        ff_expanded = Path(ff).expandvars()
        if ff_expanded.exists():
            try:
                subprocess.Popen([str(ff_expanded), caminho.as_uri()])
                print(f"✅ Aberto no Firefox: {caminho}")
                return True
            except Exception as e:
                print(f"❌ Erro ao abrir no Firefox: {e}")
                return False
    print("❌ Firefox não encontrado nos caminhos padrão")
    return False


def iniciar_servidor_http(caminho: Path, porta: int = 8000) -> bool:
    """Inicia servidor HTTP local e abre no browser."""
    try:
        pasta = caminho.parent
        print(f"🌐 Iniciando servidor HTTP em http://localhost:{porta}")
        print(f"📁 Servindo: {pasta}")
        print("   Pressione Ctrl+C para parar o servidor")

        # Abre o browser após um breve delay
        def abrir_apos_inicio():
            time.sleep(1.5)
            webbrowser.open(f"http://localhost:{porta}/index.html")

        import threading
        threading.Thread(target=abrir_apos_inicio, daemon=True).start()

        # Inicia o servidor (bloqueia até Ctrl+C)
        subprocess.run([sys.executable, "-m", "http.server", str(porta)], cwd=pasta)
        return True
    except KeyboardInterrupt:
        print("\n🛑 Servidor parado")
        return True
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Abre o tutorial Wi-Fi Corporativo")
    parser.add_argument("--chrome", action="store_true", help="Abrir no Chrome")
    parser.add_argument("--firefox", action="store_true", help="Abrir no Firefox")
    parser.add_argument("--server", action="store_true", help="Iniciar servidor HTTP local (porta 8000)")
    parser.add_argument("--port", type=int, default=8000, help="Porta para servidor HTTP (padrão: 8000)")
    args = parser.parse_args()

    caminho = Path(__file__).parent / "index.html"

    if not caminho.exists():
        print(f"❌ Arquivo não encontrado: {caminho}")
        return 1

    print(f"📄 Tutorial: {caminho.name}")
    print(f"📍 Local: {caminho.parent}")
    print()

    if args.server:
        return 0 if iniciar_servidor_http(caminho, args.port) else 1
    elif args.chrome:
        return 0 if abrir_chrome(caminho) else 1
    elif args.firefox:
        return 0 if abrir_firefox(caminho) else 1
    else:
        return 0 if abrir_browser_padrao(caminho) else 1


if __name__ == "__main__":
    sys.exit(main())