#### Pair Problem

Map Reduce!  
Create your own mapper and reducer python files to generate a word count of the following:   

```
lucy foo lucy lu 
you some foo lucy girl
```

Use the following to get your wordcounts:
```bash
cat input.txt | python map.py | sort | python reduce.py > output  
```

The mapper should get results like this
```
lucy 1
foo 1
lucy 1
lu 1
you 1
some 1
foo 1
lucy 1
girl 1
```

and the final output should look like
```
foo 2
girl 1
lu 1
lucy 3
some 1
you 1
```
