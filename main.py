import discord
import requests

HGKey = "SUA_KEY_HGBrasil"

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()

    def printAtivo(mensagem):
        splitMensagem = mensagem.lower().split(" ")
        ativo = splitMensagem[1]
        link = "https://api.hgbrasil.com/finance/stock_price?key=" + HGKey +"&symbol=" + ativo

        response = requests.get(link)
        string = response.text

        stringInArray = string.split(",")
        intermediario = stringInArray[2].split(':')
        erro = intermediario[2]

        if erro == '{"error"':
            toReturn = 'Cotação "' + ativo.upper() + '" não encontrada!'
        else:
            stringInArray = string.split(",")
            price = stringInArray[14].split(':')
            valor = price[1]

            toReturn = 'Cotação ' + ativo.upper() + ': '  + valor + ' R$'

        return toReturn

    if message.content.startswith("-b3 ping"):

        await message.channel.send("pong")

    elif message.content.startswith("-b3 help"):

        await message.channel.send('Digite: "-b3 <ATIVO>" para saber a cotação atual do ativo \nDigite: "-b3 ping" para testar o bot (recebendo um "pong" em resposta)\n\nAtenção!: "Cotei! - [B]³ Cotações Bot" não possuí envolvimento com a bolsa "[B]³" assim como não se resposabiliza por lucos ou perdas dos usuários. O bot apenas informa a cotação das ações por meio de APIs públicas e privadas.\n\nCriado por @MarlonHenq  https://github.com/MarlonHenq')

    elif message.content.startswith("-b3"):
        await message.channel.send(printAtivo(message.content))


client.run('BOT_CLIENT_ID')
