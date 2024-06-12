{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6aad89e4",
   "metadata": {},
   "source": [
    "# guess a number game"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "08f2f687",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello! What is your name?\n",
      "Ola\n",
      "Well, Ola, I am thinking of a number between 1 and 20.\n",
      "Take a guess.\n",
      "10\n",
      "Good job, Ola! You guessed my number in 1 guesses!\n"
     ]
    }
   ],
   "source": [
    "# This is a Guess the Number game.\n",
    "import random\n",
    "\n",
    "guessesTaken = 0\n",
    "\n",
    "print('Hello! What is your name?')\n",
    "myName = input()\n",
    "\n",
    "number = random.randint(1, 20)\n",
    "print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')\n",
    "\n",
    "for guessesTaken in range(6):\n",
    "    print('Take a guess.') # Four spaces in front of \"print\"\n",
    "    guess = input()\n",
    "    guess = int(guess)\n",
    "    \n",
    "    if guess < number:\n",
    "        print('Your guess is too low.') # Eight spaces in front of \"print\"\n",
    "        \n",
    "    if guess > number:\n",
    "        print('Your guess is too high.')\n",
    "        \n",
    "    if guess == number:\n",
    "        break\n",
    "        \n",
    "if guess == number:\n",
    "    guessesTaken = str(guessesTaken + 1)\n",
    "    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')\n",
    "    \n",
    "if guess != number:\n",
    "    number = str(number)\n",
    "    print('Nope. The number I was thinking of was ' + number + '.')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c2969599",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello! What is your name?\n",
      "Ola\n",
      "Well, Ola, I am thinking of a number between 0 and 20.\n",
      "Take a guess.\n",
      "0\n",
      "Your guess is too low.\n",
      "Take a guess.\n",
      "16\n",
      "Your guess is too high.\n",
      "Take a guess.\n",
      "55\n",
      "Your guess is too high.\n",
      "Take a guess.\n",
      "10\n",
      "Good job, Ola! You guessed my number in 4 guesses!\n"
     ]
    }
   ],
   "source": [
    "# This is a Guess the Number game.\n",
    "import random\n",
    "\n",
    "guessesTaken = 0\n",
    "\n",
    "print('Hello! What is your name?')\n",
    "myName = input()\n",
    "\n",
    "number = random.randint(0, 20)\n",
    "print('Well, ' + myName + ', I am thinking of a number between 0 and 20.')\n",
    "\n",
    "for guessesTaken in range(6):\n",
    "    print('Take a guess.') # Four spaces in front of \"print\"\n",
    "    guess = input()\n",
    "    guess = int(guess)\n",
    "    \n",
    "    if guess < number:\n",
    "        print('Your guess is too low.') # Eight spaces in front of \"print\"\n",
    "        \n",
    "    if guess > number:\n",
    "        print('Your guess is too high.')\n",
    "        \n",
    "    if guess == number:\n",
    "        break\n",
    "        \n",
    "if guess == number:\n",
    "    guessesTaken = str(guessesTaken + 1)\n",
    "    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')\n",
    "    \n",
    "if guess != number:\n",
    "    number = str(number)\n",
    "    print('Nope. The number I was thinking of was ' + number + '.')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "278026ae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58271c7a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "77539673",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Length of password: 6\n",
      "How many letters do you want in your password : 2\n",
      "How many numbers do you want in your password : 4\n",
      "Your random password is:  :fGg!cTXdTrt\n"
     ]
    }
   ],
   "source": [
    "#password generator\n",
    "import random\n",
    "import string\n",
    "\n",
    "length = int(input('Enter Length of password: '))\n",
    "n_letters = int(input('How many letters do you want in your password : '))\n",
    "n_digits = int(input('How many numbers do you want in your password : '))\n",
    "\n",
    "chars = string.ascii_letters\n",
    "chars += string.digits\n",
    "chars += string.punctuation\n",
    "\n",
    "password = \"\"\n",
    "for i in range(length):\n",
    "    password += random.choice(chars)\n",
    "    \n",
    "for i in range(1,n_letters+1):\n",
    "    password += random.choice(chars)\n",
    "    \n",
    "for i in range(1,n_digits+1):\n",
    "    password += random.choice(chars)\n",
    "    \n",
    "print('Your random password is: ', password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c239b98d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae02d0ac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6e7a964d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Length of password: 8\n",
      "How many letters do you want in your password : 4\n",
      "How many symbols do you want in your password : 3\n",
      "How many numbers do you want in your password : 1\n",
      "Your random password is:  HvlE4<$~\n"
     ]
    }
   ],
   "source": [
    "#password generator\n",
    "import random\n",
    "import string\n",
    "\n",
    "length = int(input('Enter Length of password: '))\n",
    "n_letters = int(input('How many letters do you want in your password : '))\n",
    "n_symbols = int(input('How many symbols do you want in your password : '))\n",
    "n_digits = int(input('How many numbers do you want in your password : '))\n",
    "\n",
    "letters = string.ascii_letters\n",
    "numbers = string.digits\n",
    "symbols = string.punctuation\n",
    "\n",
    "password = \"\"\n",
    "#for i in range(length):\n",
    "   # password += random.choice(chars)\n",
    "    \n",
    "for i in range(1,n_letters+1):\n",
    "    password += random.choice(letters)\n",
    "    \n",
    "for i in range(1,n_digits+1):\n",
    "    password += random.choice(numbers)\n",
    "    \n",
    "for i in range(1,n_symbols+1):\n",
    "    password += random.choice(symbols)\n",
    "    \n",
    "    \n",
    "print('Your random password is: ', password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdace52d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47055e3b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
