#include <sys/types.h> /* basic system data types */
#include <sys/socket.h> /* basic socket definitions */
#include <netinet/in.h> /* sockaddr_in{} and other Internet defns */
#include <arpa/inet.h> /* inet(3) functions */
#include <sys/errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define SERVER_PORT 8000 /* This is the port that the server is listening on */
#define MAXLINE 4096
#define SA struct sockaddr /* The generic socket address structure */

void str_cli(FILE *fp, int sockfd);
int number1, number2; /* declare global variables */

int main(int argc, char **argv)
{
    int sockfd;
    struct sockaddr_in server_addr; /* This contain the server add structure */

    if (argc < 2) {
        printf("The Server IP address is missing. To run Successfully you need at least an IP address\n");
        printf("Format: <./file> <server IP address>\n");
        exit(1);
    }

    sockfd = socket(AF_INET, SOCK_STREAM, 0); /* create a client socket */

    bzero(&server_addr, sizeof(server_addr)); /* clear the server address structure of any garbage value */

    /* configure the server address structure */
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    inet_pton(AF_INET, argv[1], &server_addr.sin_addr);

    /* connect the client to the server using the client socket */
    connect(sockfd, (SA *) &server_addr, sizeof(server_addr));

    if (argc > 2)
     {
         number1 = atoi(argv[2]);
         number2 = atoi(argv[3]);
     }
     else
     {
         printf("Enter the first number: ");
         scanf("%d", &number1);
         printf("\nEnter the second number: ");
         scanf("%d", &number2);
     }

    str_cli(stdin, sockfd); /* The function that will carry out the logic*/
    close(sockfd);
    exit(0);
}

void str_cli(FILE *fp, int sockfd)
{

    /* declare the character arrays that will hold the data as it is being sent and received from the server */
    char sendline[MAXLINE];
    char recvline[MAXLINE];

    /* convert the two integers to strings, the string will be stored in variable sendline*/
    sprintf(sendline, "%d %d", number1, number2);

    /* send the contents of sendline to server through the client socket using write() function */
    write(sockfd, sendline, strlen(sendline));

    printf("\n\n.... sending the data to server please wait for results (^-^)\n\n");
    sleep(3);

    /* the receive and read result from the server */
    ssize_t n;
    n = read(sockfd, recvline, MAXLINE);

    if(n == 0)
    {
        printf("Server terminated prematurely kindly check if it is still up");
        return;
    }
    /* null terminate the string because read function does not null terminate the recvline. */
    recvline[n] = '\0';

    /* convert the received string to an integer */
    int result = atoi(recvline);

    printf("Thank you for waiting here are your result!!\n");
    /* finally print the result to the user */
    printf("The Sum of the Two integers is: %d\n", result);
}

