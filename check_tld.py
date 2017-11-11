import dns.resolver

# Set the DNS Server
resolver = dns.resolver.Resolver()
resolver.nameservers=["8.8.8.8"]

with open('tlds.txt') as tld_file:
    tld_file.readline()
    tlds = list(tld_file)

for tld in tlds:
    for rdata in resolver.query("{}.".format(tld.strip()), 'ns'):
        print("<{}> {}".format(tld.strip(), rdata.target))
    print()
