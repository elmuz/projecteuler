# Read file and convert into a list of integer numbers
with open('p059_cipher.txt') as file:  
    data = file.read() 
splitted = data.split(',')
encoded = [int(a) for a in splitted]

# For every ASCII lower case chars test XOR decypher
best_score = 0
best_key = []
best_decoded = []
for k1 in range(97, 123):
    for k2 in range(97, 123):
        for k3 in range(97, 123):
            decoded = []
            for i in range(len(encoded)):
                if i % 3 == 0:
                    decoded.append(encoded[i] ^ k1)
                elif i % 3 == 1:
                    decoded.append(encoded[i] ^ k2)
                else:
                    decoded.append(encoded[i] ^ k3)
            # Speculate that English text will have many space chars (32), so look for the most frequent
            score_temp = decoded.count(32)
            if score_temp > best_score:
                best_score = score_temp
                best_key = [k1, k2, k3]
                best_decoded = decoded

# Print decoded text
decoded_msg = ''.join([chr(a) for a in best_decoded])
print(decoded_msg)
print('Original message ASCII sum:', sum(best_decoded))
