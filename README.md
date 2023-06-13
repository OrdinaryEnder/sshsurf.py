# sshsurf.py
A shitty wrapper over ssh.surf API written in Python3


# Installing

You can use pip (i released the code to pypi lol)
```
pip install sshsurf.py
```

or from GitHub itself
```
pip install git+https://github.com/OrdinaryEnder/sshsurf.py
```

# Example

```py
from sshsurf import sshClient
import asyncio

client = sshClient("api key here")

async def main():
  await client.exec("/root", "echo 'Hello World'")
  

asyncio.run(main())
```
Docs coming soon
