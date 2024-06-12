

// 先用gettimeofday()测两个函数的运行时间，然后问了一大堆操作系统，内存之类的东西
// gettimeofday   在C语言中可以使用函数gettimeofday()函数来得到时间。它的精度可以达到微妙
// https://yq.aliyun.com/articles/17473

// 调用Ctime实现,         timeval    timezong 结构体
// 在gettimeofday()函数中tv或者tz都可以为空。如果为空则就不返回其对应的结构体。
// 函数执行成功后返回0，失败后返回-1，错误代码存于errno中。
// 使用gettimeofday()函数时，第二个参数一般都为空，因为我们一般都只是为了获得当前时间，而不用获得timezone的数值

// CTime 中定义 

struct  timeval{
       long  tv_sec;/*秒*/
       long  tv_usec;/*微妙*/
}；

 
#include<stdio.h>
#include<sys/time.h>
#include<unistd.h>

 int delay(int time)
{
    int i,j;

    for(i =0;i<time;i++)
        for(j=0;j<5000;j++)
            ;
}

int main()
{
        struct  timeval start;
        struct  timeval end;
        unsigned  long diff;

        // count time obtain itme val start and end， No need to return timezone so set to null
        gettimeofday(&start,NULL);
        delay(10);
        gettimeofday(&end,NULL);

        //diff  秒   微妙
        diff = 1000000 * (end.tv_sec-start.tv_sec)+ end.tv_usec-start.tv_usec;

        printf("thedifference %ld\n",diff);
        
        return 0;
}

///////////////////////////////////////////////////////////////////

#include <stdio.h> 

int main(int argc, char* argv[]) {
	char* string1 = "string";
	char string2[] = "string";
}

#include <stdio.h> 

/* Describe the code below */

struct s {
	double f;
	int i;
	char c[3];
	void *p;
	int x[0];
};

/*
The size of the struct is 24 
The size of the double is 8 
The size of a character array is 3 
The size of a void pointer is 8 
The size of a integer array is 0 
The size of a integer is 4 
*/
int main(int argc, char ** argv) {

	struct s temp;

	printf("The size of the struct is %d \n", sizeof(temp));

	printf("The size of the double is %d \n", sizeof(temp.f));

	printf("The size of a character array is %d \n", sizeof(temp.c));

	printf("The size of a void pointer is %d \n", sizeof(temp.p));

	printf("The size of a integer array is %d \n", sizeof(temp.x));

	printf("The size of a integer is %d \n", sizeof(temp.i));

	return 0;
}



/* What's wrong with this program? 

test2.c:3:5: error: second parameter of 'main' (argument array!!!) must
      be of type 'char **'
*/

#include <stdio.h> 

int main(int argc, char const * argv) {
	for (int i = 0; i < argc; ++i) {
		printf("%s\n", argv[i]);
	}
}


/* Can you tell me what the program will do when I run it like this:
* <prog> 1 2 3 4

➜  Desktop ./test 1 2 3 4
./test
1
2
3
4

*/


/*
Describe what two of these do, and how they're useful for debugging:


Profiling 测试性能	不同level

###	gprof  简单但是不适合内核态执行程序 函数调用次数 时间	
gprof是GNU工具之一，它在编译的时候在每个函数的出入口加入了profiling的代码，
运行时统计程序在用户态的执行信息，可以得到每个函数的调用次数，执行时间，调用关系等信息，简单易懂。
@@@@	适合于查找用户级程序的性能瓶颈，对于很多时间都在内核态执行的程序，gprof不适合。

###	 oprofile   内核信息	cache  memorys	
oprofile也是一个开源的profiling工具，它使用硬件调试寄存器来统计信息，进行profiling的开销比较小，
而且可以对内核进行profiling。它统计的信息非常的多，可以得到cache的缺失率，memory的访存信息，
分支预测错误率等等，这些信息gprof是得不到的，但是对于函数调用次数，它是不能够得到的。


###	Perf   	  随机采集和分析	 	内核源码
Perf 是内置于Linux 内核源码树中的性能剖析（profiling）工具。它基于事件采样原理，
以性能事件为基础，支持针对处理器相关性能指标与操作系统相关性能指标的性能剖析。
可用于性能瓶颈的查找与热点代码的定位。

基于硬件的采集方法，此种方法需要采用CPU中的PMU（performance monitoring unit）部件，
在特定的条件下探测性能事件是否发生以及发生的次数。

基于软件的采集方法，需要将代码内置于kernel，分布在各个功能模块中，统计和操作系统相关性能事件。






###	printf  C 函数	redirecting 重定向打印	适用于简单的函数调试

加了一个printf就能确定错误的位置，如果程序较长的话，就需要增加多个printf来打印中间结果，并且逐段去排查。

可用于调试marco函数		装逼用 	
某个C驱动模块，希望在调试时打印调试信息，而产品代码中不显示调试信息。
v1--单参数宏
#define DRV_DEBUG 1
#if DRV_DEBUG
    #define DRV_PRINT(x) printf(x)
#else
    #define DRV_PRINT(x) 
#endif




####  syslog 		log 输出	
syslog是一种工业标准的协议，可用来记录设备的日志。在UNIX系统，路由器、交换机等网络设备中，
系统日志(System Log)记录系统中任何时间发生的大小事件。管理者可以通过查看系统记录，随时掌握系统状况。

UNIX的系统日志是通过syslogd这个进程记录系统有关事件记录，也可以记录应用程序运作事件。通过适当的配置，
我们还可以实现运行syslog协议的机器间通信，通过分析这些网络行为日志，藉以追踪掌握与设备和网络有关的状况。

syslog设备依据两个重要的文件：
/etc/syslog	守护进程		和	/etc/syslog.conf配置文件。
*/



////////////////////////////// C++  code ///////////////////////////////

/*
	C 不是面向对象编程			没有class的概念
	C 的struct和cpp的	struct  不是一个东西！！！
*/


#include <stdlib.h> 
#include <stdio.h> 

class C {
public:
	void func() {
		printf("func called\n");
	}
	virtual void virtualFunc() {			// 可以之后override
		printf("virtual func called\n");
	}
};

class D : class C{
	void virtualFunc() {			// 可以之后override
		printf("hah \n");
	}

}

int main(int argc, char ** argv) {
	C * obj = NULL // new C();
	/* What does the following print? 
		seg falut if not new one 	pointing to Null 
		new C() 	*/
	obj->func();
	/* What does the following print? 
		func called */
	obj->virtualFunc();
	/* What's the difference? 

		定义一个函数为虚函数，不代表函数为不被实现的函数。
		定义他为虚函数是为了允许用基类的指针来调用子类的这个函数。

		定义一个函数为 pure virtual 纯虚函数，才代表函数没有被实现。
		virtual void virtualFunc() = 0
	*/
}


/* 
OOP的主要有三个主要的特点。
 一个是封装（Encapsulation），一个是继承（inheritance）， 一个是多态（Polymorphism）。


What's polymorphism? 
pverride 	

class B : public A 

C++多态(polymorphism)是通过虚函数来实现的，虚函数允许子类重新定义成员函数，
而子类重新定义父类的做法称为覆盖(override)，或者称为重写。


What's abstraction == encapsulation? 
hiding detail	 only provide the interface 	

*/



#include <cstdlib> 
#include <ctime> 
#include <sys/time.h> 
#include <iostream> 
#include <cstdio> 
using namespace std;

/* What do this do? */
int a(unsigned int i) {
	int c = 0;
	while (i) {
		if (i & 1) { c++; }
		i >>= 1;
	}
	return c;
}

/* What does this one do? */

int b(unsigned int i) {
	static unsigned char n[] = { 0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4 };
	int c = 0;
	while (i) {
		c += n[i & 15];
		i >>= 4;
	}
	return c;
}
#include <algorithm> 
#include <stdio.h> 
#include <string.h> 
#include <string> 

using namespace std;


std::string::iterator contains(char c, string s1) {
	std::string::iterator i = std::find(s1.begin(), s1.end(), c);
	if (i != s1.end())
		return i;
	else
		return null;
}



int anagram(const string s1, const string s2) {
	for (int i = 0; i < s1.size(); i++) {
		std::string::iterator i =, s2.find(s1[i]);
		if (i != s2.end())
			s2.erase(i);
		else
			return false;
	}
	return s2.size() == 0;
}

int main(int argc, char *argv[]) {
	printf("%d", anagram(argv[1], argv[2]));
}

F
/ \
/ \
D M
/ \ / \
B E L P
/ \ / \
A C H S
/ \
R T

In - order traversal :
A->B->C->D->E->F->H->L->M - P->R->S->T

Requirement :
Write a function(pseudo - code is fine) that given a starting node, advances to the next in - order node in a binary tree.
Please also provide a data - structure definition of a node.


struct node
{
};


node *next_node(node *current)
{
	node *next;

	/* current - any node in the tree, advance to next node */

	return next;
}


#include <stdio.h> 
#include <stdlib.h> 
#include <assert.h> 
#include <string.h> 
/*
vercmp compares two software version strings and returns the following:
if v1 > v2 : return 1
if v1 == v2 : return 0
if v1 < v2 : return -1
input strings are in the form "1.0.3", "2.10", "6.0.0.3", etc...
"1.0" is considered bigger than "1" and "1.10" is greater than "1.2"

很简单  looping 过程中无视点	变成 numerical 比较大小	
*/
int vercmp(char * v1, char * v2) {
 	//  vnum stores each numeric part of version 
    int vnum1 = 0, vnum2 = 0; 
  
    //  loop untill both string are processed 
    for (int i=0,j=0 ; (i<v1.length() || j<v2.length()); i++, j++ ) 
    { 
        //  storing numeric part of version 1 in vnum1 
        while (i < v1.length() && v1[i] != '.') 
        { 
            vnum1 = vnum1 * 10 + (v1[i] - '0'); 
            i++; 
        } 
  
        //  storing numeric part of version 2 in vnum2 
        while (j < v2.length() && v2[j] != '.') 
        { 
            vnum2 = vnum2 * 10 + (v2[j] - '0'); 
            j++; 
        } 
  
        if (vnum1 > vnum2) 
            return 1; 
        if (vnum2 > vnum1) 
            return -1; 
  
        //  if equal, reset variables and go for next numeric 
        // part 
        vnum1 = vnum2 = 0; 
    } 
    return 0; 
}

int main() {
	assert(vercmp("1.1", "1.0") == 1);
	assert(vercmp("1.0", "1.1") == -1);
	assert(vercmp("1.0", "1.0") == 0);
	assert(vercmp("1", "1.0") == -1);
	assert(vercmp("1.0", "1") == 1);
	return 0;
}

/*		网络协议

Describe in 5 minutes or less what ！！！one of these protocols is :

###	DHCP	
DHCP 主要分为两部分： 地址的管理 和 配置信息的传递 
+ 地址管理： 地址管理处理IP‘地址的动态分配、向客户端提供地址租约 
+ 配置信息的传递： 包含DHCP报文格式、状态机


DHCP服务器提供了三种IP分配方式：自动分配(Automatic allocation)、
手动分配  和  动态分配（Dynamic Allocation）。

 
DHCP基于UDP/IP传输。！！！！

　在网络中，我们把主机分为两大类，服务器主机和客户端主机， 
+ 服务器主机： 一般采用手动配置 
+ 客户端主机： 一般采用动态获取 
服务器一般采用手动配置，而客户端一般动态获取。主要基于以下原因： 
1. 客户主机比服务主机移动更频繁 
2. 服务主机需要提供更可靠的服务，其配置信息应该减少对其他系统/主机的依赖 
3. 客户主机比服务主机的数量要多得多。 
4. 客户主机使用者的网络配置知识比服务主机的使用者低



#####BGP	Border Gateway Protocol, 边界网关协议	
路由选择协议	去中心化		维护IP路由表前缀实现自制系统
routing table 路由表存储着指向特定网络地址的路径


######## STP生成树协议（英语：Spanning Tree Protocol，STP），
是一种工作在OSI网络模型中的第二层(数据链路层)的通信协议，
基本应用是防止交换机冗余链路产生的环路. 用于确保以太网中无环路的逻辑拓扑结构. 
从而避免了广播风暴,大量占用交换机的资源.

*/

/*		数据结构
Pick one of these data structures and tell me everything you know about it :

RB - tree      4 rule 

Avl Tree    more strict 	by height 	
All RB are AVL 

###	Trie			TRIES 	auto complete / spell check
class TrieNode {
    public TrieNode[] links;
    public final int R = 26;
    public boolean isEnd;
    public TrieNode() { links = new TrieNode[R];}
}


Or describe a data structure that can store a set of integers.

If you're not familiar with any of the above, tell me what you know about 
one of these :

Bit vector
Binary tree
std::vector
Doubly Linked List

*/

/*		

#!/usr/bin/python 

# Write a program to  sum up the Nth column of integers in a file that has
# M rows in it.

*/
def sumColumn(m, column, rows):
    total = 0
    for row in range(len(rows)):
        total += m[row][column]
    return total


/*   网络  分析工具
What do these tools do ?

#####	ping   Unix和Linux系统下的一个命令。ping也属于一个通信协议，
是TCP/IP协议的一部分。利用“ping”命令可以检查网络是否连通，

#####   wireshark   是一个免费开源的网上数据包分析软件。
网上数据包分析软件的功能是截取网上数据包，并尽可能显示出最为详细的网上数据包数据

#####	ifconfig		ifconfig是linux中用于显示或配置网络设备

#####	netstat
Netstat是在内核中访问网络连接状态及其相关信息的程序，它能提供TCP连接，TCP和UDP监听，进程内存管理的相关报告。
*/



/*
/////////////////////////////////////////////////////////////
What seven system calls do you use to implement a TCP server ?


Client 						Server
						socket – make socket
						bind – assign address
						listen – listen for clients
soket – make socket
bind – assign address (optional)
connet – connect to listening socket
						accept – accept connection
write – send data 		read – receive data
read – receive data 	write – send data

/////////////////////////////////////////////////////////////


/**		链表		
* Given a linked list of the structure:
print out the fibonacci nodes e.g. the 1st, 2nd, 3rd, 5th, 8th... nodes
up until the list ends.
*/

// Function to print first n Fibonacci Numbers 
void printFibonacciNumbers(int n) 
{ 
    int f1 = 0, f2 = 1, i; 
  
    if (n < 1) 
        return; 
  
    for (i = 1; i <= n; i++) 
    { 
        printf("%d ", f2); 
        int next = f1 + f2; 
        f1 = f2; 
        f2 = next; 
    } 

} 

///////////////////// 		链表			/////////////////////////////
//  remove duplicate numbers from linked list

/* Function to remove duplicates from a 
   unsorted linked list */
void removeDuplicates(struct Node *start) 
{ 
    // Hash to store seen values 
    unordered_set<int> seen; 
  
    /* Pick elements one by one */
    struct Node *curr = start; 
    struct Node *prev = NULL; 

    while (curr != NULL) 
    { 
        // If current value is seen before 
        if (seen.find(curr->data) != seen.end()) 
        { 
           prev->next = curr->next; 
           delete (curr); 
        } 
        else
        { 
           seen.insert(curr->data); 
           prev = curr; 
        } 
        //move next
        curr = prev->next; 
    } 
} 




//	Implement a queue using two stacks
# implement stacks using plain lists with push and pop functions
Stack1 = []
Stack2 = []

# implement enqueue method by using only stacks
# and the append and pop functions

def Enqueue(element):
  Stack1.append(element)
  

# implement dequeue method by pushing all elements
# from stack 1 into stack 2, which reverses the order
# and then popping from stack 2


def Dequeue():
  if len(Stack2) == 0:
    if len(Stack1) == 0:
      return 'Cannot dequeue because queue is empty'
    while len(Stack1) > 0:
      p = Stack1.pop()
      Stack2.append(p)
  return Stack2.pop()



/////////////////////////////////////////////////////////////


#include <stdio.h> 
#include <stdlib.h> 
#include "list.h" 

struct node {
	int val;
	struct node* next;
};

int main(int argc, char** argv) {
	if (argc != 2) {
		printf("usage fib num --you gave %d args\n", argc - 1);
		exit(0);
	}
	int nodes = atoi(argv[1]);

	if (nodes < 1) {
		printf("num must be a positive number --you gave %d\n", nodes);
	}

	struct node* list = createList(nodes);
	// ... 
	freeList(list, nodes);
}

# include <stdlib.h>
#include <assert.h> 
struct node {
	int val;
	struct node* next;
};

struct node* createList(int nodes);
struct node* freeList(struct node* list, int nodes);

struct node* createList(int nodes) {
	int i = 0;
	struct node* list = (struct node*) malloc(sizeof(struct node) * nodes);
	
	assert(list);
	
	for (i = nodes - 1; i >= 0; --i) {
		list[i].val = (nodes - i) - 1;
		list[i].next = list + (i - 1);
	}
	list[0].next = NULL;
	return &list[nodes - 1];
}

struct node* freeList(struct node* list, int nodes) {
	free(&list[1 - nodes]);
}


/////////////////////////////////////////////////////////////
#include <stdio.h> 
#include <assert.h> 
#include <stdbool.h> 

extern bool isPalindrome(const char * str){

    int l = 0; 
    int h = strlen(str) - 1; 
  
    while (h > l) 
    { 
        if (str[l++] != str[h--]) 
        { 
          	return false;
        } 
    } 
    return true;
} 



/////////////////////////////////////////////////////////////

#include "caesar.h" 
#include <stdlib.h> 

char rotate(const char in, char pivot, int offset)
{
	return pivot + (in - pivot + offset) % 26;
}

void caesar(const char *in, char *outbuf, int offset)
{
	int i;
	char *out = outbuf;
	for (; *in; ++in, ++out) {
		if (*in >= 'A' && *in <= 'Z')
			*out = rotate(*in, 'A', offset);
		else if (*in >= 'a' && *in <= 'z')
			*out = rotate(*in, 'a', offset);
		else
			*out = *in;
	}
	*out = 0;
}


#include "caesar.h" 
#include <stdlib.h> 
#include <stdio.h> 

int  main(int argc, char *argv[])
{
	char *buf = strdup(argv[1]);
	caesar(buf, buf, 13);
	printf("%s\n", buf);
	free(buf);
	return 0;
}




/////////////////////////////////////////////////////////////


struct Tree {
	struct Tree * left; // for bst, check all nodes are less than parent 
	struct Tree * right; // for bst, check all nodes are greater than parent 
	int value;
}


// 判断是不是二叉树	递归		

bool isBst(Tree * tr) {
	return helpIsBst(tr, INT_MIN, INT_MAX);
}


bool helpIsBst(Tree * root, int min, int max) {
	if (root == NULL) return true;

	if (root->value < min || root->value > max)  
	     return false;  

	return    // node 没有重复
	    isBSTUtil(root->left, min, root->value-1) &&  
	    isBSTUtil(root->right, root->value+1, max);
}

Example BST :
*
* 8
* / \
* 4 12
* / \ / \
* 1 7 11 20
* /



/////////////////////////////////////////////////////////////
struct node {
	int value;
	struct node *left, *right, *parent;
}

/* print the bst in-order */
void printBst(struct node *n) {
	if(!root)
		return;
	printInOrder(root->left);
	printf( " %d ", root->value );
	printInOrder(root->right);
}


struct node * minValue(struct node* node) { 
  struct node* current = node; 
   
  /* loop down to find the leftmost leaf */
  while (current->left != NULL) { 
    current = current->left; 
  } 
  return current; 
} 


struct node * inOrderSuccessor(struct node *root, struct node *n) 
{ 
  // step 1 of the above algorithm  
  if( n->right != NULL ) 
    return minValue(n->right); 	/// call find min 
  
  // step 2 of the above algorithm 
  struct node *p = n->parent; 
  while(p != NULL && n == p->right) 
  { 
     n = p; 
     p = p->parent; 
  } 
  return p; 
} 


void foo(struct node *root) {
	for (struct node * n = findMin(root); n; n = findNext(n)) {
		printf("%d ", n->value);
	}
}

#include <cstdio> 

// 10 
// / \ 
// 5 16 
// / \ / \ 
// 3 11 14 17 

struct node {
	int value;
	node * left;
	node * right;
	node * parent;

	node(int value, node * left, node * right, node * parent = NULL) : value(value), left(left), right(right), parent(parent) {}
};


// Test functions 

void connect_parents(node * n, node * parent) {
	if (n) {
		n->parent = parent;
		connect_parents(n->left, n);
		connect_parents(n->right, n);
	}
}

node * construct_tree() {
	node * root = new node(
		10,
		new node(5,
			new node(3, NULL, NULL),
			new node(9, NULL, NULL)),
		new node(16,
			new node(14, NULL, NULL),
			new node(17, NULL, NULL)));
	connect_parents(root, NULL);
	return root;
}

int main() {
	node * root = construct_tree();
	// for( node * n = find_min( root ); n; n = find_next( n ) ) { 
	// printf( "%d\n", n->value ); 
	return 0;
}



// 1. Create account for interviewee
// $ tempaccount <username>

// 2. Login to recruit.arista.com as interviewee
// $ ssh username@recruit.arista.com # passwd = aristarecruit

// 3. Install interview questions into temp account
// $ cp ~bterrell / screeningQuestions.gz .
// $ tar xvfz screeningQuestions.gz
// $ rm screeningQuestions.gz

// 4. Start tmux on my shell with two panes
// $ cp ~bterrell / .tmux.conf ~/ .
// $ tmux new - s interview
// - ctrl + \, "-" to split panes


// 5. Meet with interviewee(or telecon)
// $ ssh username@recruit.arista.com # passwd = aristarecruit
// $ tmux attach - t interview" 









