
import requests

url = "https://result.election.gov.np/JSONFiles/Election2079/Common/PAPartyTop5-S5.txt"
response = requests.get(url).json()
i = 0
while i<6:
    name= response[i]['PoliticalPartyName']

    info = response[i]
#b= a.encode(encoding='UTF-8',errors='strict')
    decoded_name = name.encode('latin1').decode('utf8')
    print(f"------------------------------------------\nParty: {decoded_name}")
    print(f"Win: {info['TotWin']}\nLead:{info['TotLead']}\nTotal Win Lead:{info['TotWinLead']}\n")
    
    i = i+1