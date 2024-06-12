/*	on campus 	
    Give a string test if it is palindrome 
*/
#include <iostream>
using namespace std;

void RemoveSpace(string& str){
    // To keep track of non-space character count 
    int count = 0; 
    // Traverse the given string. If current character 
    // is not space, then place it at index 'count++' 
    for (int i = 0; i<str.size(); ++i) {
        if (str[i] != ' ') {
            str[count] = str[i]; 
            count++;
        }
    }
    str.resize(count);
}
void changeToLower(string& str){
    for( int i=0; i< str.size(); ++i){
       str[i] =  tolower(str[i]);
    }
}

bool isPalindrome(string& str, bool countSpace, bool countUpper){
    if (countUpper)
        RemoveSpace(str);
    if(countUpper)
        changeToLower(str);

    int size = str.size();
    int halfSize = str.size()/2;

    for( int i=0; i< size; ++i){
        if (str[i] != str[size-i-1]){
            return false;
        }
    }   
    return true;    
}


int main(){
    string temp1 = "a BA ba ba ";
    string temp2 = "03 34 30";
    string temp3 = "28883";

    if (isPalindrome(temp1,true,true))
        printf("temp1 is palindrome\n");
    else
        printf("temp1 is NOT palindrome\n");

    if (isPalindrome(temp2,true,true))
        printf("temp2 is palindrome\n");
    else
        printf("temp2 is NOT palindrome\n");

    if (isPalindrome(temp3,false,false))
        printf("temp3 is palindrome\n");
    else
        printf("temp3 is NOT palindrome\n");
} 









