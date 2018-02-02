# This section is about big data and relating technologies
# data on local computer has size between 0 and 8 GB
# when data scale is bigger than 8GB try using SQL DB to move storage on to
# hard drive instead of RAM or distribute data to multiple machines

# Local machine versus Distributed System. Local machine is restricted by the
# RAM, CPU and HDD of the local computer. Distributed system use one machine to
# manage many other machines and thus can use their computing resources.
# Process could also work locally or distributedly. And it is easier to scale
# out workload to many weak machines than to scale up to a single powerful one.
# Distributed system has advantage at scaling by adding new machines versus
# local machine may have more limit on expending CPU, RAM and HDD capability.
# Distributed System has better fault tolerance without single failure point.

# Hadoop is a way to distribute very large files across multiple machines by
# using Hadoop Distributed File System (HDFS) which can work with large data
# sets, provide fault tolerance by duplicating blocks of data and MapReduce to
# allow computations on that data.

# HDFS uses blocks of data with a size of 128 MB by default and duplicates
# these data blocks 3 times with support of fault tolerance. Keeping the data
# blocks small facilitates parallelization during processing and multiple
# copies of data prevent loss of data due to failure of a single node point.
# MapReduce splits a computation task to a distributed set of files. It 
# consists of a Job Tracker and multiple Task Trackers. Job Tracker control the
# whole job and sends code to run on Task Trackers, while Task Trackers
# allocate CPU and RAM for the tasks and monitor tasks on the worker nodes.

# Spark is an open source project o Apache for quickly and easily handling Big
# Data. Spark was created at the AMPLab at UC Berkeley on 2009 and first
# released in Feb 2013. Spark is a flexible alternative to MapReduce and can
# work on various kinds of data formats such as Cassandra, AWS S3 and HDFS.

# MapReduce requires files to be stored in HDFS, Spark does not as it also
# support other file formats. And Spark works 100x faster than MapReduce.
# MapReduce writes most data to disk after each map and reduce operation, while
# Spark keeps most of the data in memory after each transformation and only
# spill over the data to disk if the memory is filled.

# Spark has Resilient Distributed Dataset (RDD) at core with 4 main features
# of Distributed Collection of Data, Fault Tolerant, Parallel Operation, and
# ability to user many other data sources. RDDs are immutable, lazily evaluated
# and cachable, with two types of operations of Transformation and Action.

# The basic Transformations are Filter, Map, and FlatMap
# Filter applies a function to each element and returns that evaluate to true
# Map transforms each element and preserves their index, similar to .apply()
# FlatMap transforms each element into 0-N elements and changes their index

# The basic Actions are First, Collect, Count, and Take.
# Count returns the number of elements in the RDD. 
# First return the first element in the RDD.
# Take returns an array with the first n elements of the RDD.
# Collect return all elements of the RDD as an array.

# RDDs usually hold their values in tuples with form of (key,value) which offer
# better patitioning of data and leads to functionality based on reduction.
# Reduce() aggregates RDD elements with a function that returns one element
# ReduceByKey() aggregates Pair RDD with a function that returns a Pair RDD
# The actions above work similar to a Group By operation.