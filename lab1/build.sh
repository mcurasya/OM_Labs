g++ -c *.cc
g++ *.o -o result
rm *.o
./result > logs.txt