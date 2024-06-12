技术面至少四轮。。。

深圳  滨海大厦    广州也在扩招
增值业务部，微信游戏（包括小程序游戏，小游戏开发者的开发建设，精品游戏）
工作时间 10am-8pm  根据项目组而定

其他问题：
简历相关项目问

C++ VS  Java

zookeeper   简历

// coding 16进制转十进制  string输入输出
// followUp  如果输出超过long/int 范围咋整？ String存储， int cache，进位

#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main() {
    //int a;
    //cin >> a;
    string s;
    while(cin>>s){
        cout << s <<endl;
        int bit = 0;
        int cache = 0;    // 9999 + 100 = string "1"   int 0098
                          // string + int => string
        string res = "";
        for(int i=s.length()-1; i>1;i--){
            //check digit
            if (s[i]>='0' && s[i]<='9'){
                cache += (s[i]-'0')*pow(16,bit++);     // <15*16  
            }
            else if(s[i]>='A' && s[i]<='F'){
                cache += (s[i]-'A'+10)*pow(16,bit++);
            }
            // check if overflow
            if (cache>10000){
                res += cache/10000;
                cache = cache % 10000;
            }
        }
        res =  res + to_string(cache);
        cout << res <<endl;
    }
}