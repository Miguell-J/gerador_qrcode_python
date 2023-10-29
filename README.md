# Gerador de QR Code

<img src="qrcode.png"/>

Este é um programa simples em Python que usa a biblioteca `qrcode` para gerar um código QR a partir de uma URL e, em seguida, salva o QR Code como uma imagem.

## Instruções

1. Certifique-se de que você tem a biblioteca `qrcode` instalada. Caso não tenha, você pode instalá-la usando o pip: `pip install qrcode[pil]`.

2. Execute o código em um ambiente Python compatível.

3. O código gera um QR Code para a URL 'https://github.com', mas você pode facilmente personalizá-lo alterando a URL na linha `img = qrcode.make('https://github.com')`.

4. O código salvará o QR Code como uma imagem chamada 'QRcode.png' no mesmo diretório em que o script está localizado.

## Exemplo de Uso

Após a execução do código, você encontrará um arquivo 'QRcode.png' no mesmo diretório, que contém o código QR para a URL fornecida.

## Notas

- Certifique-se de que você tem a biblioteca `Pillow` instalada, pois ela é necessária para salvar o QR Code como uma imagem. Caso não a tenha instalada, você pode fazê-lo com o comando `pip install pillow`.

Agora você pode gerar QR Codes para as URLs de sua escolha de forma simples e rápida!