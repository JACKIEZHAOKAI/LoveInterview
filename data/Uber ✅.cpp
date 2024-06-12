'''
    ################################################   
    两轮电面   两轮easy 投的早很关键    八月底内推
    2018.9.28 一面    Remove all Comment 
    2018.10 9 二面    substring    GO代码重写C++
    ################################################   
    Intern 两轮电面
    没有固定题库    大场面试很灵活 题目完全没必要猜题
    心态和思路表述是关键   

    官网    准备内容
    https://eng.uber.com/engineering-interview/

    ################################################   
    Uber 第二轮面试题
    Karsten McMinn <karsten@uber.com>

    开始解释完题目    assumption 解释完
    面试过程一言不发    有点尴尬      
    3 min self intro +   8min法一 + 20min 法二     + follow Up 5min有点尴尬 +     5-10 min交流

    题目     check if C1 is a substring  in C2
    1    C++的 cstring find实现    要求代码越短越好    1行
        return ( c2.find(c1)>0)? true: false;

    2    C++    用index追踪比较        
            两个while loop    runtime  O(m*n )
            Arista Network面试写过一遍C的代码 哈哈

    3    follow UP 
        如何在不改变time complexity的基础上 提高效率    当C2非常大
        瞎扯一堆。。。 C++ fstream用buff 暂存？ OS level？ 完全不会 GG

    4    write code in GO  and email to k@uber.com

    ################################################   
    Uber 第一轮面试题    南大老哥            过了 
    1    踩了个坑    STL创建的所有object都是在heap
        vector<int>
        需要加强C++基础知识    面设么语言就准备该语言的基础     C++

    2    优点继续保持：实现的函数功能先
        解释如何实    有什么edge cases        不着急写
        然后    代码先搭好架构 for loop  if statement     之后再填充内容
        基本上看你的代码架构没问题就不会细看代码实现了

    题目    Remove all comment        C++ 

    ################################################   
    2017 Fall 校招
    Given a incorrect BST with two node swapped,  
    find the two node and swap them to make it a correct BST?        45mins

    Failed 经验总结：
        1    没有解释清楚思路
        2    coding没有策略  不知道从何入手  用array还是 treeNode存放呢？
                tree insert func要不要写？怎么写得完这么多
        3     testcase不知道怎么测试
'''


#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> helper(string inputString){
    
    vector<string> res;
    int index;
    string comment;
    
    //edge case total length less than 2
    if (inputString.size() <=1)
        return res;
        
    for (int i=0; i<inputString.size(); ++i){
        // check //,  stroing the string until hitting \n
        if( inputString[i] =='/' && inputString[i+1] == '/'){
            index = i;
            comment ="";
            while(inputString[index] != '\n'){
                comment+=(inputString[index]); //add char in 
                index++;
            }
            res.push_back(comment);
        }
        //check /*   */
         //store the comment until hitting */ only,  igonre /n
        else if ( inputString[i]=='/' && inputString[i+1] == '*'){
            index = i;
            comment ="";
            while( !(inputString[index] == '*' && inputString[index+1] =='/'  )){
                comment+=(inputString[index]);  //add char in 
                index++;
            }
            comment.push_back('*');
            comment.push_back('/');
            res.push_back(comment);
        }
    }
    return res; // list of comment     
}


int main() {
    int x; // trailing comments
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string inputString = R"(int main() { 
    int x; // trailing comments 
    source = "string s = "/* still a comment. */";"  //this is a comment 
    /* ********* Enter your code here. Read input from STDIN. Print output to STDOUT ****/ 
    vector<char> inputString == ""; 
    vector<string> res = helper(inputString); 
    return 0;  
    /* multiple  
    line        
    1           
    2           
    */          
    })";    
    
    vector<string> res = helper(inputString);
    for(auto item : res){
        cout << item <<endl;
    }
    
    return 0;
}




#include <iostream>
#include <string>
#include <vector>

using namespace std;

/* impl 1, implement substring in as few lines of code as possible */
/* ** anything in the c++ stdlib ** */
bool checkSubstr( string& c1,  string& c2){
   return ( c2.find(c1) == -1)? false: true;
}

bool checkSubstr2( string& c1,  string& c2){
    int index1=0;
    int index2 = 0;
    bool flag = true;
    //iterate c2, check curr char of c2 is the char in c1 start
    //if match iterate c1 from the curr char in c2.
    //else next char in c2
    while(c2[index2]!='\0'){
        if(c2[index2]  == c1[index1]){
            flag = true;
            index1 = 0;
            //interate c1
            while(c1[index1] != '\0'){
                //compare char by char 
                if(c1[index1] != c2[index1+index2]){
                    flag = false;
                    break;
                }
                index1 ++;  
            }
            if (flag)
                return true;
        }
        index2++;
    }
    
    return false;
}
        
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    /*  pass two string, check if str A is in str B 
                  needle     haystack
        substring("cow", "this is cow") => bool:true
        substring("cow", "this is dog") => bool:false
        substring("cow", "this is coows and dog") => bool:true
        
        Testcase???
        arg1, aka, needle, string
        arg2, haystack, string
        retval = boolean
        
    */
    
    string c1 = "cow";
    string c2 = "this is dog";
    string c3 = "this is cow";
    string c4 = "cow is me";
            
    if( checkSubstr2( c1, c2) ){
        cout<< "found"<<endl;
    }
    else 
    {
        cout << "not found "<<endl;
    }
    if( checkSubstr2( c1, c4) ){
        cout<< "found"<<endl;
    }
    else 
    {
        cout << "not found "<<endl;
    }
    
    return 0;
}











