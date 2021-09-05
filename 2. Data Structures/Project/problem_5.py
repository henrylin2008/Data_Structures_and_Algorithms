# Blockchain
# A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and
# how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the
# previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash,
# the Greenwich Mean Time when the block was created, and text strings as the data.
#
# Use your knowledge of linked lists and hashing to create a blockchain implementation.
#
# We can break the blockchain down into three main parts.
#
import hashlib
import datetime

# the block on the blockchain:
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        return (f'Timestamp: {self.timestamp} \n'
                f'Data: {self.data} \n'
                f'Hash: {self.hash} \n'
                f'Previous Hash: {self.previous_hash}')

def get_utc_time():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%m-%d-%y %H:%M:%S")

class Node:
    def __init__(self, block):
        self.block = block
        self.next = None

    def __str__(self):
        return str(self.block)

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data=None):
        timestamp = get_utc_time()
        if self.head:
            block = Block(timestamp, data, self.tail.block.hash)
            node = Node(block)
            self.tail.next = node
            self.tail = node
        else:
            block = Block(timestamp, data, 0)
            node = Node(block)
            self.head = node
            self.tail = node
        return

    def __str__(self):
        current_node = self.head
        output = ""
        while current_node:
            output += str(current_node) + " \n\n"
            current_node = current_node.next
        return output


# test cases
# case 1:adding blocks
block_chain = BlockChain()
print("Blockchain 1:")
block_chain.add_block("Block 0")      # adding first block
block_chain.add_block("Block 1")     # adding second block
block_chain.add_block("Block 2")      # adding third block
print(block_chain)
print("Blockchain 1 Head:")
print(block_chain.head)
print("")
print("Blockchain 1 tail:")
print(block_chain.tail)
print("")

# edge case - empty block
print("Blockchain 2:")
block_chain2 = BlockChain()
block_chain2.add_block()
print(block_chain2)

# edge case - empty blockchain
print("Blockchain 3:")
bc3 = BlockChain()
print(bc3)
