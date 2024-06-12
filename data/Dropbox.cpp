// dropbox题目基本不变    但是followUp很难

// 题库精炼    

// Hiring process:
// 1    coding challenge     
// 2    on campus / Phone interview
// 3    on-site 

// ##########################################################
// #    11 / 9  10点      Dropbox  phone interview— failed

// # Find Assessable files in a Linux Tree Structure System

// 知识点：    Tree    buildTree     bfs     unordered_map    
// Assumption：  folders 第一个是root    在之后的内容基于之前built的tree    

// Given a list folders        vector of pairs 
// folders = { {“A”,” “} , {“B”,”A”}, {“C”,”A”}. {“D”, “C”}, {“E”,”C”}… }
// and given an access list of folders 
// access  =     {“B”, ”D”}

// implement a API         bool   hasAccess (string name)
// for example       hasAccess (“A”) ==  True       hasAccess (“B”)  == false 

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
/*
Follow up questions:

    1. Imagine you are given a real file system, how will you search files? DFS or BFS ?
        In general, BFS will use more memory then DFS. 
        However BFS can take advantage of the locality of files in inside directories,
        and therefore will probably be faster

    2. If the file content is very large (GB level), how will you modify your solution?
        In a real life solution we will not hash the entire file content, since it's not practical. 
        Instead we will first map all the files according to size. 
        Files with different sizes are guaranteed to be different. 
        We will than hash a small part of the files with equal sizes 
        (using MD5 for example). Only if the md5 is the same, we will compare the files byte by byte

    3. If you can only read the file by 1kb each time, how will you modify your solution?
        This won't change the solution. 
        We can create the hash from the 1kb chunks,
        and then read the entire file if a full byte by byte comparison is required.

    What is the time complexity of your modified solution? What is the most time consuming part and memory consuming part of it? How to optimize?
        Time complexity is O(n^2 * k) since in worse case we might need to 
        compare every file to all others. k is the file size

    How to make sure the duplicated files you find are not false positive?
        We will use several filters to compare: File size, Hash and byte by byte comparisons.
*/


vector<vector<string>> findDuplicate(vector<string>& paths) {

	//key:unique file contain  	value: list of files having the contain
	//root/a/2.txt
    unordered_map<string, vector<string>> files;
    vector<vector<string>> result;

    //read all files under all paths, files saperates with ' '
    for (const auto& path : paths) {
        stringstream ss(path);
        string root;
        string s;
        getline(ss, root, ' ');
        while (getline(ss, s, ' ')) {
        	// file path ending with ( starts
            string fileName = root + '/' + s.substr(0, s.find('('));
            // contain inside  ( )
            string fileContent = s.substr(s.find('(') + 1, s.find(')') - s.find('(') - 1);
            //create key value pair
            files[fileContent].push_back(fileName);
        }
    }

    for (const auto& file : files) {
        if (file.second.size() > 1)
            result.push_back(file.second);
    }

    return result;
}



