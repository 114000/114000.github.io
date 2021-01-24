---
title: Cloud Fundamentals

---

## Foundational & Compute Service 

### What's Cloud Computing

#### Cloud Computing

Cloud Computing is the delivery of IT resources over the Internet. The cloud is like a virtual data center accessible via the Internet that allows you to manage:

- Storage services likes databases
- Servers, compute power, networking
- Analytics, artificial intelligence, augmented reality
- Security services for data and applications

#### Characteristics of Cloud Computing

- Pay as you go - You pay only for what you use and only when your code runs.
- Autoscaling - The number of active servers can grow or shrink based on demand.
- Serverless - Allows you to write and deploy code without having to worry about the underlying infrastructure.

### Types of Cloud Computing

1. Infrastructure-as-a-Service(IaaS)
  - The provider supplies virtual server instances, storage, and mechanisms for you to manage servers.
  - e.g. AWS(Amazon Web Services), Rackspace, Digital Ocean, Iron Mountain

2. Platform-as-a-Service (PaaS)
  - A platform of development tools hosted on a provider's infrastructure. Provider manage the hardware and operating system. Developer focus on managing and deploying applications.
  - e.g. GoDaddy, salesforcesforce.com
3. Software-as-a-Service (SaaS)
  A software application that runs over the Internet and is managed by the service provider.
  - e.g. Google's Gmail, Microsoft's Office 365

[Resources - Types of Cloud Computing](https://aws.amazon.com/cn/types-of-cloud-computing/)

### Cloud Computing Deployment Model

- Public Cloud
  - A public cloud makes resources available over the Internet to the general public.
  - Resources include databases, application development services, etc.
- Private Cloud
  - A private cloud is a proprietary network that supplies services to a limited number of people.
- Hybrid Cloud
  - A hybrid model contains a combination of both a public and a private cloud.
  - The hybrid model is a growing trend in the industry for those organizations that have been slow to adopt the cloud due to being in a heavily regulated industry. The hybrid model gives organizations the flexibility to slowly migrate to the cloud.

PII(Personally Identifiable Information)


### Common Benefits

- Innovation
- Ability to scale quickly
- Fail fast
- Stop guessing about capacity.
- Avoid huge capital investments up front.
- Pay for only what you use.
- Scale globally in minutes.
- Deliver faster.


### Popular Cloud Platforms Options

- AWS
- GCP(Google Cloud Platform)
- Microsoft Azure

### Services

Cloud Based Products
Amazon Web Services offers a broad set of global cloud-based products.
- Analytics
  * Quick Sight
  * Athena
  * Redshift
- Application integration
  * Simple Queue Service (SQS)
  * Simple Notification Service (SNS)
- Cost management
  * AWS Budgets
- Compute services
  * Elastic Cloud Compute (EC2)
  * Lambda
  * Elastic Beanstalk
- Database management services
  * MySQL
  * Oracle
  * SQLServer
  * DynamoDB
  * MongoDB
- Developer tools
  * Cloud 9
  * Code Pipeline
- Security services
  * Key Management Service (KMS)
  * Shield
  * Identity and Access Management (IAM)
- Additional Services
  * Blockchain
  * Machine Learning
  * Computer Vision
  * Internet of Things (IoT)
  * AR/VR

[Resources - AWS Cloud Proeducts](https://aws.amazon.com/products/)

### Global Infrastructure

- Region
  - Geographic location
  - Availablity zone
  - Reduce latency and costs
- Availability Zone
  - Isolated location
  - Physical data center
  - Failures independent 
- Edge Location
  - Mini data center
  - Cache large data files
  - Content delivery network

- Additional Information
  - There are more Availability Zones (AZs) than there are Regions.
  - There should be at least two AZs per Region.
  - Each region is located in a separate geographic area.
  - AZs are distinct locations that are engineered to be isolated from failures.

- [Resource - Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Resource - Regions & Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

### Shared Responsibility Model

- AWS is responsible for:
  - Securing edge locations
  - Monitoring physical device security
  - Providing physical access control to hardware/software
  - Database patching
  - Discarding physical storage devices
- You are responsible for:
  - Managing AWS Identity and Access Management (IAM)
  - Encrypting data
  - Preventing or detecting when an AWS account has been compromised
  - Restricting access to AWS services to only those users who need it

- [Resources - Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

### Lab: Setup free-tier account

## Foundational & Compute Service

### AWS EC2 (Elastic Cloud Compute)

- Servers for rent
- Manage and deploy application
- Instances
- Physical servers in an AZ(not considered serverless)

[Resources - Amazon Elastic Cloud Compute](https://www.amazonaws.cn/en/ec2/)

**EC2 Auto Scaling**

- Monitors EC2 instances
- Automatically adjusts
- Conditions you define
- Maintain application availability
- Provide peak performance


### AWS EBS (Elastic Block Store)

- Storage solution for EC2
- Physical hard drive
- Attach to server and mount
- Some instances have volumes attached

- Benefits
  * Able to persist data after EC2 is terminated
  * (AWS)Automatically replicated in its AZ

### AWS VPC (Virtual Private Cloud)

- Private network
- Launch services(like EC2) inside
- Security measure
- Public or private subnets


### Compute Power In The Cloud

- Run code in the cloud 
- No provisioning or managing servers (i.e. serverless)
- Automatically scales
- High availability
- Fault tolerance
- Writing code
- Pay when code runs

### AWS Lambda

- Compute power in the cloud
- Chunk of code
- One specific task
- 15 minute time limit

Language Support 

- Node.js
- Python
- Ruby
- Java
- Go
- .NET
- Custom



[Resources - AWS Lambda](https://aws.amazon.com/lambda/)

### Serverless

- No concern for servers
- Pay only when your code runs
- Author locally or directly via console
- Event-driven code
- Environment manages code

### AWS Elastic Beanstalk

- Orchestration service
- Deploy an application
- Provisioning services

The Process
- Create an EC2 instance
- Auto-scaling
- Elastic load balancer
- Administer separately

Runtimes - Java, PHP, Python, .NET, Node.js, Ruby, Docker and Common servers
Services - Database, VPCs, Security groups
 


## Storage & Content Delivery

### Cloud Storage

- collect
- store
- analyze

### Storage Services

- Durability
  * Guarantees no data loss
  * High Durability
  * Your data will be there
- Avaliability
  * How quickly you access data
  * High Avaliability
  * Fast and reliable
- Scalability
  * Meet demand seamlessly
  * Automatically adding or removing
  * Maintain steady state
  * Scaling types
- Vertical scaling
  * Scaling up
  * Modify the server
  * Adding memory or capacity
- Horizontal scaling
  * Scaling out
  * Add or remove servers
  * 2 servers to 6
- Diagonal scaling
  * combination of horizontal and vertical
  * Maximun flexibility


Storage & Database Services

- Amazon Simple Storage Service (Amazon S3)
- Amazon Simple Storage Service (Amazon S3) Glacier
- DynamoDB
- Relational Database Service (RDS)
- Redshift
- ElastiCache
- Neptune
- Amazon DocumentDB

#### AWS S3 (Simple Storage Service) & S3 Glacier

- Object storage system
- Text document
- Image files
- html files
- A unique URL that can be used to access it

**Bucket**

- Objects stored in a bucket
- Holds millions of objects
- S3 Buckets live in a region
- Globally unique names

**Design**

- Durability of 99.999999999%
- Multiple availability zones
- Availability of 99.99%

**Use Case**

- Static websites
- Content delivery
- Backup and recovery
- Archiving and big data
- Application data
- Hybird cloud storage

**Storage Classes**

- Different access levels
- Types
  * S3 Standard
  * S3 Glacier
  * S3 Glacier Deep Archive
  * S3 Intelligent-Tiering
  * S3 Standard Infrequent Access
  * S3 One Zone-Infrequent Access
- S3 Glacier is for Data archiving is cheaper than S3 standard class, 
  * Monthly log files
  * Audit purposes
  * Preserve files
  * infrequently-accessed

**S3 tips**

- S3 is found under the Storage section on the AWS Management Console.
- A single object can be up to 5 terabytes in size.
- You can enable Multi-Factor Authentication (MFA) Delete on an S3 bucket to prevent accidental deletions.
- S3 Acceleration can be used to enable fast, easy, and secure transfers of files over long distances between your data source and your S3 bucket.

### AWS DynamoDB

- Fully managed
- Don't worry about servers
- Don't worry about patches or upgrades

**NoSQL**

- Schema less
- No fixed structure
- Offers flexibility

**Data**

- JSON

**Document**
- Each row or record 


### AWS RDS (Ralational Database Service)

- Aids in database administration
- Sits on top of your database
- Automates time consuming tasks
- Database types
  * Oracle
  * PostgreSQL
  * MySQL
  * MariaDB
  * SQL Server
  * Aurora(AWS)
    - MySQL
    - Postgres
- Features
  * Failover, Backups
  * Restore, Encryption
  * Security, Monitoring
  * Data replication
  * Ability to scale


**Persist Data**

- Relational database
  * Oracle
  * PostgreSQL
  * MySQL

**Administration**

- Hard and time consuming
- Specialized skills
- Takes away development time

**Tasks**

- Upgrades
- Patching
- Installs
- Backups
- Monitoring
- Performance checks, security

**Resourses**

- [What Is A Relational Database](https://aws.amazon.com/relational-database/)
- [Amazon Relational Database Service](https://aws.amazon.com/rds/)
- [AWS Product Databases using Relational Databases](https://aws.amazon.com/products/databases/)

### AWS Redshift

- Data warehousing service
- Manage big data
- Quickly scale
- Managed Service
  * Execute fast queries
  * SQL
  * ETL
  * BI
  * Automates tasks
- Features
  * Fast query and analysis
  * Not transaction processing
  * Hsitorical data
  * Recent transactions placed in relational database
  * Old orders archived
- Format
  * Columnar format
  * Not a row store
  * Aids in fast query and analysis

### CDN (Content Delivery Network)

- Speeds up delivery
- Static and dynamic web content
  * Web pages
  * Cascading style sheets
  * JavaScript
  * Images
- Content
  * Cached
  * Content pulled from cache
  * Fast delivery
- Benefits
  * Reduces latency  
  * Decreases load from servers
  * Good end-user experience

**Latency**

- Respond to a request
- The time from website access to website load

#### AWS Cloud Front

- AWS content delivery
- Edge loations - Amazion's worldwide 
- Configure how long an item remains cached before a refresh
- Manually expire
- Maximum size: 20GB

## Security 


### AWS Shield

- DDoS (Distributed Denial of Service)
- Distributed Denial of Service


**DDoS Attack**

- Website or application 
- unavailable
- Overwhelming it
- Multiple sources

### AWS WAF(Web Application Firewall)


**Firewall**

- Network security mechanism
- Monitors and controls
- Incoming and outgoing
- Security rules

**Common Attacks**

- SQL injection
- Cross-site scripting
- Reviewing data send
- Stopping well-known attacks


### AWS IAM (Identity & Access Management)

- Configure
  * AWS account
    - Email address - Root level account with full access and permission
    - MFA (Muli Factor Authentication) Addition form of authentication, e.g. phone code.
  * Services
  * Application 
- Global service is automatically available across all regions


**User**

- Protect data and systems
- verify users
- Access specific data
- Least privileged access

**IAM User**

- Entity
- Person or service
- Access credentials

**IAM Group**

- Collection of users
- Permission for a collection
- Easy to manage

**IAM Role**

- Identity
- Permissions
- Set if privileges
- Not associated with a user or group
- Attached or assumed

**Policy**

- Granular permission, Users, Groups, Roles

**EC2 Security Group**

- Not a part of IAM
- IAM security group
- EC2 instance
- Built-in firewall

## Networking & Elasticity

**Cloud Networking**

- Network architecture
- Network connectivity: Services offer reliable and cost-effective ways to route end-users to Internet appliaction
- Application delivery
- Global performance
- Delivery

**DNS (Domain Name System)**

- Foundational networking service
- Domain Name System
- Domain authority
- Registration service
- Process
  * Routed to address
  * Website displays


### AWS Route 53

- Cloud DNS
- Reliable and scalable
- Global
- Register a domain name
- Route Internet traffic
- Health check
  * Ensure web servers
  * DNS failover
  * Alternate location to avoid site outages


**Elastic Load Balancer**

- Balances the load
- Stands in front
- Redundancy and performance
  * Redundancy: if you lose a server, the load balancer will send requests to other working servers.
  * Performance: if a server starts having issues or bottlenecks, the load balancer will add more servers
  to the poll available servers.
  

## Messaging & Containers

- Text message
- Emails
- Storage and flexibility
- Send notifications
- Track notification lifecycle

**Message**

- Internet-based applications
- Devices
- Send a message

### AWS SNS(Simple Notification Service)

is a cloud service that allow you to send notifictions to the users of your applications.

- Publish/subsribe 
- Sign-up first
- Subscribe
  * Person
  * Other AWS services
- ways
  * Mobile push
  * Text messages
  * Email

**Queue**

- Waiting in line 
- Join in line 
- Message
- Join queue
- First In First Out(FIFO)

Messaging queues improve:

- performance
- scalability
- asynchronous processing
- user experience

### AWS SQS(Simple Queue Service)

- Fully managed queue service
- Integrate queuing functionally
- Send/store/receive messages
- types
  * Standard - best-effort ordering
  * FIFO - exacting once, exacting order
- example
  * Course registration system
  * Account creation
  * Course registration
  * Messages stored on queue


**Docker**

- Leading container technology
- Container orchestration services
- Docker clusters
  * Kubernetes
  * Docker Swarm
- Popularity
  * Everything an application needs
    * Application
    * Dependencies
    Bundled in one package
- Migration
  * Don't have to rebuild
  * Environment to environment
  * Move entire container
  * Independent component 

### AWS ECS(Elastic Container Service)

- Orchestration service
- Supports Docker
- Managing containers
- Feature
  * Lauching 
  * Stopping 
  * Scaling
  * Querying state
  * Convenience service


## AWS Management

### AWS Cloud Trail

- Audit AWS account 
- Log ins
- Services accessed
- Records calls
- Delivers log file

### AWS Cloud Watch

- Monitors resources and applications
- Collect and track metircs
- Collect monitor logs
- Set alarms and create triggers
- React to change 




### AWS Cloud Formation 

- Infrastructure As Code
- Model your infrastructure 
- Text file template 
  * JSON or YAML
  * From scratch
  * Reuse a blueprint 
  * Visual designer
  * Version control
- Provision AWS resources

**Infrastructure as Code**

- Stand up servers
- Databases
- Runtime parameters
- Resources
- Scripts


### AWS CLI(Command Line Interface)

