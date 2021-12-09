digit-gt/2 9 [0-8]
1

digit-gt/2 8 [0-7]
1

digit-gt/2 7 [0-6]
1

digit-gt/2 6 [0-5]
1

digit-gt/2 5 [0-4]
1

digit-gt/2 4 [0-3]
1

digit-gt/2 3 [0-2]
1

digit-gt/2 2 [01]
1

digit-gt/2 1 0
1

digit-gt/2 \d \d
0

digit-eq/2 (\d) \1
1

digit-eq/2 \d \d
0

order/3 (\d) (\d) 1
\2\1

order/3 (\d) (\d) 0
\1\2

order/2 (\d) (\d)
order/3 \1 \2 digit-gt/2 \2 \1

rshift/1 (\d+)\d
\1

rshift/1 \d
0

last/1 \d*(\d)
\1

add/5 (\d*X) (\d+) (\d+) 00 0
add/4 0\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 00 1
add/4 1\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 10 0
add/4 1\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 10 1
add/4 2\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 11 0
add/4 2\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 11 1
add/4 3\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 20 0
add/4 2\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 20 1
add/4 3\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 21 0
add/4 3\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 21 1
add/4 4\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 22 0
add/4 4\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 22 1
add/4 5\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 30 0
add/4 3\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 30 1
add/4 4\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 31 0
add/4 4\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 31 1
add/4 5\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 32 0
add/4 5\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 32 1
add/4 6\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 33 0
add/4 6\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 33 1
add/4 7\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 40 0
add/4 4\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 40 1
add/4 5\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 41 0
add/4 5\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 41 1
add/4 6\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 42 0
add/4 6\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 42 1
add/4 7\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 43 0
add/4 7\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 43 1
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 44 0
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 44 1
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 50 0
add/4 5\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 50 1
add/4 6\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 51 0
add/4 6\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 51 1
add/4 7\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 52 0
add/4 7\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 52 1
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 53 0
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 53 1
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 54 0
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 54 1
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 55 0
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 55 1
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 60 0
add/4 6\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 60 1
add/4 7\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 61 0
add/4 7\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 61 1
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 62 0
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 62 1
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 63 0
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 63 1
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 64 0
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 64 1
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 65 0
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 65 1
add/4 2\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 66 0
add/4 2\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 66 1
add/4 3\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 70 0
add/4 7\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 70 1
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 71 0
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 71 1
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 72 0
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 72 1
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 73 0
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 73 1
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 74 0
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 74 1
add/4 2\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 75 0
add/4 2\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 75 1
add/4 3\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 76 0
add/4 3\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 76 1
add/4 4\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 77 0
add/4 4\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 77 1
add/4 5\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 80 0
add/4 8\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 80 1
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 81 0
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 81 1
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 82 0
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 82 1
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 83 0
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 83 1
add/4 2\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 84 0
add/4 2\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 84 1
add/4 3\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 85 0
add/4 3\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 85 1
add/4 4\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 86 0
add/4 4\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 86 1
add/4 5\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 87 0
add/4 5\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 87 1
add/4 6\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 88 0
add/4 6\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 88 1
add/4 7\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 90 0
add/4 9\1 \2 \3 0

add/5 (\d*X) (\d+) (\d+) 90 1
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 91 0
add/4 0\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 91 1
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 92 0
add/4 1\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 92 1
add/4 2\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 93 0
add/4 2\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 93 1
add/4 3\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 94 0
add/4 3\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 94 1
add/4 4\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 95 0
add/4 4\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 95 1
add/4 5\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 96 0
add/4 5\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 96 1
add/4 6\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 97 0
add/4 6\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 97 1
add/4 7\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 98 0
add/4 7\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 98 1
add/4 8\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 99 0
add/4 8\1 \2 \3 1

add/5 (\d*X) (\d+) (\d+) 99 1
add/4 9\1 \2 \3 1

add/4 X 0 0 0
0

add/4 (\d+)X 0 0 0
\1

add/4 (\d+)X 0 0 1
1\1

add/4 (\d*X) (\d+) (\d+) (\d)
add/5 \1 rshift/1 \2 rshift/1 \3 order/2 last/1 \2 last/1 \3 \4

add/2 (\d+) (\d+)
add/4 X \1 \2 0

counters-inc/6 1 (\d+) (\d+) (\d+) (\d+) (\d+)
add/2 1 \1 \2 \3 \4 \5

counters-inc/6 2 (\d+) (\d+) (\d+) (\d+) (\d+)
\1 add/2 1 \2 \3 \4 \5

counters-inc/6 3 (\d+) (\d+) (\d+) (\d+) (\d+)
\1 \2 add/2 1 \3 \4 \5

counters-inc/6 4 (\d+) (\d+) (\d+) (\d+) (\d+)
\1 \2 \3 add/2 1 \4 \5

counters-inc/6 5 (\d+) (\d+) (\d+) (\d+) (\d+)
\1 \2 \3 \4 add/2 1 \5

count/6 \$ (\d+ \d+ \d+ \d+ \d+)
0 \1 0 0 0

count/6 (\d),(\S+) (\d+ \d+ \d+ \d+ \d+)
count/6 \2 counters-inc/6 \1 \3

count/1 ([\d,]+)
count/6 \1,$ 0 0 0 0 0

add-all/x (\d+) (\d+) (\d+)
add-all/x add/2 \1 \2 \3

add-all/x (\d+) (\d+) ((?:\d+ )+)(\d+)
add-all/x add/2 \1 \2 \3\4

add-all/x (\d+) (\d+)
add/2 \1 \2

sim/9 (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)
\2 \3 \4 \5 \6 \7 add/2 \8 \1 \9 \1

iter-sim/11 (\d+) \1 (\d+ \d+ \d+ \d+ \d+ \d+ \d+ \d+ \d+)
\2

iter-sim/11 (\d+) (\d+) (\d+ \d+ \d+ \d+ \d+ \d+ \d+ \d+ \d+)
iter-sim/11 \1 add/2 1 \2 sim/9 \3

iter-sim/10 (\d+) (\d+ \d+ \d+ \d+ \d+ \d+ \d+ \d+ \d+)
iter-sim/11 \1 0 \2

solve/2 (\d+) ([\d,]+)
add-all/x iter-sim/10 \1 count/1 \2

part1/1 ([\d,]+)
solve/2 80 \1

part2/1 ([\d,]+)
solve/2 256 \1