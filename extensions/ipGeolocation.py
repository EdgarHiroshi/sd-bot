from discord.ext import commands
from http.client import HTTPConnection
from ipaddress import ip_address
import json

class ipGeolocation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    def getAddressByIP(ip = ''):
        inputIp = ip.strip()

        if inputIp == '':
            return "Endereço IPv4/IPv6 inválido"

        try:
            ip_address(inputIp)
        except ValueError:
            return "Endereço IPv4/IPv6 inválido"

        response = None
        requestClient = None
        try:
            requestAddress = "www.ip-api.com"

            requestClient = HTTPConnection(requestAddress)
            
            requestPath = "/json/{}?fields=49177&lang=pt-BR".format(inputIp)
            requestClient.request("GET", requestPath)

            response = json.load(requestClient.getresponse())

            if response["status"] == "fail":
                return "Requisição falhou [" + response["message"]  + "]"

        except:
            return "Requisição falhou"
        finally:
            if requestClient != None:
                requestClient.close()

        return response

    @commands.command()
    async def localiza(self, ctx, args):
        ip = str(args)
        resposta = self.getAddressByIP(ip)

        strResposta = ""
        if isinstance(resposta, dict):
            strResposta = f"O ip {ip} está localizado no(a) {resposta['country']} na região de {resposta['regionName']} na cidade de {resposta['city']}"
        else:
            strResposta = resposta
        
        await ctx.send(strResposta)

def setup(bot):
    bot.add_cog(ipGeolocation(bot))
    print('Loaded ipGeolocation.py')