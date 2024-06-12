# 一轮PM，一轮Mgr， 一轮 system，两轮 SDE coding
# 这次有tm gpt的加持，加上这两个月的变化，极度自信，面试效果非常好，左手gpt，右手面试台

# question Given an integer array nums, find the subarray with the largest sum, and return its sum.


############################################################
# 11-26-2022    店面 ebay Core AI，面我的这个tm也是搞笑 升了mgr想要我
############################################################# 
'''
    Core AI
        7-8 yr ML platform team to train model
    
    Goal:
        Ebay life commos
        provide REST gateway service LLM, onboard llam2, fine tuning the existing model
        Azure OpenAI cloud => Ebay cloud (API, scalbility)
        
        Future, 
            Add more domain service to the ML platform team
            Add more model, ex Hugging face

    # https://pages.ebay.com.au/eBayLife/index.html
    # https://innovation.ebayinc.com/tech/
'''
# #   API platform fashion 
def merge_intervals(intervals):
    
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])

    return merged
# test case
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [4, 5]]
# intervals = [[1, 4], [0, 4]]
# intervals = [[1, 4], [0, 1]]
# intervals = [[1, 4], [0, 0]]
# intervals = [[1, 4], [0, 2], [3, 5]]

# Merge the intervals
merged_intervals = merge_intervals(intervals)

# Output the result
print(merged_intervals)


############################################################
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    min_heap = []

    # Add the head of each linked list to the min-heap
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, i))

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, i = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next

        if lists[i].next:
            lists[i] = lists[i].next
            heapq.heappush(min_heap, (lists[i].val, i))

    return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Example usage:
# lists = [
#     list_to_linked_list([1, 4, 5]),
#     list_to_linked_list([1, 3, 4]),
#     list_to_linked_list([2, 6])
# ]

# lists = [
#     list_to_linked_list([1, 4, 5]),
#     list_to_linked_list([1, 3, 4]),
#     list_to_linked_list([2, 6])
# ]

lists = [
    list_to_linked_list([7, 8]),
    list_to_linked_list([1, 4]),
]

result = merge_k_sorted_lists(lists)
print(linked_list_to_list(result))



############################################################
# VO2  mgr面
# goal: migrate to internal model under ebay domain,
# R&D 70%, 20% support, 10% meeting

############################################################

# vector DB, AGI , RAG (Retrieval-Augmented Generation)

# how to work with auto scaling team? provide scalibility of AI ML, new use case

# want to build own LLM to support ebay domain, ask questions to mgr

# real time orchestration service? failure of connection cross multi service ?

'''
STAR 的食用方法！！！
    # Situation
    #     Begin by setting the context. Describe a scenario where you were faced with the need to adopt or explore new technology. 
    #     This could be a project requirement, a new trend in your industry, or a personal interest in staying current with emerging technologies.

    # Task
    #     Explain the specific challenge or objective you were facing. Was it to improve efficiency, solve a specific problem, 
    #     or innovate within your role or project? Detail what made this technology adoption significant to your task.

    # Action
    #     This is where you delve into the steps you took to approach the new technology. Break this down into key actions:

        # Research
        #     Describe how you conducted initial research to understand the technology's capabilities, limitations, 
        #     and how it could be applied to your needs. Mention any specific resources you found helpful, such as documentation, forums, online courses, or communities.

        # Evaluation: Talk about how you evaluated the technology's fit for your project or goals. 
        # This could include criteria like scalability, performance, compatibility with existing systems, and cost-effectiveness.

        # Learning and Skill Acquisition: Share your strategy for learning the new technology. 
        # Did you set aside dedicated time for learning, use specific projects for hands-on experience, or collaborate with others to deepen your understanding?

        # Implementation: Discuss how you applied the new technology to your task. Highlight any prototypes, pilots, 
        # or projects where you utilized the technology. Emphasize your adaptability and problem-solving skills throughout this process.

        # Feedback and Iteration: Explain how you gathered feedback on your initial implementation and iterated on your approach. This could involve user feedback, performance metrics, or peer reviews.

    # Result
    #   Conclude with the outcomes of adopting the new technology. Focus on both the direct results, such as enhanced performance, 
    # cost savings, or improved user satisfaction, and indirect benefits, such as personal growth, team skill enhancement, or fostering a culture of innovation.

'''

'''
# how to approach new tech? BQ quesution 
    Example Response
        "In my previous role, we were facing significant challenges with our legacy system's scalability and performance. 
        I identified a new technology, XYZ, that promised to address these issues. After researching and discussing with my team, 
        I led a pilot project to integrate XYZ into our workflow. This involved self-study, attending workshops, and collaborating closely with the vendor. 
        The implementation resulted in a 40% improvement in processing times and a reduction in operational costs by 20%. Personally, 
        it was a rewarding experience that bolstered my confidence in leading tech adoption efforts, and it encouraged my team to proactively seek innovative solutions."
'''

'''
how to prioritize multi task?

    "Last quarter, I was tasked with leading a major project deadline while simultaneously handling daily responsibilities and an unexpected client request. 

    Recognizing the challenge, I first categorized tasks by urgency and importance. 
    I used a digital project management tool to visualize deadlines and dependencies, which helped in allocating my time effectively. 
    I communicated openly with my team and stakeholders about realistic deadlines, redistributing some tasks to leverage my team’s strengths better.

    To manage my focus, I scheduled deep work sessions for the most challenging tasks, ensuring progress on the project. 
    When an urgent client request came in, I assessed its impact and negotiated a slight deadline extension that satisfied all parties involved without compromising our project timeline.

    As a result, we met our project deadline with high praise from the client and stakeholders. 
    This experience reinforced the importance of flexibility, clear communication, and the strategic use of tools in managing multiple tasks. 
    It also highlighted the value of trusting my team, as delegation was key to our success."
'''


############################################################
# VO3 印度老b Staff 面 SD
############################################################
# Web Crawler and data strage challenge

# visit a web, how to know if umbralla

# how deduplicate

# Implement a Data Structure for Storing Unique Records IF data large how?


'''
    system design web scraping for dress, 
    Pipeline which cleans the content
    write this clean data into DB

For a streamlined system designed for web scraping dress data, processing it, and storing it in a database, the key components include:

    Web Scraper: Automated tools that navigate web pages to extract dress-related information. Utilizes libraries like Scrapy or Beautiful Soup.

    Content Cleaning and Processing Pipeline: A series of steps to clean, validate, and format the scraped data. Involves normalization, deduplication, and validation processes to ensure data quality.

    Database: Stores the cleaned and processed data. Can be SQL (e.g., PostgreSQL, MySQL) for structured query capabilities or NoSQL (e.g., MongoDB) for flexible schema design.

    Message Queue/Broker (Optional but Recommended): Manages data flow between the scraper and processing pipeline, enhancing system resilience and scalability. Examples include RabbitMQ or Kafka.

'''


############################################################
# VO4 中国哥 senior？
############################################################
# ech challenge transition from monotolic to microservice,  example databse
    # Database Decoupling: Just as you orchestrated AWS-related infrastructure resources through REST APIs , consider decoupling microservices and their databases. This may involve creating APIs that abstract the database interactions, allowing services to remain database-agnostic.

    # Data Consistency and Transactions: In a microservices architecture, maintaining data consistency across services becomes more complex. Drawing from your work on enhancing transaction management , implement strategies like Saga patterns for managing distributed data consistency and compensating transactions.

    # Database Schema Migration: Transitioning to microservices may require schema changes. Use tools and practices for database versioning and migrations, ensuring seamless transitions as your microservices evolve.

    # Data Replication and Synchronization: Some data may need to be shared or synchronized across microservices. Use event-driven architectures, similar to the message bus or event streams you might have used at VMware, to propagate data changes asynchronously.

    # Service-Specific Data Stores: Not all microservices require the same type of database (SQL vs. NoSQL). Choose the most appropriate data store based on the service's requirements, taking advantage of the flexibility microservices offer.

# how to handle traffic of DB

    # 1. Database Pooling
    # Use connection pooling to minimize the overhead associated with establishing connections to the database. Connection pooling allows a pool of reusable connections to be maintained, reducing the time and resources needed to establish new connections for each request.

    # 2. Read-Write Splitting
    # Separate read and write operations to different database instances. This can be particularly effective if your application's workload is read-heavy. You can direct read queries to read replicas and write queries to the primary database, thereby distributing the load and improving performance.

    # 3. Caching
    # Implement caching to reduce the number of direct database calls required for frequently accessed data. Caches can be maintained at various levels, including the application layer or through distributed caching systems. Caching read-heavy and relatively static data can significantly reduce database load.

    # 4. Database Sharding
    # Consider sharding your database to distribute data across multiple databases or servers, each handling a subset of the data. Sharding can help scale the database horizontally and manage large volumes of traffic by reducing the load on any single database server.

# multi threading api?
    # Asynchronous Programming Models: Utilize asynchronous programming models provided by your programming language or framework. For example, in Java, you can use CompletableFuture to execute asynchronous computations. In Python, you can use asyncio for asynchronous programming.

    # Thread Pool Management: Instead of creating new threads for each task, use a thread pool to manage a pool of worker threads. This helps limit the number of concurrent threads, reducing overhead and improving resource management. Most modern web frameworks and languages provide utilities for thread pool management.

    # Task Queuing: Implement a task queue that holds tasks to be processed by worker threads. This decouples task submission from task execution and helps manage load under high traffic.

    # Error Handling and Monitoring: Ensure robust error handling and monitoring for multi-threaded operations. Keep track of thread execution, handle exceptions gracefully, and monitor thread health and performance metrics.

# kalfka if it goes down, event how, from recover 

# flink?  coreAI组常用工具！！！
    # Apache Flink is a powerful stream processing framework that enables the processing of unbounded and bounded data streams with ease. 
    # It is designed to run in all common cluster environments, perform computations at in-memory speed, and at any scale

    # Core Concepts of Flink
        # DataStream API: Flink's DataStream API allows for the processing of real-time streaming data. It supports time windowing, event-time processing, and state management, making it ideal for applications that require complex time-based data computations.
        # DataSet API: For batch processing, Flink offers the DataSet API, which is designed for bounded data sets. This allows for efficient batch processing, similar to how you might use Apache Hadoop, but with more flexibility and better performance.
        # Stateful Computations: Flink is designed to handle stateful computations across streams. Its fault tolerance mechanism ensures that state is consistently maintained across stream processing nodes, even in the event of failures.
        # Event Time Processing: Flink supports event time processing, which allows you to process events based on the time they actually occurred, rather than the time they are processed by the system. This is crucial for accurate analytics on real-time streams.

    # Integrating Flink into Microservices Architecture
        # Given your role in transitioning VMware's systems to a microservices-based architecture, integrating Flink can enhance your system's capability to process data streams in real-time, offering insights and operational capabilities that are reactive to the current state of data.
        # Real-time Analytics: Use Flink to process data streams for real-time analytics, enabling your microservices to react to data changes instantaneously. This is particularly useful for applications that require dashboard updates, real-time monitoring, or instant decision-making based on streaming data.
        # Event-driven Microservices: Build event-driven architectures where microservices communicate through events. Flink can process these events in real-time, enabling complex event chaining, event sourcing, and CQRS patterns.
        # Scalability: Leverage Flink's scalability to handle varying loads of streaming data. Flink can scale out to handle massive streams of data across a cluster, making it ideal for microservices architectures that need to scale based on demand.

    # Best Practices for Using Flink
        # State Management: Utilize Flink's state management features to keep track of the computation state in case of node failures. This ensures that your stream processing jobs can recover from failures without losing state.
        # Watermarking and Windowing: Implement watermarking to handle out-of-order events in your stream processing. Use Flink's windowing functions to aggregate or process data in fixed or dynamic time windows.
        # Monitoring and Tuning: Monitor your Flink jobs and cluster resources to tune performance. Flink provides metrics that can be used to monitor job performance, resource usage, and to identify bottlenecks.

    # Use Cases for Flink in Your Environment
        # Log and Transaction Processing: Process logs or transactions in real-time to detect anomalies, aggregate statistics, or trigger alerts and actions based on specific patterns or thresholds.
        # Machine Learning: Implement real-time machine learning models that react to streaming data, providing instant insights or predictions based on incoming data streams.
        # Data Pipeline: Build robust data pipelines that cleanse, aggregate, and enrich streaming data before it is stored or further processed. Flink's exactly-once processing guarantees ensure data integrity throughout the pipeline.


# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum 
# is greater than or equal to target. If there is no such subarray, return 0 instead.

def minSubArrayLen(target, nums):
    min_length = float('inf')  # Initialize min_length to infinity
    left = 0  # Start of the window
    current_sum = 0  # Current sum of the window

    for right in range(len(nums)):
        current_sum += nums[right]  # Expand the window to the right
        # Shrink the window from the left as long as the current sum
        # is equal to or larger than the target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    # If min_length is still infinity, no such subarray was found
    return min_length if min_length != float('inf') else 0

# Example usage
nums = [2, 3, 1, 2, 4, 3]
target = 7
print(minSubArrayLen(target, nums))



# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency in alphabetical order (letters are sorted from a-z).

def topKFrequent(words, k):
    # Count the frequency of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Create a list of tuples (word, count) and sort it
    # First, sort alphabetically, then by frequency in reverse order
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Extract the top k words
    return [word for word, count in sorted_words[:k]]

# Example usage
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(words, k))
# Expected output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.



############################################################
# VO5 印度 senior
############################################################
    # database service crud?
# Java
    # how to interact wih DB, sprint? query ?
    # how manage collection?

# application, one service down, failutre?

    # 1. Implement Health Checks
    # Regularly check the health of each service using health endpoints. This allows you to detect and address issues before they impact users.
    # 2. Use Circuit Breakers
    # Implement circuit breakers to prevent a failing service from causing system-wide failures. Circuit breakers stop requests to a service that's deemed unhealthy, allowing it to recover, and fallback methods can provide default responses to maintain functionality.
    # 3. Service Discovery
    # Use a service discovery mechanism that automatically detects and routes around downed services. This ensures that requests are only sent to healthy instances.
    # 4. Load Balancing
    # Employ load balancers to distribute traffic across multiple instances of services. This not only helps with distributing load but also in routing traffic away from unhealthy instances.
    # 5. Timeouts and Retries
    # Set sensible timeouts and implement retry mechanisms with exponential backoff for transient failures. Be cautious with retries to avoid overwhelming a struggling service.
    # 6. Fallback Strategies
    # Design services to have fallback options that provide degraded but acceptable levels of functionality. For example, a product recommendation service might revert to showing best-selling items if personalized recommendations are unavailable.
    # 7. Statelessness and Scalability
    # Design your services to be stateless where possible, allowing for easy scaling up or down. This makes it easier to launch new instances in response to failures or increased load.
    # 8. Distributed Tracing and Monitoring
    # Implement comprehensive monitoring and distributed tracing. This helps in quickly identifying which service is failing and why, significantly reducing downtime.
    # 9. Decouple Service Dependencies
    # Minimize tight coupling between services. Use asynchronous communication, such as message queues or event streams, to allow services to operate and fail independently.
    # 10. Data Replication and Persistence
    # Ensure critical data is replicated across multiple locations (e.g., using a distributed database). This prevents data loss and allows services to continue operating in a read-only mode if necessary.
    # 11. Regular Testing of Failure Scenarios
    # Conduct chaos engineering exercises and regularly test your system's resilience to failures. This includes deliberately taking services down in a controlled environment to ensure the rest of the system behaves as expected.
    # 12. Disaster Recovery Planning
    # Have a disaster recovery plan in place that includes data backups, service restoration procedures, and communication plans for stakeholders.
    # Example Scenario: Handling Service Failure
    # Imagine an e-commerce platform where the payment processing service fails. Here's how the above strategies help maintain functionality:

    # Circuit Breakers: Prevent further strain on the failing service by stopping requests to it.
    # Fallbacks: Switch to an alternative payment method or allow users to choose "pay on delivery" as a fallback.
    # Monitoring: Alert administrators to the failure, providing logs and metrics for quick diagnosis.
    # Service Discovery and Load Balancing: Route new payment requests to healthy instances, if available.
    # Health Checks: Continuously check the health of the payment service to determine when it becomes healthy again and can be reintroduced to handle requests.



# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: sum - 6, sub array [4,-1,2,1]
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Input: nums = []
# Output: 0

# Input: nums = [-1,1,-1,1,-1]
# Output: 1


def findMaxSum(nums):
    if not nums:
        return 0, []

    max_sum = nums[0]
    curr_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > curr_sum + nums[i]:
            curr_sum = nums[i]
            temp_start = i
        else:
            curr_sum += nums[i]
        
        if curr_sum > max_sum:
            max_sum =  curr_sum
            start = temp_start
            end = i
        # # take the next num or adds up
        # curr_sum = max(num, curr_sum + num)
        # max_sum = max(max_sum, curr_sum)
    
    # print(start, end, max_sum)    
    return max_sum, nums[start: end+1]

print(findMaxSum([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(findMaxSum([1])) # 1
print(findMaxSum([])) # 0
print(findMaxSum([-1,1,-1,1,-1])) # 1
print(findMaxSum([5,4,-1,7,8])) # 23


# The largest sum of any contiguous subarray within the given array is 6. This sum comes from the subarray [4, -1, 2, 1]

# The problem is to find the largest sum of any contiguous subarray within the array nums.
# This can be solved using Kadane's algorithm.

# Kadane's Algorithm Explained:
def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Input array
nums = [-2,1,-3,4,-1,2,1,-5,4]

# Find the largest sum
largest_sum = max_subarray_sum(nums)
largest_sum


def find_pair_with_sum(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True  # Pair found
        elif current_sum < target:
            left += 1  # Move the left pointer right to increase the sum
        else:
            right -= 1  # Move the right pointer left to decrease the sum
            
    return False  # Pair not found
