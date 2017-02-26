#encoding=utf8
import httplib
import json
receipt = raw_input("Enter Your transactionReceiptString:")
jsonStr = json.dumps({"receipt-data":receipt})
#connect = httplib.HTTPSConnection("buy.itunes.apple.com")
# sandbox
connect=httplib.HTTPSConnection("sandbox.itunes.apple.com")
headers={"Content-type":"application/json"}
connect.request("POST","/verifyReceipt",jsonStr)
result=connect.getresponse()
data=result.read()
connect.close()
decodedJson=json.loads(data)
print decodedJson
