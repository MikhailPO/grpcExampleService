# grpcExampleService
gRPC's Python Example services.
## Overview

0. How install and start
    1. [Windows](#Windows)
    2. [Linux](#Linux)
1. [Work and API](#Work-and-API)

## Windows
____
  Execute following scripts:
  ```
  generate_file.bat
  install.bat
  start.bat
  ```
  
## Linux
____
  Execute following scripts:
  ```
  generate_file.sh
  install.sh
  start.sh
 ```
## Work and API
____
The database is created (on local PC) at the first start, to fill it with data, use the API ``` AddClient ``` 
After the start, the message ``` GrpcExample service start ``` will be displayed in the console
The service is running on localhost and is now listening on the port ``` 50051 ```
You can connect to the server using any grpc clients, for example postman
  ## API
  ### AddClient
  ``` Example ```
  ![image](https://user-images.githubusercontent.com/29360277/193614940-9249afc0-1bbd-4acd-b5d9-c198b901440b.png)
  
  ### GetClients
  ``` Example ```
  ![image](https://user-images.githubusercontent.com/29360277/193615167-73d7f20d-38f7-444b-b75d-bd27ee7fabd5.png)
  
  ### GetClientByLogin
  ``` Example ```
  ![image](https://user-images.githubusercontent.com/29360277/193615477-f6e6837f-2732-4850-a41a-cdc47ae82b74.png)

  ### Response error
  ``` Example ```
  ![image](https://user-images.githubusercontent.com/29360277/193616015-cbc33c33-6012-47c0-92cc-604dc72dc972.png)

  

  
