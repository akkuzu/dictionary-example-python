
'''
A data type in Python.
Dictionaries are indexed by keys and these keys can be a String and integer type.
Shown as key:value pairs and keys are the unique values.
'''

d={}
print(d)
print(type(d))

d={"python":1 , "course":2}
print(d)

d2= {"machine":"learning","artificial":"intelligence"}
print(d2)

print(d2["artificial"])

d2["java"]= "programming"
print(d2)

d2["ruby"] = "language"
print(d2)

print(d)
print(d["course"])
print(d.keys())
print(d2.keys())

for k in d2.keys():
    print(k)

for v in d2.values():
    print(v)

for k,v in d.items():
  if v == 2:
    print(k)

d["a"]=[3,4,5]
print(d)

d.pop("python")
print(d)
print(len(d))

d2.get("artificial")

d4 = {"human":2,
      "cat":4,
      "spider":8
     }

for i in d4:
  leg = d4[i]
  print("%s has %d legs " % (i,leg))
  print(str(i) + " has " + str(leg) +" legs.")

d4 = {"human":2, "cat":4, "spider":8}

for i,leg in d4.items():
  print(str(i) + " has " + str(leg) +" legs.")
