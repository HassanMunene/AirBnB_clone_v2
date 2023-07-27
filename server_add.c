#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h> // used for handling internet addresses and converting them to different format
#include <sys/errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define SERVER_PORT 8000
#define MAXLINE 4096
#define LISTENQ 5

void str_echo(int sockfd); //This is the function that will handle the client

int main(int argc, char **argv)
{
    int listenfd, connectedfd;
    pid_t child_pid;
    socklen_t client_addr_len;
    struct sockaddr_in client_addr, server_addr;

    // create listening socket
    listenfd = socket(AF_INET, SOCK_STREAM, 0);

    // clear server address structure of any garbage value
    bzero(&server_addr, sizeof(server_addr));

    // Assign values to server address structure, family, ip, port
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(SERVER_PORT);

    printf("---------------------------------------------\n");
    printf("Serving Client APP client_add\n\nRunning on address 0.0.0.0:port 8000 \n\nWARNING: This is a testing Server\n\n");
    printf("----------------------------------------------\n");

    // bind the listenig socket to an ip and port number
    bind(listenfd, (struct sockaddr *)&server_addr, sizeof(server_addr));
    printf("***BINDING OUR SOCKET TO AN IP ADDRESS AND PORT Number:8000***\n\n");
    sleep(2);

    // call the listen() for the server to start listening for connections
    listen(listenfd, LISTENQ);
    printf("***SERVER HAS STARTED LISTENING FOR CONNECTIONS***\n");
    printf("Press CTRL+C to quit\n");

    for ( ; ; )
    {
        client_addr_len = sizeof(client_addr);
        connectedfd = accept(listenfd, (struct sockaddr *)&client_addr, &client_addr_len);
        if (connectedfd > 0)
        {
            printf("***Recieved A Connection From: %s Port: %d***\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));
        }
        child_pid = fork();
        if (child_pid == 0)
        {
            // This means we are in the child process
            close(listenfd);
            str_echo(connectedfd);
            exit(0);
        }
        else if (child_pid > 0)
        {
            // we are in the parent process
            close(connectedfd);
        }
    }
}

/**
 * read the two integers sent by the client
 * calculate the sum of the two integers
 * send the result of the sum back to the client
 */

void str_echo(int sockfd)
{
    /* declare a character array that will hold the recieved data from client */
    char recvline[MAXLINE];

    /* read the data from client through the server socket(sockfd) and then store the data in recvline */
    ssize_t n;
    n = read(sockfd, recvline, MAXLINE);
    if (n == 0)
    {
        printf("Im not receiving any data from the client, can you check if the client is really sending the data");
        return;
    }

    /* as always null terminate the string */
    recvline[n] = '\0';

    /* declare two integer variables will hold the integers once they have been exctrcted from recvline */
    int number1, number2;

    /* extract two integers from the recvline using sscanf*/
    int items = sscanf(recvline, "%d %d", &number1, &number2);

    if (items != 2)
    {
        printf("The input from the client is not valid. Ensure you enter Two numbers\n");
        return;
    }
    /* calculate the sum of the two numbers */
    int sum = number1 + number2;

    /* convert the sum to a string to send it to the client using sprintf*/
    char sendline[MAXLINE];
    sprintf(sendline, "%d", sum);

    /* send the data back to the client through the socket*/
    write(sockfd, sendline, strlen(sendline));
}

