#include <pthread.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <unistd.h>

#include "kernel.c"

uint64_t combine_digits(
	const uint8_t digit1, const uint8_t digit2, const uint8_t digit3, const uint8_t digit4,
	const uint8_t digit5, const uint8_t digit6, const uint8_t digit7, const uint8_t digit8,
	const uint8_t digit9, const uint8_t digit10, const uint8_t digit11, const uint8_t digit12,
	const uint8_t digit13, const uint8_t digit14
) {
	return digit14 +
	       digit13 * 10ll +
		   digit12 * 100ll +
		   digit11 * 1000ll +
		   digit10 * 10000ll +
		   digit9  * 100000ll +
		   digit8  * 1000000ll +
		   digit7  * 10000000ll +
		   digit6  * 100000000ll +
		   digit5  * 1000000000ll +
		   digit4  * 10000000000ll +
		   digit3  * 100000000000ll +
		   digit2  * 1000000000000ll +
		   digit1  * 10000000000000ll;
}

typedef struct {
	uint8_t digit1;
	uint8_t digit2;
} digit_pair_t;

typedef struct {
	digit_pair_t task;
	uint64_t progress;
	uint64_t min_result;
	uint64_t max_result;
	bool complete;
} task_comm_t;

void* worker(void *arg) {
	volatile task_comm_t *comm = (task_comm_t*) arg;
	
	const uint8_t digit1 = comm->task.digit1;
	const uint8_t digit2 = comm->task.digit2;
	
	for (uint8_t digit3  = 1; digit3  < 10; ++digit3 ) {
	for (uint8_t digit4  = 1; digit4  < 10; ++digit4 ) {
	for (uint8_t digit5  = 1; digit5  < 10; ++digit5 ) {
	for (uint8_t digit6  = 1; digit6  < 10; ++digit6 ) {
	for (uint8_t digit7  = 1; digit7  < 10; ++digit7 ) {
	for (uint8_t digit8  = 1; digit8  < 10; ++digit8 ) {
	for (uint8_t digit9  = 1; digit9  < 10; ++digit9 ) {
	for (uint8_t digit10 = 1; digit10 < 10; ++digit10) {
	for (uint8_t digit11 = 1; digit11 < 10; ++digit11) {
	for (uint8_t digit12 = 1; digit12 < 10; ++digit12) {
	for (uint8_t digit13 = 1; digit13 < 10; ++digit13) {
	for (uint8_t digit14 = 1; digit14 < 10; ++digit14) {
		int64_t result = kernel(
			digit1, digit2, digit3, digit4, digit5, digit6, digit7,
			digit8, digit9, digit10, digit11, digit12, digit13, digit14
		);
		
		if (result == 0) {
			comm->max_result = combine_digits(
				digit1, digit2, digit3, digit4, digit5, digit6, digit7,
				digit8, digit9, digit10, digit11, digit12, digit13, digit14
			);
			
			if (comm->min_result == 0) {
				comm->min_result = comm->max_result;
			}
		}
	}
	}
	}
	}
	}
	}
	}
	}
	}
		comm->progress = (digit3 - 1) * 81  + (digit4 - 1) * 9 + digit5;
	}
	}
	}
	
	comm->complete = true;
}

void run_worker_group(digit_pair_t *tasks, int si, int ei) {
	volatile task_comm_t comm[ei - si];
	pthread_t   threads[ei - si];
	
	for (int i = 0; i < ei - si; ++i) {
		comm[i].task = tasks[si + i];
		comm[i].progress = 0;
		comm[i].min_result = 0;
		comm[i].max_result = 0;
		comm[i].complete = false;
		
		printf("Thread #%d will do (%u, %u).\n", i + 1, comm[i].task.digit1, comm[i].task.digit2);
	}
	
	puts("Starting threads.");
	for (int i = 0; i < ei - si; ++i) {
		pthread_create(&threads[i], 0, worker, (void*) &comm[i]);
	}
	
	while (1) {
		printf("\r");
		bool all_done = true;
		for (int i = 0; i < ei - si; ++i) {
			printf("#%d: %u ", i + 1, comm[i].progress);
			if (!comm[i].complete) all_done = false;
		}
		
		if (all_done) break;
		
		usleep(1000000);
	}
	printf("\n");
	
	puts("Results.");
	for (int i = 0; i < ei - si; ++i) {
		printf("#%d %llu %llu\n", i + 1, comm[i].min_result, comm[i].max_result);
	}
}

int main(int argc, char **argv) {
	digit_pair_t pairs[81];
	
	uint16_t i = 0;
	for (uint8_t j = 1; j < 10; ++j) {
		for (uint8_t k = 1; k < 10; ++k) {
			digit_pair_t pair = { j, k };
			pairs[i++] = pair;
		}
	}
	
	puts("First worker group.");
	run_worker_group(pairs, 0, 16);
	
	puts("Second worker group.");
	run_worker_group(pairs, 64, 81);
	
	puts("Third worker group.");
	run_worker_group(pairs, 16, 32);
	
	puts("(you may Ctrl+C now.)");
	
	puts("Fourth worker group.");
	run_worker_group(pairs, 48, 64);
	
	puts("Fifth worker group.");
	run_worker_group(pairs, 32, 48);	
}