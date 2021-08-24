# Blockchain
# A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and
# how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the
# previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash,
# the Greenwich Mean Time when the block was created, and text strings as the data.
#
# Use your knowledge of linked lists and hashing to create a blockchain implementation.
#
# We can break the blockchain down into three main parts.
# #
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
        return (f'Timestamp: {self.timestamp} \n '
                f'Data: {self.data} \n'
                f'Hash: {self.hash} \n'
                f'Previous Hash: {self.previous_hash} ')

def get_utc_time():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%m-%d-%y %H:%M:%S")

class Node:
    def __init__(self, node):
        self.node = node
        self.next = None

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        if self.head is None:
            timestamp = get_utc_time()
            data = data
            block = Block(timestamp, data, 0)
            node = Node(block)
            self.head = node
            self.tail = node
        else:
            timestamp = get_utc_time()
            data = data
            block = Block(timestamp, data, self.tail.node.hash)
            node = Node(block)
            self.tail.next = node
            self.tail = node
