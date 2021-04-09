import requests
import json

class metabasepy:
	def __init__(self, base_url,username,password):
		self.base_url=base_url
		if base_url[-1]=="/": #Remove final slash if present metabase can't handle //
			self.base_url=base_url[:-1]
		creds={"username":username,"password":password,"remember":"true"}
		
		req=requests.post(self.base_url+"/api/session",json=creds)
		#print(req.text)
		
		if req.status_code>=200 and req.status_code<300:
			self.token=req.json()
		else:
			self.token=None
			raise Exception("Unexpected status code recieved."+req.text)


	def fetch_question(self,question_id, parameters, tempdir=None):
		if self.token==None:
			raise Exception("Token is null")
		params=[]
		for p,v in parameters.items():
			params.append({"type":"category","target":["variable",["template-tag",p]],"value":v})
		url=f"{self.base_url}/api/card/{question_id}/query/json"
		headers={
			"X-Metabase-Session":self.token["id"],
			"Content-Type":"application/x-www-form-urlencoded",
		}
		req=requests.post(url,headers=headers,data={"parameters":json.dumps(params)}) #If this fails, try data=params     ,encode="form")
		#if (req$status_code < 200 || req$status_code >= 300) { raise Exception
		if tempdir!=None:
			#dump req.text to a temporary file in tmpdir
			pass
		#print(req.text)
		return req.json()


if __name__=="__main__":
	user=input("Username: ").strip()
	passwd=input("password: ").strip()
	url=input("Base url: ").strip()
	mb=metabasepy(url,user,passwd)
	print(mb.token)
