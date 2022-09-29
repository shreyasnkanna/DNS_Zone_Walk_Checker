import dns.resolver
import os
import sys
import argparse
import warnings
warnings.filterwarnings("ignore")


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", nargs="+", help="Enter Domain to check DNS Security Configs (seperated by space for multiple inputs)")
parser.add_argument("-f", "--file", help="Enter full path to Input File")
args = parser.parse_args()

Input_File = args.file



def Zone_Walk_Check(DOMAIN):
        print("\n\n   -- Performing Zone_Walk Check for " + DOMAIN + " domain.. ")
        nameserver=[]
        try:
                answers = dns.resolver.query(DOMAIN, 'A')
        except:
                print("Could not find 'A record' for : "+DOMAIN)
                return False


        try:
                answers = dns.resolver.query(DOMAIN, 'NS')
                for rdata in answers:
                        nameserver+=[str(rdata)]
        except:
                print("Could not resolve NS for: "+DOMAIN)
                return False

        SOA=''
        try:
                answers = dns.resolver.query(DOMAIN, 'SOA')
                for rdata in answers:
                        SOA+=str(rdata)
        except:
                print("Could not resolve SOA for: "+DOMAIN)


        primary_nameserver="NULL"
        try:
                for h in nameserver:
                        if(str(h) in SOA):
                                primary_nameserver=h
                                break
        except:
                pass

        if(primary_nameserver!="NULL"):
                cmd = "dig axfr @"+primary_nameserver+" "+DOMAIN

                returned_value = os.popen(cmd).read()

                if("; transfer failed." in returned_value.lower()):
                        Zone_Walk_Flag = 1
                else:
                        Zone_Walk_Flag = 0
        else:
                Zone_Walk_Flag = 2


        if Zone_Walk_Flag == 0:
                print('DNS Zone Walking','DNS Zone Walking is Enabled.')
        elif Zone_Walk_Flag == 2:
                print('DNS Zone Walking',"Having Trouble findind Zone Walking.")
        else:
                print('DNS Zone Walking',"DNS Zone Walking is Disabled.")






if args.input:
        for each_term in args.input:
                Zone_Walk_Check(each_term)



elif args.file:
        print("\nReading from Input File: "+Input_File)
        with open(Input_File, 'r') as file:
                lines = file.readlines()
                for each_term in lines:
                        each_term = each_term.strip()
                        
                        Zone_Walk_Check(each_term)

else:
        print("No input provided!")
        sys.exit()
