# 📡 Tutorial Interativo: Rede Wi-Fi Corporativa no Cisco Packet Tracer

[![Cisco Packet Tracer](https://img.shields.io/badge/Cisco_Packet_Tracer-v8.x-005073?style=for-the-badge&logo=cisco&logoColor=white)](https://www.netacad.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

Tutorial interativo passo a passo para simulação e configuração de uma **Rede Wi-Fi Corporativa** utilizando **Lightweight Access Point (LAP)** gerenciado centralmente por uma **Wireless LAN Controller (WLC)** no **Cisco Packet Tracer**.

---

## 🧭 Visão Geral e Arquitetura

Em ambientes residenciais ou pequenas empresas, costuma-se usar Access Points autônomos. Em redes corporativas (universidades, hospitais, shoppings), a configuração manual de centenas de APs é inviável.

Esta topologia demonstra a arquitetura corporativa moderna:
- **WLC (Wireless LAN Controller):** O "cérebro" da rede sem fio. Concentra todas as configurações de SSIDs, segurança e canais.
- **LAP (Lightweight Access Point):** Ponto de acesso "leve". Não funciona de forma autônoma; descobre a WLC via DHCP (Option/WLC Address) e baixa as políticas automaticamente.
- **Servidor DHCP:** Distribui endereços IP para a infraestrutura e para os clientes sem fio, fornecendo o ponteiro do endereço da WLC.

```mermaid
graph TD
    subgraph Infraestrutura Cabeada
        SW[Switch Cisco 2960]
        SRV[Servidor DHCP<br>192.168.0.10]
        WLC[Controladora WLC-PT<br>192.168.0.20]
        LAP[Access Point LAP-PT<br>192.168.0.100]
        
        SRV ---|FastEthernet| SW
        WLC ---|Gigabit/FastEthernet| SW
        LAP ---|FastEthernet| SW
    end

    subgraph Clientes Wi-Fi (SSID: RedeAlunos)
        PC0[PC0 com placa WMP300N<br>192.168.0.100 via DHCP]
        PC1[PC1 com placa WMP300N<br>192.168.0.101 via DHCP]
        
        LAP -.->|Wi-Fi WPA2-PSK| PC0
        LAP -.->|Wi-Fi WPA2-PSK| PC1
    end

    style WLC fill:#0284c7,stroke:#0369a1,color:#fff
    style LAP fill:#0ea5e9,stroke:#0284c7,color:#fff
    style SRV fill:#10b981,stroke:#059669,color:#fff
    style SW fill:#64748b,stroke:#475569,color:#fff
    style PC0 fill:#8b5cf6,stroke:#7c3aed,color:#fff
    style PC1 fill:#8b5cf6,stroke:#7c3aed,color:#fff
```

---

## 📋 Tabela de Endereçamento e Parâmetros

| Dispositivo | Interface | Endereço IP | Máscara | Método |
|---|---|---|---|---|
| **Server0** | FastEthernet0 | `192.168.0.10` | `255.255.255.0` | Estático |
| **WLC-PT** | Management | `192.168.0.20` | `255.255.255.0` | Estático |
| **LAP-PT** | Gigabit/Fa | `192.168.0.100` | `255.255.255.0` | DHCP (Server0) |
| **PC0** | Wireless0 | `192.168.0.100` | `255.255.255.0` | DHCP (Server0) |
| **PC1** | Wireless0 | `192.168.0.101` | `255.255.255.0` | DHCP (Server0) |

### Parâmetros da Rede Sem Fio
- **SSID (Nome da Rede):** `RedeAlunos`
- **Segurança:** `WPA2-PSK`
- **Senha (Passphrase):** `12345678`
- **VLAN ID:** `1`
- **WLC Address (no DHCP):** `192.168.0.20`

---

## 🚀 Como Visualizar e Usar o Tutorial

O projeto conta com duas formas de uso:

### 1. Aplicação Web Interativa (`index.html`)
Abra o arquivo `index.html` em qualquer navegador moderno. O tutorial oferece:
- Navegação guiada em **12 telas interativas**.
- Suporte nativo a **Tema Claro e Escuro** (salvo automaticamente).
- **Zoom em Imagens (Lightbox)** com clique em qualquer captura de tela.
- **Botões de Cópia em 1 Clique** para IPs, senhas e comandos.
- **Checklist Interativo de Verificação** para os alunos validarem sua bancada de testes.
- **Mini-Quiz de Fixação** para consolidação da aprendizagem.
- **Modo Impressão/PDF** (`Ctrl + P` ou botão de imprimir) gerando apostila completa.

#### Executando via script Python:
```bash
# Abre no navegador padrão
python abrir_tutorial.py

# Ou inicia um servidor HTTP local na porta 8000
python abrir_tutorial.py --server
```

### 2. Guia em Formato Markdown (`tutorial_wifi_corporativo.md`)
O arquivo [`tutorial_wifi_corporativo.md`](tutorial_wifi_corporativo.md) contém o roteiro completo formatado em Markdown com todas as capturas de tela relativas, ideal para visualização rápida no VS Code ou leitura direta no GitHub.

---

## 🌐 Publicando no GitHub Pages (Acesso Online pelos Alunos)

Você pode disponibilizar este tutorial online para seus alunos em poucos segundos via GitHub Pages:

1. Faça o push deste repositório para o seu GitHub:
   ```bash
   git remote add origin https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
   git branch -M main
   git push -u origin main
   ```
2. No seu repositório no GitHub, acesse **Settings** > **Pages** (menu lateral esquerdo).
3. Em **Build and deployment**:
   - **Source:** selecione `Deploy from a branch`
   - **Branch:** selecione `main` e a pasta `/ (root)`
   - Clique em **Save**.
4. Em 1 minuto, sua página estará disponível publicamente no endereço:
   `https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/`

---

## ⚠️ Erros Comuns em Laboratório

1. **LAP desligado:** No Cisco Packet Tracer, o `LAP-PT` vem **desligado por padrão**. É preciso acessar a aba *Physical* e arrastar a fonte de alimentação para o conector redondo.
2. **Placa de rede dos PCs:** Os PCs vêm com interface cabeada. Deve-se desligar o PC, remover a placa FastEthernet, inserir o módulo wireless `WMP300N` e religar o computador.
3. **Endereço da WLC no DHCP:** Se o campo `WLC Address` não for preenchido com `192.168.0.20` no serviço DHCP do servidor, o LAP não saberá onde a controladora está e não transmitirá o sinal.
4. **Tempo de convergência:** No Packet Tracer, utilize o botão **Fast Forward Time (`>>`)** para acelerar a negociação CAPWAP e a concessão DHCP.

---

## 👨‍🏫 Autor e Créditos

Desenvolvido para fins didáticos e educacionais:
- **Prof. Romulo Cesar** — IFCE / Redes Cuca
- Projeto de apoio às disciplinas de Redes de Computadores e Conectividade Sem Fio.
