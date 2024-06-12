// 胖子说话比较慢 不着急，但是考察的coding工程化很难

// 项目中最困难的是什么？
// 	tracing 故障定位

// 日志很多，如何做存储计算?
// 	索引 query 
// 处理大量日志并进行存储计算是许多现代应用程序和系统中的关键任务。以下是一些用于处理大量日志的常见方法和技术：

  // 使用日志管理工具： 选择适当的日志管理工具，如ELK Stack (Elasticsearch, Logstash, Kibana)、Splunk、Fluentd、Loggly等。这些工具能够帮助你收集、分析和可视化日志数据。

  // 分布式存储系统： 使用分布式存储系统，如Hadoop HDFS、Amazon S3、Google Cloud Storage等，来存储大量的日志数据。这些系统具有高可扩展性和可靠性，适合大规模数据存储。

  // 日志压缩： 在存储日志之前，考虑对日志数据进行压缩以减少存储需求。压缩可以减小存储成本并提高性能。

  // 日志分片： 将日志数据分成小的分片或块，以便更轻松地管理和存储。这可以通过日志滚动策略来实现，例如按时间、按文件大小等。

  // 索引和元数据： 为了快速检索和查询日志数据，使用适当的索引和元数据。这可以加速数据访问和分析。

  // 数据清理： 实施数据清理策略，定期删除不再需要的日志数据，以释放存储空间。这可以是根据保留期限、存储容量或其他因素来执行的。

  // 分布式计算： 使用分布式计算框架，如Apache Spark或Hadoop MapReduce，来对大量日志数据执行计算和分析任务。这将使你能够有效地处理大数据集。

  // 流处理： 如果你需要实时分析和响应日志数据，考虑使用流处理框架，如Apache Kafka和Apache Flink。这些工具允许你实时处理和分析日志数据。

  // 安全性和合规性： 确保你的日志存储和计算符合相关的安全性和合规性标准，包括数据加密、访问控制和审计跟踪。

  // 监控和警报： 实施监控系统来跟踪日志存储和计算的性能和可用性，并设置警报以便在问题出现时及时采取行动。

  // 自动化： 自动化日志管理和存储计算任务，以减少人工干预并提高效率。这可以通过脚本、自动化工具或云服务来实现。



#include <iostream>
#include <string>
using namespace std;

class RemoteReader {
 public:
  virtual size_t read(size_t offset, size_t size, char *output) = 0;
};

class CachingReader {
public:
  // Maximum memory used by a caching reader
  static const size_t kMaxCacheSize;
  
  CachingReader(RemoteReader *remote_reader) 
    :remote_reader_(remote_reader) {}
  
  size_t read(size_t offset, size_t size, char *output);
private
  RemoteReader *remote_reader_;
};

int main()
{
  cout << "Talk is cheap. Show me the code." << endl;
  return 0;
}



// In this optimized version, an LRU cache is used to store the data, 
// and addToCache is responsible for adding data to the cache while managing its size. 
// The cache structure allows for efficient querying of data, making it suitable for scenarios where quick access to cached data is essential.

#include <iostream>
#include <string>
#include <unordered_map>
#include <list>
using namespace std;

class RemoteReader {
public:
    virtual size_t read(size_t offset, size_t size, char* output) = 0;
};

class CachingReader {
public:
    // Maximum memory used by a caching reader
    static const size_t kMaxCacheSize;

    CachingReader(RemoteReader* remote_reader)
        : remote_reader_(remote_reader) {}

    size_t read(size_t offset, size_t size, char* output);

private:
    RemoteReader* remote_reader_;
    unordered_map<size_t, list<char>::iterator> cache_;
    list<char> cacheData_;

    bool isDataInCache(size_t offset, size_t size);
    void addToCache(size_t offset, size_t size, char* data);
};

const size_t CachingReader::kMaxCacheSize = 1024;  // Replace 1024 with your desired value

bool CachingReader::isDataInCache(size_t offset, size_t size) {
    return cache_.find(offset) != cache_.end() && cacheData_.size() - distance(cacheData_.begin(), cache_[offset]) >= size;
}

void CachingReader::addToCache(size_t offset, size_t size, char* data) {
    while (cacheData_.size() + size > kMaxCacheSize) {
        // Remove the least recently used elements if the cache is full
        auto it = cacheData_.begin();
        size_t key = cache_.begin()->first;
        advance(it, key);
        cache_.erase(key);
        cacheData_.erase(it);
    }

    auto it = cacheData_.insert(cacheData_.end(), data, data + size);
    for (size_t i = 0; i < size; ++i) {
        cache_[offset + i] = it;
    }
}

size_t CachingReader::read(size_t offset, size_t size, char* output) {
    size_t totalBytesRead = 0;
    size_t cacheOffset = offset;
    size_t remainingSize = size;

    while (remainingSize > 0) {
        if (isDataInCache(cacheOffset, remainingSize)) {
            size_t bytesAvailable = cacheData_.size() - distance(cacheData_.begin(), cache_[cacheOffset]);
            size_t bytesToCopy = min(remainingSize, bytesAvailable);
            auto it = cache_[cacheOffset];

            memcpy(output + totalBytesRead, &(*it), bytesToCopy);
            totalBytesRead += bytesToCopy;
            cacheOffset += bytesToCopy;
            remainingSize -= bytesToCopy;
        } else {
            char remoteData[kMaxCacheSize];
            size_t bytesRead = remote_reader_->read(cacheOffset, min(kMaxCacheSize, remainingSize), remoteData);

            if (bytesRead == 0) {
                break;
            }

            addToCache(cacheOffset, bytesRead, remoteData);
            cacheOffset += bytesRead;
            remainingSize -= bytesRead;
            totalBytesRead += bytesRead;
        }
    }

    return totalBytesRead;
}

int main() {
    cout << "Talk is cheap. Show me the code." << endl;
    return 0;
}
