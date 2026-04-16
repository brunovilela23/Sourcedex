# Sourcedex
<img width="1114" height="674" alt="image" src="https://github.com/user-attachments/assets/3ba9681c-9add-45a1-b21e-3b3207a46a40" />

Um script em Python simples e eficiente para extrair URLs e identificar parâmetros de consulta (query strings) a partir de uma página web. Ideal para profissionais de segurança (Pentest), desenvolvedores e entusiastas de automação.

O SourceDex analisa o código HTML de uma URL fornecida, identifica tags que contêm links (como , <script>, , etc.) e extrai todos os parâmetros encontrados. O script também simula um navegador real usando cabeçalhos HTTP personalizados para evitar bloqueios simples.

Funcionalidades Extração Multitag: Captura URLs em atributos href e src.

Análise de Parâmetros: Isola e exibe chaves e valores de parâmetros das URLs encontradas.

Saída Colorida: Interface de terminal organizada por cores para facilitar a leitura.

Normalização de URL: Adiciona automaticamente o protocolo https:// caso o usuário esqueça.

🛠️ Instalação

Clonar o repositório

git clone https://github.com/brunovilela23/Sourcedex.git

Instalar dependências Este script utiliza as bibliotecas requests e beautifulsoup4. Instale-as via pip:

pip install requests beautifulsoup4

Como usar Para executar o script, basta rodar o comando abaixo no terminal:

python3 sourcedex.py

Caso não queira digitar toda hora python3 sourcedex.py faça o seguinte:

mv sourcedex.py /usr/local/bin/sourcedex

chmod +x /usr/local/bin/sourcedex

Pronto, pode chamar o script de qualquer lugar apenas digitando sourcedex.

⚠️ Aviso Legal Este script foi desenvolvido para fins educacionais e de pesquisa. O uso desta ferramenta para realizar atividades sem autorização prévia em sistemas de terceiros é de inteira responsabilidade do usuário. O autor não se responsabiliza por qualquer uso indevido.

Xabaluba!
