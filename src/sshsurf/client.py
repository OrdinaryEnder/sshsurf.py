import aiohttp




class sshClient:
    def __init__(self, apikey: str):
        self.sshheader = {'x-ssh-auth': apikey}
        self.base_url = "https://api.ssh.surf"



    async def hello(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/hello') as resp:
                result = await resp.json()
        
        return result

    async def name(self):
        # its kinda pointless to make this but its alrigh
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/name'):
                result = await resp.json()

        return result


    async def start(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/start') as resp:
                result = await resp.json()
        
        return result

    async def stop(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/stop'):
                result = await resp.json()

        return result

    async def restart(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/restart') as resp:
                result = await resp.json()
        
        return result

    async def info(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/info'):
                result = await resp.json()

        return result


    async def stats(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/stats') as resp:
                result = await resp.json()
        
        return result

    async def time(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/time'):
                result = await resp.json()

        return result



    async def rootpass(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/rootpass') as resp:
                result = await resp.json()
        
        return result

    async def newkey(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/new-key'):
                result = await resp.json()

        return result



    async def keytime(self):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/key-time') as resp:
                result = await resp.json()
        
        return result

    async def license(self):
        # its kinda pointless to make this but its alrigh
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.get(self.base_url + '/license'):
                result = await resp.json()

        return result

    async def exec(self, pwd: str, cmd: str):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.post(self.base_url + '/exec', json={"pwd": pwd, "cmd": cmd}) as resp:
                result = await resp.json()
        return result

    async def notify(self, message: str):
        async with aiohttp.ClientSession(headers=self.sshheader) as ses:
            async with ses.post(self.base_url + '/notify', json={'message': message}) as resp:
                result = await resp.json()

        return result


if __name__ == '__main__':
    print("https://youtu.be/qZWCxNDRVPc")
