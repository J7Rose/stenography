# Jose Gonzalez
# 1001705536
# 03/07/2025

import bitstring

class Stenography:
    def __init__(self, ):
        self._get_user_input()

    def _get_user_input(self, ):
        print("Modes:\n" "1: Embedding\n" "2: Retrieval")
        self.C = int(input("Enter mode of operation: "))
        
        self.P = input("Enter plaintext file: ")
        self.S = int(input("Enter starting bit: "))
        self.L = input("Enter length (periodicity) of the replacement (in bits): ")
        self.L = [int(i) for i in self.L.split(",")]
        
        self.M = input("Enter message file: ")
        
    def embed(self, ):
        # read P and M by bits
        p_bits = bitstring.BitArray(filename=self.P)
        m_bits = bitstring.BitArray(filename=self.M)

        # set index to starting bit
        idx = self.S
        i = 0

        # loop through P and M files
        while i < len(m_bits) and idx < len(p_bits):
            # replace bits
            p_bits[idx] = m_bits[i]
            i += 1

            # move to next M bit index based on L (periodicity)
            idx += self.L[i % len(self.L)]

        # save changes to output file
        with open(self.P, "wb") as f:
            f.write(p_bits.bytes)
    
    def retrieve(self, ):
        # read plaintext file and initialize empty message bit array
        p_bits = bitstring.BitArray(filename=self.P)
        m_bits = bitstring.BitArray()

        # get message from plaintext file
        idx = self.S
        while idx < len(p_bits):
            # get bit from plaintext and save it to message
            m_bits.append(bitstring.BitArray(uint=int(p_bits[idx]), length=1))

            # move to next index
            idx += self.L[len(m_bits) % len(self.L)]

        # pad message to full byte if incomplete
        if len(m_bits) % 8 != 0:
            padding = 8 - (len(m_bits) % 8)
            m_bits.append(bitstring.BitArray(uint=0, length=padding))
        
        # write data to file
        with open(self.M, "wb") as f:
            f.write(m_bits.bytes)

                
def main():
    print("Stenography")

    user_stenography = Stenography()

    if user_stenography.C == 1:
        user_stenography.embed()
    elif user_stenography.C == 2:
        user_stenography.retrieve()
    

if __name__ == "__main__":
    main()
