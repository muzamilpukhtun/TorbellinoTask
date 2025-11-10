import hashlib
import json
def generateTransactionHash(data,securityParameter):
    #Converting the Dictionary To String if there is a need
    if isinstance(data,dict):
        data=json.dumps(data,sort_keys=True)
    #Add  Security Parameter Concatenation with data
    saltedData=f"{data}|λ={securityParameter}"
    #creating the hash of the data
    hashObject=hashlib.sha256(saltedData.encode('utf-8'))
    return hashObject.hexdigest()

    #Check how much the function is negligible as much as the value of λ is greater the as long the probability of breaking the funcition is complex and probability is zero like is the value of λ is 32 64 the probability may be higher to break the function but if the value of λ is 256 128 then it would be complex because the hacker has to tries billions of times of break the function and its impossible 
def isNegligible(probability,securityParameter=256):
    threshold=1/(2**securityParameter)
    return probability<threshold
