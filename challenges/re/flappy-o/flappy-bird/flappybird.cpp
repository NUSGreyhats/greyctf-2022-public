#include <ncurses.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#include <iostream>
using namespace std;

#define GET_NAME(playerName) getstr(playerName)
#define FILE_NAME "bestScore.bin"
#define NAME_SIZE 100
#define JUMP 4
#define CRACK_SIZE 4
#define WAIT_BIG 140000
#define WAIT_LIT 110000
#define DOUBLE 2

void setupColors();
void writeInfo(int row, int col);
void drawPipe(int begin, int end, int pipeCol, int row);
void drawStarting(int row, int col);
void gameLoop();
void readBest(int * bestScore, char bestPlayerName[]);
void writeBest(int bestScore, const char bestPlayerName[]);
void getPlayerName(char playerName);
void getNewPipeValue(int * crackStart, int * crackFinish, int row);
void ggs();
int controlCollision(int pipeCol, int birdCol, int birdRow, int crackStart,
					 int crackFinish);

int score = 0, isScore = 0, bestScore = 0;
int isOver = 0, flag = -1;
;
int crackStart1, crackFinish1, crackStart2, crackFinish2;
int row, col, birdRow, birdCol, pipeCol1, pipeCol2;
int pipeCounter, collision;
int wait_duration = WAIT_LIT;
int command;
char playerName[NAME_SIZE], bestPlayerName[NAME_SIZE];
char bird = 'O', ch;

int main() {
	srand(time(NULL));

	readBest(&bestScore, bestPlayerName);

	initscr();
	curs_set(0);
	keypad(stdscr, true);

	setupColors();

	getmaxyx(stdscr, row, col);

	if (row < 24 || col < 75) {
		wait_duration = WAIT_BIG;
	}

	writeInfo(row, col);
	GET_NAME(playerName);

	drawStarting(row, col);

	refresh();
	noecho();
	timeout(true);

	birdRow = row / 2;
	birdCol = col / 4;
	pipeCol1 = col;
	pipeCol2 = col;
	pipeCounter = col;

	getNewPipeValue(&crackStart1, &crackFinish1, row);
	getNewPipeValue(&crackStart2, &crackFinish2, row);

	gameLoop();

	writeBest(bestScore, bestPlayerName);
	ggs();

	return 0;
}

void setupColors() {
	start_color();
	int mode = rand() % 2;
	// RANDOM FOREGROUND AND BACKGROUND COLORS
	if (mode == 0) {
		assume_default_colors(COLOR_BLACK, COLOR_CYAN);  // DAY MODE
	} else {
		assume_default_colors(COLOR_WHITE, COLOR_BLACK);  // NIGHT MODE
	}
	init_pair(1, COLOR_BLACK, COLOR_GREEN);  // PIPE COLORS
	int birdType = rand() % 3;
	// RANDOM BIRD COLORS
	if (birdType == 0) {
		init_pair(2, COLOR_BLACK, COLOR_YELLOW);
		if (mode == 0) {
			init_pair(7, COLOR_YELLOW, COLOR_CYAN);
		} else {
			init_pair(7, COLOR_YELLOW, COLOR_BLACK);
		}
	} else if (birdType == 1) {
		init_pair(2, COLOR_BLACK, COLOR_RED);
		if (mode == 0) {
			init_pair(7, COLOR_RED, COLOR_CYAN);
		} else {
			init_pair(7, COLOR_RED, COLOR_BLACK);
		}
	} else if (birdType == 2) {
		init_pair(2, COLOR_BLACK, COLOR_BLUE);
		if (mode == 0) {
			init_pair(7, COLOR_BLUE, COLOR_CYAN);
		} else {
			init_pair(7, COLOR_BLUE, COLOR_BLACK);
		}
	}
	init_pair(3, COLOR_YELLOW, COLOR_YELLOW);  // UNDERGROUND COLORS
	init_pair(4, COLOR_BLACK, COLOR_WHITE);	// LOGO COLORS
	init_pair(5, COLOR_WHITE, COLOR_RED);	  // GAME OVER COLORS
	init_pair(6, COLOR_WHITE,
			  COLOR_GREEN);  // GET READY AND GROUND BORDER COLORS
}

void writeInfo(int row, int col) {
	/*
	 _____ _                         ____  _         _
	|  ___| | __ _ _ __  _ __  _   _| __ )(_)_ __ __| |
	| |_  | |/ _` | '_ \| '_ \| | | |  _ \| | '__/ _` |
	|  _| | | (_| | |_) | |_) | |_| | |_) | | | | (_| |
	|_|   |_|\__,_| .__/| .__/ \__, |____/|_|_|  \__,_|
				  |_|   |_|    |___/
	*/
	attron(A_BOLD | COLOR_PAIR(4));
	mvprintw(row / 2 - 10, (col - 50) / 2,
			 " _____ _                         ____  _         _ ");
	mvprintw(row / 2 - 9, (col - 50) / 2,
			 "|  ___| | __ _ _ __  _ __  _   _| __ )(_)_ __ __| |");
	mvprintw(row / 2 - 8, (col - 50) / 2,
			 "| |_  | |/ _` | '_ \\| '_ \\| | | |  _ \\| | '__/ _` |");
	mvprintw(row / 2 - 7, (col - 50) / 2,
			 "|  _| | | (_| | |_) | |_) | |_| | |_) | | | | (_| |");
	mvprintw(row / 2 - 6, (col - 50) / 2,
			 "|_|   |_|\\__,_| .__/| .__/ \\__, |____/|_|_|  \\__,_|");
	mvprintw(row / 2 - 5, (col - 50) / 2,
			 "              |_|   |_|    |___/                   ");
	attroff(A_BOLD | COLOR_PAIR(4));
	/*
				[][][][][][]
			[][]      []    []
		  []        []        []
	  [][][][]      []      []  []
	[]        []    []      []  []
	[]          []    []        []
	[]          []      [][][][][][]
	  []      []      []            []
		[][][]      []  [][][][][][]
		[]            []          []
		  [][]          [][][][][]
			  [][][][][]
	*/
	attron(COLOR_PAIR(7));
	mvprintw(row / 2 - 3, (col - 34) / 2, "            [][][][][][]          ");
	mvprintw(row / 2 - 2, (col - 34) / 2, "        [][]      []    []        ");
	mvprintw(row / 2 - 1, (col - 34) / 2, "      []        []        []      ");
	mvprintw(row / 2 + 0, (col - 34) / 2, "  [][][][]      []      []  []    ");
	mvprintw(row / 2 + 1, (col - 34) / 2, "[]        []    []      []  []    ");
	mvprintw(row / 2 + 2, (col - 34) / 2, "[]          []    []        []    ");
	mvprintw(row / 2 + 3, (col - 34) / 2, "[]          []      [][][][][][]  ");
	mvprintw(row / 2 + 4, (col - 34) / 2, "  []      []      []            []");
	mvprintw(row / 2 + 5, (col - 34) / 2, "    [][][]      []  [][][][][][]  ");
	mvprintw(row / 2 + 6, (col - 34) / 2, "    []            []          []  ");
	mvprintw(row / 2 + 7, (col - 34) / 2, "      [][]          [][][][][]    ");
	mvprintw(row / 2 + 8, (col - 34) / 2, "          [][][][][]              ");
	attroff(COLOR_PAIR(7));
	mvprintw(row / 2 + 10, (col - 24) / 2, "Enter Your Name: ");
}

int checkCollision(int pipeCol, int birdCol, int birdRow, int crackStart,
					 int crackFinish) {
	int status = false;

	if (pipeCol - 8 == birdCol || pipeCol - 7 == birdCol ||
		pipeCol - 6 == birdCol || pipeCol - 5 == birdCol ||
		pipeCol - 4 == birdCol || pipeCol - 3 == birdCol ||
		pipeCol - 2 == birdCol || pipeCol - 1 == birdCol) {
		status++;
		if (birdRow < crackStart || birdRow > crackFinish) {
			status++;
		}
	}

	return status;
}

void drawPipe(int begin, int end, int pipeCol, int row) {
	for (int i = 0; i < row - 3; i++) {
		if (i < begin) {
			if (i == begin - 1 || i == begin - 2) {
				mvprintw(i, pipeCol - 9, "          ");
			} else if (i == begin - 3) {
				mvprintw(i, pipeCol - 8, "________");
			} else {
				//                       9876543210
				mvprintw(i, pipeCol - 8, "        ");
			}
		}
		if (i > end) {
			if (i == end + 1) {
				mvprintw(i, pipeCol - 9, "          ");
			} else if (i == end + 2) {
				mvprintw(i, pipeCol - 9, " ________ ");
			} else {
				mvprintw(i, pipeCol - 8, "        ");
			}
		}
	}
}

void drawStarting(int row, int col) {
	clear();
	/*
	  ____      _     ____                _       _
	 / ___| ___| |_  |  _ \ ___  __ _  __| |_   _| |
	| |  _ / _ \ __| | |_) / _ \/ _` |/ _` | | | | |
	| |_| |  __/ |_  |  _ <  __/ (_| | (_| | |_| |_|
	 \____|\___|\__| |_| \_\___|\__,_|\__,_|\__, (_)
											|___/
	*/
	attron(A_BOLD | COLOR_PAIR(6));
	mvprintw(row / 2 - 10, (col - 48) / 2,
			 "  ____      _     ____                _       _ ");
	mvprintw(row / 2 - 9, (col - 48) / 2,
			 " / ___| ___| |_  |  _ \\ ___  __ _  __| |_   _| |");
	mvprintw(row / 2 - 8, (col - 48) / 2,
			 "| |  _ / _ \\ __| | |_) / _ \\/ _` |/ _` | | | | |");
	mvprintw(row / 2 - 7, (col - 48) / 2,
			 "| |_| |  __/ |_  |  _ <  __/ (_| | (_| | |_| |_|");
	mvprintw(row / 2 - 6, (col - 48) / 2,
			 " \\____|\\___|\\__| |_| \\_\\___|\\__,_|\\__,_|\\__, (_)");
	mvprintw(row / 2 - 5, (col - 48) / 2,
			 "                                        |___/   ");
	attroff(A_BOLD | COLOR_PAIR(6));
	mvprintw(row / 2 + 1, (col - 5) / 2 + 3, "]");
	mvprintw(row / 2 + 1, (col - 5) / 2 - 1, "[");
	mvprintw(row / 2 + 3, (col - 34) / 2,
			 "Press \"SPACE BAR\" to flap the bird");

	for (int j = 1; j < 4; j++) {
		for (int i = 0; i < j; i++) {
			mvprintw(row / 2 + 1, (col - 5) / 2 - 1 + j, "#");
			refresh();
		}
		sleep(1);
	}
}

void processInput() {
	command = getch();
	if (command == ' ') {
		flag++;
		birdRow -= JUMP;
	} else if (command == KEY_F(5)) {
		wait_duration -= 10000;
	}

	if (birdRow < row - 1) {
		birdRow++;
	}

	if (birdRow < 2) {
		birdRow = 2;
	}

	if (birdRow > row - 4 /*|| birdRow == 2*/) {
		// TOUCH THE GROUND
		isOver = true;
	}
}

void drawBird() {
	mvaddch(birdRow, birdCol, bird | COLOR_PAIR(2));
}

void drawStats() {
	if (score % 8 == 0) {
		mvprintw(1, col / 2 - 20, "SCORE : %d", score / 8);
	}

	mvprintw(0, col / 2 - 20, "%s", playerName);
	mvprintw(0, col / 2 + 13, "%s", bestPlayerName);
	mvprintw(1, col / 2 + 13, "BEST : %d", bestScore);
}

void drawAndUpdatePipes() {
	attron(COLOR_PAIR(1));
	drawPipe(crackStart1, crackFinish1, pipeCol1, row);

	// if (pipeCounter < col / 2) {
	// 	drawPipe(crackStart2, crackFinish2, pipeCol2, row);
	// 	pipeCol2--;
	// }
	pipeCol1--;
	attroff(COLOR_PAIR(1));
}

void drawGrass() {
	for (int i = 0; i < col; i++) {
		attron(COLOR_PAIR(3));
		mvprintw(row - 1, i, "#");
		mvprintw(row - 2, i, "#");
		attroff(COLOR_PAIR(3));
		attron(COLOR_PAIR(6));
		mvprintw(row - 3, i, "/");
		attroff(COLOR_PAIR(6));
		// mvprintw(2, i, "#");
	}
}

void checkAndHandleCollision() {
	collision = checkCollision(pipeCol1, birdCol, birdRow, crackStart1,
								crackFinish1);
	// collision = 1;
	if (collision) {
		if (collision == DOUBLE) {
			isOver = true;
		} else if (isScore) {
			score++;
			if (score / 8 > bestScore) {
				bestScore = score / 8;
				strcpy(bestPlayerName, playerName);
			}
		}
	}

	// collision = checkCollision(pipeCol2, birdCol, birdRow, crackStart2,
	// 								crackFinish2);
	// if (collision) {
	// 	if (collision == DOUBLE) {
	// 		isOver = true;
	// 	} else if (isScore) {
	// 		score++;
	// 		if (score / 8 > bestScore) {
	// 			bestScore = score / 8;
	// 			strcpy(bestPlayerName, playerName);
	// 		}
	// 	}
	// }
}

void updatePipeIfNeeded() {
	if (pipeCol1 == 0) {
		getNewPipeValue(&crackStart1, &crackFinish1, row);
		pipeCol1 = col;
	}

	// if (pipeCol2 == 0) {
	// 	getNewPipeValue(&crackStart2, &crackFinish2, row);
	// 	pipeCol2 = col;
	// 	pipeCounter = col / 2;
	// }
}

void reportCheater() {
	mvprintw(row / 2 + 1, (col - 39) / 2, "Cheater Detected!");
	refresh();
	getchar();
	endwin();
	exit(0);
}

unsigned char key1[] = "\xaa\x7a\xe1\xbb\x9a\xe7\xff\x7c\x35\x01\x06\x09\xc2\x50\x62\x38\xdb\x76\xd5\xe1\x68\xa9\xbf\xb4\x52\x8f\xc0\x17\x0e\x2f\xda\xea\x8a\xcf\xa2\x90\xe7\x08\xeb\x0e\x3b\x14\x72\xbe\x9a\xde\xd5\x51\x97\x2c\xbc\xf3\x35\xb6\x21\x29\x7d\xa8\xd7\x2b\xed\xfe\xf0";
unsigned int key2[] = {0x7caa42eb, 0xcd53fda8, 0xf7420557, 0x5267eec4, 0x793e70ed, 0x68d1aec0, 0x38da23eb, 0x6f1d6fb1, 0x39489b7b, 0xf4f87516, 0xed67bc18, 0x8ad36ba0, 0xaf2a684f, 0x80883171, 0x86ce7d28, 0x438cb016, 0x5784988c, 0x4bb5278b, 0xbfdcd0c6, 0x6dda7789, 0xb0f09aa3, 0x557478be, 0xc372aee8, 0x40a28470, 0xa855383a};

unsigned short lfsr1(int n) {
    int i, lsb;
	int seed = 0xabcd;

    for (i=0; i<n; i++) {
        lsb = seed & 1;
        seed >>= 1;
        if (lsb) seed ^= 0x82EE;
    }

	return seed;
}

int lfsr2_seed = 0x1a2b3c4d;

unsigned int lfsr2(int n) {
    int i, lsb;

    for (i=0; i<n; i++) {
        lsb = lfsr2_seed & 1;
        lfsr2_seed >>= 1;
        if (lsb) lfsr2_seed ^= 0x80000DD7;
    }

	return lfsr2_seed;
}

char genFlag1(int n) {
	return key1[n] ^ (lfsr1(n) & 0xff);
}

int genFlag2(int i) {
	return lfsr2(lfsr1(i)) ^ key2[i/10000];
}

int prevScore = 0;
unsigned char flag1[sizeof(key1)+4] = {0};
unsigned char flag2[sizeof(key2)] = {0};
void updateAndDrawFlag() {
	mvprintw(3, col / 2 - 20, "%s", flag1);
	mvprintw(4, col / 2 - 20, "%s", flag2);

	int actualScore = score / 8;
	if (actualScore == prevScore) return;
	if (actualScore - prevScore != 1) {
		reportCheater();
	}

	// actualScore *= 10000;

	// flag1 is generated from lfsr with xor key
	if (actualScore < sizeof(key1))	flag1[actualScore - 1] = genFlag1(actualScore - 1);

	// flag2 is comprised of pieces. when score reaches multiple of 10000 a char of flag2 is shown
	lfsr2(1);
	if (actualScore % 10000 == 0 && actualScore/10000 <= sizeof(key2)/4)
		((unsigned int*)flag2)[actualScore/10000-1] = genFlag2(actualScore-10000);

	// actualScore /= 10000;
	prevScore = actualScore;
}

void gameLoop() {
	while (!isOver) {
		clear();

		processInput();
		drawBird();
		drawStats();
		drawAndUpdatePipes();
		drawGrass();

		checkAndHandleCollision();
		updatePipeIfNeeded();

		updateAndDrawFlag();

		isScore++;
		pipeCounter--;

		refresh();
		usleep(wait_duration);
	}
}

void readBest(int * bestScore, char bestPlayerName[]) {
	FILE * bestFilePtr;

	bestFilePtr = fopen(FILE_NAME, "rb");
	if (bestFilePtr != NULL) {
		fread(bestScore, sizeof(int), 1, bestFilePtr);
		fread(bestPlayerName, sizeof(char) * NAME_SIZE, 1, bestFilePtr);
		fclose(bestFilePtr);
	}
}

void writeBest(int bestScore, const char bestPlayerName[]) {
	FILE * bestFilePtr;

	bestFilePtr = fopen(FILE_NAME, "wb");
	fwrite(&bestScore, sizeof(int), 1, bestFilePtr);
	fwrite(bestPlayerName, sizeof(char) * NAME_SIZE, 1, bestFilePtr);

	fclose(bestFilePtr);
}

void getNewPipeValue(int * crackStart, int * crackFinish, int row) {
	*crackStart = rand() % row / 2 + 3;
	*crackFinish = *crackStart + CRACK_SIZE;
}

void ggs() {
	clear();
	/*
	  ____                         ___
	 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __
	| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
	| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |
	 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
	*/
	attron(A_BOLD | COLOR_PAIR(5));
	mvprintw(row / 2 - 10, (col - 51) / 2,
			 "  ____                         ___                 ");
	mvprintw(row / 2 - 9, (col - 51) / 2,
			 " / ___| __ _ _ __ ___   ___   / _ \\__   _____ _ __ ");
	mvprintw(row / 2 - 8, (col - 51) / 2,
			 "| |  _ / _` | '_ ` _ \\ / _ \\ | | | \\ \\ / / _ \\ '__|");
	mvprintw(row / 2 - 7, (col - 51) / 2,
			 "| |_| | (_| | | | | | |  __/ | |_| |\\ V /  __/ |   ");
	mvprintw(row / 2 - 6, (col - 51) / 2,
			 " \\____|\\__,_|_| |_| |_|\\___|  \\___/  \\_/ \\___|_|   ");
	attroff(A_BOLD | COLOR_PAIR(5));
	mvprintw(row / 2 - 1, col / 2 - 20, "SCORE : %d", score / 8);
	mvprintw(row / 2 - 2, col / 2 - 20, "%s", playerName);
	mvprintw(row / 2 - 2, col / 2 + 10, "%s", bestPlayerName);
	mvprintw(row / 2 - 1, col / 2 + 10, "BEST : %d", bestScore);
	mvprintw(row / 2 + 1, (col - 39) / 2, "Best score was saved to \"%s\"",
			 FILE_NAME);
	refresh();

	getchar();

	endwin();
}
