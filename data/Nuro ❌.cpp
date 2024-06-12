// Nuro做外卖小车的自动驾驶，技术栈主要是C++，Python, GO，在infra平台上跑自动驾驶的算法，需要平台支持。
// 面试要求写CPP代码，python和CPP的题目会有不一样。
// 面试关是刚你毕业工作一年多的ABC小哥，和大多数进nuro的人一样感觉都是一看就是很聪明的，英语说得也很快的。（基本标配大二大厂实习）

// 题目很直观就是设计一个String的class可以实现get（） append（） length（）的API，
// 开始有点摸不清楚他的思路，时间消耗的很快，主要考察对象不光是做题，还有很多相关性的问题：

// 例如 space/time locality 为什么用array比 hashmap好？
// 例如 为什么resize array的时候不应该线性，可以用每次size成倍增加实现 append的time complexity接近O(1)
//       N/8 => N/16 => N/32 ==> 1  
// 例如 C++ array操作中新开和释放内存

#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

const int INITIAL_SIZE = 8;

class String {
public:
  // Initialize an empty string.
  String() {
      buf_ = new char[INITIAL_SIZE];
      length = 0;
      capacity = INITIAL_SIZE;
  }

  // Get the ith character (0 indexed).
  char get(int i) {
      assert(i < length && i >= 0);
      return buf_[i];
  }

  // Append c to the end of the string.
  void append(char c) {
      //check if need to resize, check if 8 16 32 64... resize
      if (length == capacity){
          capacity *= 2;
          char* new_buf_ = new char[capacity];
          for (int i=0; i < capacity; i++){
              new_buf_[i] = buf_[i];
          }
          delete buf_;    // deallocate!
          buf_ = new_buf_;  // set old buf to new one
      }
      buf_[length] = c;
      length += 1;
  }

  // Get the length of the string.
  int length() {
      return length;
  }
private:
  // Fill this in.
  char* buf_;
  int length;
  int capacity;
};

int main() {
  String s;
  s.append('c');
  assert(s.get(0) == 'c');
  assert(s.length() == 1);
  return 0;
}