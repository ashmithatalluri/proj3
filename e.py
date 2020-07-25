def most_frequent(s):
      d={"m":1,"i":4,"s":4,"p":2}

      sort= sorted(d, key=d.get,reverse= True)
      for a in sort:
            print(a,d[a])




s=("Mississippi")
most_frequent(s)
