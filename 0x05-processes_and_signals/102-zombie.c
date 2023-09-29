#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - The program's infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - The program's entry point
 *
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid > 0)
		{
			printf("Zombie mode activated, PID: %d\n", zombie_pid);
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (0);
}
