from colorama import Fore
import json,random

class LoadAccounts():
    def __init__(self):
        self.make_json()
    def read_file(self):
        with open("apis.txt","r",encoding="utf-8") as file:
            apis = file.readlines()
            apis = [api.strip() for api in apis]
        api = random.choice(apis).split(" ")
        return api[0],api[1]

    def write_json(self,data,output_filename):
        with open(f"{output_filename}.json","w",encoding="utf-8") as output:
            json.dump(data,output)

    def readfile(self,filename):
        account_list = []
        proxy = ""
        with open(f"{filename}.txt","r",encoding="utf-8") as file:
            phones =[phone.strip() for phone in file.readlines()]
            for phone in phones:
                api,hash = self.read_file()
                jsondata = {}
                jsondata["api_id"] = api
                jsondata["api_hash"]=hash
                jsondata["phone"]=phone
                jsondata["proxy"] = proxy
                account_list.append(jsondata)
        return account_list
    def make_json(self):
        try:
            account_list = self.readfile("alive_acc")
            print(Fore.GREEN,"File Read Successful")
        except Exception as err:
            print(Fore.RED,err,Fore.RESET)
        
        output_file = "accounts"
        try:
            self.write_json(account_list,output_file)
            print(Fore.GREEN,"New Account File Loaded Successful")
        except Exception as err:
            print(Fore.RED,err,Fore.RESET)


if __name__ =="__main__":
    bot = LoadAccounts()
