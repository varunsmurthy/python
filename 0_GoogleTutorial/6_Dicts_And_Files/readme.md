https://developers.google.com/edu/python/dict-files

### Dict Hash Table

* Python's efficient key/value hash table structure is called a "dict". The contents of a dict can be written as a series of key:value pairs within braces { }, e.g. dict = {key1:value1, key2:value2, ... }.

* Looking up or setting a value in a dict uses square brackets, e.g. dict['foo'] looks up the value under the key 'foo'.

* A for loop on a dictionary iterates over its keys by default. The keys will appear in an arbitrary order. The methods dict.keys() and dict.values() return lists of the keys or values explicitly. There's also an items() which returns a list of (key, value) tuples, which is the most efficient way to examine all the key value data in the dictionary.

### Dict formatting

* The % operator works conveniently to substitute values from a dict into a string by name.  

* e.g. s = 'I want %(count)d copies of %(word)s' % dictVar , where count and word are names of keys in the doct variable, dictVar.

### Del

* The "del" operator does deletions. In the simplest case, it can remove the definition of a variable, as if that variable had not been defined. Del can also be used on list elements or slices to delete that part of the list and to delete entries from a dictionary.

### Files


### Files Unicode


### Exercise Incremental Development