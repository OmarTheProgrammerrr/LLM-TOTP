##############

if __name__ == '__main__':
  given_key = 'abcd1234'


  #defince class LM-TOTP with a given secret key with base32 and TIME STEP 120 seconds (2 minutes)
  totp = LM_TOTP(given_key , 120)

  #generate totp at now timestamp 
  totp1 = totp.now()


  #generate totp at specific timestamp 
  totp2 = totp.at(12345)
  

  #validate a given TOTP 
  print(totp.validate('5647656'))
  
