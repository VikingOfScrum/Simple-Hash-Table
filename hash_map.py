
class HashTable:

    # Creating a bucket list with given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    # Create buckets given user size of hash table
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert user given value into hash table
    def set_values(self, key, value):

        # Get hashed index from key via hash function
        hash_key = hash(key) % self.size

        # Using index to get bucket
        current_bucket = self.hash_table[hash_key]

        # Find if current bucket has same key as the key to be inserted
        found = False
        for index, record in enumerate(current_bucket):
            record_key, record_value = record

            # Break from for loop if key is found
            if record_key == key:
                found = True
                break

        # If current bucket has same key update the key value
        if found:
            current_bucket[index] = key, value

        # Else append key,value pair to current bucket
        else:
            current_bucket.append((key, value))

    # Search for value with given key and return value
    def get_value(self, key):

         # Get hashed index from key via hash function
        hash_key = hash(key) % self.size

        # Using index to get bucket
        current_bucket = self.hash_table[hash_key]

        # Find if current bucket has same key as the key to be inserted
        found = False
        for index, record in enumerate(current_bucket):
            record_key, record_value = record

            # Break from for loop if key is found
            if record_key == key:
                found = True
                break

        # If current bucket has same key return the key value
        if found:
            return record_value

        # Else return no match
        else:
            return "No record could be found."

    # Search and delete value from hash table given key
    def delete_value(self, key):

         # Get hashed index from key via hash function
        hash_key = hash(key) % self.size

        # Using index to get bucket
        current_bucket = self.hash_table[hash_key]

        # Find if current bucket has same key as the key to be inserted
        found = False
        for index, record in enumerate(current_bucket):
            record_key, record_value = record

            # Break from for loop if key is found
            if record_key == key:
                found = True
                break

        # If current bucket has same key pop from current bucket
        if found:
            current_bucket.pop(index)
        return

    # Format print string response
    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)

def switch(choice):
    match choice:

        # Case to add to hash table
        case "1":
            key = input('Input key to be added to hash table: ')
            value = input('Input desired value: ')
            create_hash_table.set_values(key, value)

        # Case to search hash table
        case "2":
            key = input('Input search key for hash table: ')
            print(create_hash_table.get_value(key))
            print()
        
        # Case to delete from hash table
        case "3":
            key = input('Input search key to delete from hash table: ')
            create_hash_table.delete_value(key)
            
        # Case to print hash table
        case "4":
           print(create_hash_table)
           print()
        
        # Case to exit program
        case "5":
            exit()

        case _:
            print("Invalid entry.")
    
    
# Ask user to create hash table size
set_table = input("Enter size of hash table: ")
create_hash_table = HashTable(int(set_table))


# Simple while loop to run menu options until user exits.
run = True

while(run):

    print("--- Menu ---")
    print("1. Add to hash table.")
    print("2. Search hash table.")
    print("3. Delete from hash table.")
    print("4. Print hash table.")
    print("5. Exit.")

    choice = input("Enter Menu option: ")
    switch(choice)


