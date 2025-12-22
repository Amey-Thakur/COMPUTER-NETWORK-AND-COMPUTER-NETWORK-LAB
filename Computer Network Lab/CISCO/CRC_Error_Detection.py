"""
Cyclic Redundancy Check (CRC) Implementation
Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
Repository: https://github.com/Amey-Thakur/COMPUTER-NETWORK-AND-COMPUTER-NETWORK-LAB

Description:
This program implements the Cyclic Redundancy Check (CRC) algorithm for error detection
in data transmission. CRC is widely used in network protocols and storage devices to
detect accidental changes to raw data.

How CRC Works:
1. Sender appends (n-1) zeros to the data (where n = length of key/divisor)
2. Performs modulo-2 division (XOR-based division)
3. The remainder becomes the CRC checksum
4. Sender transmits: Original Data + CRC Checksum

At receiver side:
- Divide received data by same key
- If remainder is 0, data is error-free
- If remainder is non-zero, error detected

Example:
Data: 10110010
Key (Generator Polynomial): 101
CRC will calculate and append the checksum
"""

def xor(a, b):
    """
    Performs XOR operation on two binary strings of equal length.
    
    Args:
        a (str): First binary string
        b (str): Second binary string
    
    Returns:
        str: Result of XOR operation
    
    Logic:
        - If bits are same (0,0 or 1,1): XOR = 0
        - If bits are different (0,1 or 1,0): XOR = 1
    """
    result = []
    
    # Start from index 1 to skip the first bit (used for division logic)
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')  # Same bits: XOR = 0
        else:
            result.append('1')  # Different bits: XOR = 1
    
    return ''.join(result)


def mod2div(dividend, divisor):
    """
    Performs Modulo-2 division (binary division using XOR).
    
    Args:
        dividend (str): Binary string to be divided
        divisor (str): Binary string divisor (generator polynomial)
    
    Returns:
        str: Remainder of the division (CRC checksum)
    
    Process:
        - Similar to long division but uses XOR instead of subtraction
        - No concept of greater/smaller numbers
        - Division continues until all bits are processed
    """
    # Number of bits to be XORed at a time (length of divisor)
    pick = len(divisor)
    
    # Take first 'pick' bits from dividend
    tmp = dividend[0:pick]
    
    # Process remaining bits one by one
    while pick < len(dividend):
        
        if tmp[0] == '1':
            # If leftmost bit is 1, XOR with divisor
            # Then append next bit from dividend
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            # If leftmost bit is 0, XOR with all zeros
            # (equivalent to just shifting)
            tmp = xor('0' * pick, tmp) + dividend[pick]
        
        # Move to next bit
        pick += 1
    
    # Process the last set of bits
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    
    # The final tmp is the remainder (CRC checksum)
    checkword = tmp
    return checkword


def encodeData(data, key):
    """
    Encodes data by appending CRC checksum.
    This is done at the sender side before transmission.
    
    Args:
        data (str): Original binary data to be transmitted
        key (str): Generator polynomial (divisor)
    
    Process:
        1. Append (n-1) zeros to data where n = length of key
        2. Perform modulo-2 division
        3. Append remainder to original data
        4. Transmit: Data + Remainder
    """
    l_key = len(key)
    
    # Append (n-1) zeros to the data
    # This creates space for the CRC checksum
    appended_data = data + '0' * (l_key - 1)
    print(f"Data with appended zeros: {appended_data}")
    
    # Calculate CRC checksum using modulo-2 division
    remainder = mod2div(appended_data, key)
    
    # Create final codeword: Original Data + CRC Checksum
    codeword = data + remainder
    
    # Display results
    print(f"\nOriginal Data: {data}")
    print(f"Generator Polynomial (Key): {key}")
    print(f"CRC Checksum (Remainder): {remainder}")
    print(f"Encoded Data (Data + CRC): {codeword}")
    print(f"\nTransmit this codeword: {codeword}")
    
    return codeword


# ==================== MAIN PROGRAM ====================
if __name__ == "__main__":
    print("=" * 60)
    print("CRC (Cyclic Redundancy Check) - Error Detection")
    print("=" * 60)
    
    # Example data and generator polynomial
    # In real applications, these would be provided by the network protocol
    data = "10110010"  # 8-bit data to be transmitted
    key = "101"        # 3-bit generator polynomial (CRC-2)
    
    print(f"\nInput Configuration:")
    print(f"Data to transmit: {data}")
    print(f"Generator Polynomial: {key}")
    print("\nCalculating CRC...\n")
    
    # Encode the data
    encoded = encodeData(data, key)
    
    print("\n" + "=" * 60)
    print("Transmission Complete!")
    print("=" * 60)
    print("\nNote: At receiver side, divide the received codeword by")
    print(f"the same key ({key}). If remainder is all zeros, no error.")
    print("If remainder is non-zero, error detected in transmission.")
