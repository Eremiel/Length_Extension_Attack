Cryptographic hash functions, such as MD5, SHA1, SHA2, etc., are based on a construct known as Merkle–Damgård. 
An interesting issue arises with this type of hash function: If you have a message that is concatenated with a secret and the resulting hash of the concatenated value (the MAC) – and you know only the length of that secret – you can add your own data to the message and calculate a value that will pass the MAC check without knowing the secret itself.

https://www.whitehatsec.com/blog/hash-length-extension-attacks/

This repo contains simple python script, used to launch an LE attack. It uses hlextend library provided by https://github.com/stephenbradshaw/hlextend


Usage:
set the values for
-mydata
-knowndata
-knownhash
and mofiy the url to fit your use. Launch the script.
