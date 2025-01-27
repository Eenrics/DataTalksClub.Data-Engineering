## Question 1. Understanding docker first run

Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash.

What's the version of pip in the image?

- [ ] 24.3.1
- [ ] 24.2.1
- [ ] 23.3.1
- [ ] 23.2.1

## Answer

```bash
$ docker run -it python:3.12.8 bash

Unable to find image 'python:3.12.8' locally
3.12.8: Pulling from library/python
e474a4a4cbbf: Downloading [=========================================>         ]  39.73MB/48.31MB
d22b85d68f8a: Download complete
936252136b92: Downloading [==============================>                    ]  39.17MB/64.36MB
94c5996c7a64: Downloading [====>                                              ]  17.77MB/202.7MB
c980de82d033: Waiting
c80762877ac5: Waiting
86f9cc2995ad: Waiting
Digest: sha256:2e726959b8df5cd9fd95a4cbd6dcd23d8a89e750e9c2c5dc077ba56365c6a925
Status: Downloaded newer image for python:3.12.8

root@d1f38d3b2fac:/# pip --version
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
root@d1f38d3b2fac:/#
```

> 24.3.1
