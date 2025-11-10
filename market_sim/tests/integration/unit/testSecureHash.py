from market_sim.blockchain.consensus.negligibleSecurity import generateTransactionHash,isNegligible

def testTransactionHash():
    #Demo Hashes
    transactionOne={"Sender":"Muzamil","Reciever":"Juan","Message":"Internship Task","amount":20}
    transactionTwo={"Sender":"Muzamil","Reciever":"Juan","Message":"Internship Task Details","amount":30}

    #Generating Two hashes using the function created in the blockchain folder
    hashOne=generateTransactionHash("HashTransactionOne",transactionOne)
    hashTwo=generateTransactionHash("HashTransactionTwo",transactionTwo)

    print("Hash One:",hashOne)
    print("Hash Two:",hashTwo)
    #Test that is there any collision in the hashes of transaction like is there any hashes of multiple transactions which is same like a and b has 2 hashes are they same or different
    assert hashOne!=hashTwo,"Collision Found But dont worry it too small may be negligible"

    #Testing how much the function is negligible is it easy or impossible to access by the hacker
def testNegligibleFunction():
    probability=1/(2**200)
    print("Negligible?",isNegligible(probability,64))