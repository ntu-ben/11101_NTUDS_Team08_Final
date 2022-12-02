word_freq = {
"Hello": 56,
"at": 23,
"test": 43,
"this": 78
}
 
key = 'sample'
if word_freq.get(key) is not None:
    print(":)")
else:
    print(":<")