g++ -c *.cc --std=c++17
g++ *.o -o result
rm *.o
./result > Result.txt