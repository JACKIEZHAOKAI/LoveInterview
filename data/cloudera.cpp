// ##############################################
//  11/5    第一轮电面 
// 虽然最后时间不够就连代码都没有compile    但是奇迹般的过了而且是面印度佬     
// 1    开始自我介绍对CS的passion非常强    而且展现skill set 很全面
// 2    做题的时候思路很清晰    保持代码结构清晰    在中间发现问题及时代码重构   

// LeecCode 题库就七道题        但是就没有问leetcode题目
// https://leetcode.com/company/cloudera/

// EX
// // Longest repeated characters, order (left to right) preserved
// //-----------------------------------
// // aaabbcbaacc -> aaabbcc 
// // bbbaacbbaaaa -> bbbcaaaa

// 给出的解法    用 hashmap
// // key pair<value,pos>   key char value LongesContinuous 
// // b <3, 0>
// // c <1 ,2>
// // b length =2 
// // a length 4
// // a <4, 3> 
// // \0


#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

string  LRC(const string& inputString){
    unordered_map<char, pair<int,int>> map;
   
   
    char tempChar ='';
    int tempLength=0;
    int pos=0; 
    
    pair<int,int> firstelem(0,0); 
    map[inputString[0]] = firstelem;
    
        
    for(int i =0; i < inputString.length()-1; ++i){

        if (inputString[i] == inputString[i+1]){
            tempChar = inputString[i];
            tempLength ++;
        }        
        else{ // when char is changed, manipulate the map
            pos ++;
            // exist in the map
            if ( map.find([inputString[i+1]]) ){
                //update
                if (map[inputString[i+1]].first < tempLength ){
                    map[inputString[i+1]].first = tempLength;
                    map[inputString[i+1]].second = pos;
                    
                }
            }
            else{
                pair<int,int> tempPair(0,pos);
                //add element into map in this way 
                map[inputString[i+1]] = tempPair;
            }    
        }
        
    }
        
    string res = ""; 
    
    for (const auto& item : map)
        for (int i; i < pair.first ; ++i )
              res+=c;
    return res;
}

int main(){
    
    const string test1 = "aaabbbcccaaaaa";
    
    string res = LRC(test1);
    
    cout << res <<endl;
    
    return 0;
}
