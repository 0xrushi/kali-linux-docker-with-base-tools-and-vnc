# A prebuilt kali-linux with GUI aka vnc in docker in 2 seconds

#### Steps to run

```
git clone https://github.com/rushic24/kali-linux-docker-with-base-tools-and-vnc.git
cd kali-linux-docker-with-base-tools-and-vnc
docker build -t mykali-light .
mkdir ~/container-data #optional if you want to share a directory
docker run -p 5900:5900 --rm -i -t -v ~/container-data:/root/data/ mykali-light 
```

Connect to vnc from Host machine on 

```
localhost:5900
```

Once inside start xfce session in the white terminal 

```
startxfce4
```

