# Bash RNG glitch

I generated three sets of random numbers using: MacBook Pro (13-inch, 2017, Two Thunderbolt 3 ports, 2,5 GHz Dual Core i7). First two sets were generated using commands:
```bash
watch -c 'echo $RANDOM >> bash1.txt';
watch -c 'echo $RANDOM >> bash2.txt';
```
There were generated parallel, in two separate tmux sessions.

[bash1.txt](./bash1.txt)

[bash2.txt](./bash2.txt)


The following Python script generated the third set:
```python
from random import random

for x in range(0,10000):
    print(str(random()*32767).split('.')[0])
```

[python.txt](./python.txt)


In each file, let's subtract each number from the previous one. Next, we will count the frequencies of each subtraction:
```bash
cat python.txt | awk '{print prev-$1 ;prev=$1}' | sort | uniq -c | sed -e 's/^ *//' | sort -t ' '  -k 1rn,2rn > python_subtraction.txt
cat bash1.txt | awk '{print prev-$1 ;prev=$1}' | sort | uniq -c | sed -e 's/^ *//' | sort -t ' '  -k 1rn,2rn > bash1_subtraction.txt
cat bash2.txt | awk '{print prev-$1 ;prev=$1}' | sort | uniq -c | sed -e 's/^ *//' | sort -t ' '  -k 1rn,2rn > bash2_subtraction.txt
```

Results:

* Columns 1-2: bash1_subtraction.txt
* Columns 3-4: bash2_subtraction.txt
* Columns 5-6: python_subtraction.txt

freq|number|freq|number|freq|number
----|------|----|------|----|--------
4725|-2726|4900|-2726|4|-1322
922|-2725|951|-2725|4|-9356
802|13204|855|13204|4|9461
553|-19564|549|-19564|3|-10270
447|30042|417|30042|3|-10636
359|14112|365|14112|3|-13308
338|14113|361|14113|3|-13866
277|-18656|257|-18655|3|-14735
259|-1817|257|-18656|3|-1700
236|-18655|159|13203|3|-17671
168|-3634|156|-3634|3|-1794
142|-3635|145|-3635|3|-184
132|13203|120|-19565|3|-2186
89|-19565|84|30043|3|-2222
76|-1818|59|12295|3|-2254
73|30043|51|-4543|3|-3012
53|12295|32|-20473|3|-3020
48|-4543|25|29134|3|-3041
31|-20473|24|-1817|3|-3215
21|11386|19|10478|3|-326
