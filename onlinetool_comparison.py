import csv

handle=open("F:\work\data.csv")
r=csv.reader(handle)
count=0
counts=0
for rows in r:
    for cols in rows:
        print(cols)
    if(rows[10]=="v.Positive"):
        row="Positive"
    elif(rows[10]=="v.Negative"):
        row="Negative"
    else:
        row=rows[10]

    print("sentiment is ")
    print(rows[4])
    print("predicted sentiment is ")
    print(row)

    if(rows[4]==row):
        count=count+1
    if(rows[4]==rows[11]):
        counts=counts+1;

print(count/105.0)
print(counts/105.0)