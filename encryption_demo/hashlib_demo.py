import hashlib

md5 = hashlib.md5()
md5.update(str(('p', 'n', 's', 't')).encode('utf-8'))
unique_id = md5.hexdigest()
print(unique_id)