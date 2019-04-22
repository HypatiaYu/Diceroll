{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Roll a dice? Y\n"
     ]
    }
   ],
   "source": [
    "import numpy\n",
    "Name=input(\"Roll a dice?\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(Name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Roll a dice? Y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Roll a dice? Y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Roll a dice? N\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bye!\n"
     ]
    }
   ],
   "source": [
    "while Name == 'Y': \n",
    "    print(numpy.random.randint(6))\n",
    "    Name = input(\"Roll a dice?\")\n",
    "else: \n",
    "    print(\"bye!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
