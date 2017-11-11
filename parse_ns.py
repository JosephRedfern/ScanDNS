import socket
import tqdm

ns = list()
with open("ns.txt", "r") as nsf:
    for l in nsf:
        ns.append(l.split(" ")[-1])

for i in tqdm.tqdm(set(ns)):
    nsaddr = i.strip()[:-1].lower()
    try:
        socket.gethostbyname(nsaddr)
    except socket.gaierror:
        print("unable to get address for", nsaddr)
