{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "filePath1 = '../data/IUB1'\n",
    "filePath2 = '../data/IUB2'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "fileNames1 = os.listdir(filePath1)\n",
    "fileNames2 = os.listdir(filePath2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['অ_BRAC1_Scan_0005.png',\n",
       " 'এ্যা_BRAC1_Scan_0013.png',\n",
       " 'কৃ_BRAC1_Scan_0027.png',\n",
       " 'ক্ষ্য_BRAC1_Scan_0020.png',\n",
       " 'গ্মি_BRAC1_Scan_0002.png',\n",
       " 'চি_BRAC1_Scan_0052.png',\n",
       " 'জ্যো_BRAC1_Scan_0046.png',\n",
       " 'ণু_BRAC1_Scan_0037.png',\n",
       " 'দূ_BRAC1_Scan_0033.png',\n",
       " 'দ্যো_BRAC1_Scan_0049.png',\n",
       " 'নৃ_BRAC1_Scan_0014.png',\n",
       " 'ন্ত্ব_BRAC1_Scan_0021.png',\n",
       " 'ন্ধ্য_BRAC1_Scan_0057.png',\n",
       " 'পিঁ_BRAC1_Scan_0021.png',\n",
       " 'ফা_BRAC1_Scan_0070.png',\n",
       " 'বু_BRAC1_Scan_0001.png']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fileNames1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['অ_BRAC2_Scan_0130.png',\n",
       " 'এ_BRAC2_Scan_0079.png',\n",
       " 'ক্কো_BRAC2_Scan_0130.png',\n",
       " 'ক্ষো_BRAC2_Scan_0087.png',\n",
       " 'গী_BRAC2_Scan_0090.png',\n",
       " 'গ্ল্যা_BRAC2_Scan_0104.png',\n",
       " 'ঙ্ঘি_BRAC2_Scan_0075.png',\n",
       " 'ছ্যা_BRAC2_Scan_0083.png',\n",
       " 'ঞ্জু_BRAC2_Scan_0105.png',\n",
       " 'ড্ড_BRAC2_Scan_0119.png',\n",
       " 'ণ্ডে_BRAC2_Scan_0141.png',\n",
       " 'ত্র_BRAC2_Scan_0119.png',\n",
       " 'দ্বু_BRAC2_Scan_0137.png',\n",
       " 'না_BRAC2_Scan_0129.png',\n",
       " 'ন্ত্রী_BRAC2_Scan_0102.png',\n",
       " 'ন্মে_BRAC2_Scan_0131.png']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fileNames2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "graphemes = []\n",
    "for file1, file2 in zip(fileNames1, fileNames2):\n",
    "    graphemes.append(file1.split('_')[0])\n",
    "    graphemes.append(file2.split('_')[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['অ',\n",
       " 'অ',\n",
       " 'এ্যা',\n",
       " 'এ',\n",
       " 'কৃ',\n",
       " 'ক্কো',\n",
       " 'ক্ষ্য',\n",
       " 'ক্ষো',\n",
       " 'গ্মি',\n",
       " 'গী',\n",
       " 'চি',\n",
       " 'গ্ল্যা',\n",
       " 'জ্যো',\n",
       " 'ঙ্ঘি',\n",
       " 'ণু',\n",
       " 'ছ্যা',\n",
       " 'দূ',\n",
       " 'ঞ্জু',\n",
       " 'দ্যো',\n",
       " 'ড্ড',\n",
       " 'নৃ',\n",
       " 'ণ্ডে',\n",
       " 'ন্ত্ব',\n",
       " 'ত্র',\n",
       " 'ন্ধ্য',\n",
       " 'দ্বু',\n",
       " 'পিঁ',\n",
       " 'না',\n",
       " 'ফা',\n",
       " 'ন্ত্রী',\n",
       " 'বু',\n",
       " 'ন্মে']"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "graphemes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(graphemes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "uniqueGraphemes = set(graphemes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "31"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(uniqueGraphemes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'set' object has no attribute 'sort'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-38b6c8416928>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0muniqueGraphemes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msort\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: 'set' object has no attribute 'sort'"
     ]
    }
   ],
   "source": [
    "uniqueGraphemes.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'অ',\n",
       " 'এ',\n",
       " 'এ্যা',\n",
       " 'কৃ',\n",
       " 'ক্কো',\n",
       " 'ক্ষো',\n",
       " 'ক্ষ্য',\n",
       " 'গী',\n",
       " 'গ্মি',\n",
       " 'গ্ল্যা',\n",
       " 'ঙ্ঘি',\n",
       " 'চি',\n",
       " 'ছ্যা',\n",
       " 'জ্যো',\n",
       " 'ঞ্জু',\n",
       " 'ড্ড',\n",
       " 'ণু',\n",
       " 'ণ্ডে',\n",
       " 'ত্র',\n",
       " 'দূ',\n",
       " 'দ্বু',\n",
       " 'দ্যো',\n",
       " 'না',\n",
       " 'নৃ',\n",
       " 'ন্ত্ব',\n",
       " 'ন্ত্রী',\n",
       " 'ন্ধ্য',\n",
       " 'ন্মে',\n",
       " 'পিঁ',\n",
       " 'ফা',\n",
       " 'বু'}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uniqueGraphemes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({'grapheme': uniqueGraphemes,\n",
    "                    'label': np.arange(0,len(uniqueGraphemes))})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>grapheme</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>{ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             grapheme  label\n",
       "0   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      0\n",
       "1   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      1\n",
       "2   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      2\n",
       "3   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      3\n",
       "4   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      4\n",
       "5   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      5\n",
       "6   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      6\n",
       "7   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      7\n",
       "8   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      8\n",
       "9   {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...      9\n",
       "10  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     10\n",
       "11  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     11\n",
       "12  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     12\n",
       "13  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     13\n",
       "14  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     14\n",
       "15  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     15\n",
       "16  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     16\n",
       "17  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     17\n",
       "18  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     18\n",
       "19  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     19\n",
       "20  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     20\n",
       "21  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     21\n",
       "22  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     22\n",
       "23  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     23\n",
       "24  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     24\n",
       "25  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     25\n",
       "26  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     26\n",
       "27  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     27\n",
       "28  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     28\n",
       "29  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     29\n",
       "30  {ত্র, দূ, অ, না, দ্বু, দ্যো, চি, ণু, ক্ষ্য, ণ্...     30"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "export_csv = df.to_csv('../dataTemp/label.csv', index = None, header=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "graphemeNames = os.listdir('../dataTemp/IUB')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['IUB_1.png',\n",
       " 'IUB_2.png',\n",
       " 'IUB_3.png',\n",
       " 'IUB_4.png',\n",
       " 'IUB_5.png',\n",
       " 'IUB_6.png',\n",
       " 'IUB_7.png',\n",
       " 'IUB_8.png',\n",
       " 'IUB_9.png',\n",
       " 'IUB_10.png',\n",
       " 'IUB_11.png',\n",
       " 'IUB_12.png',\n",
       " 'IUB_13.png',\n",
       " 'IUB_14.png',\n",
       " 'IUB_15.png',\n",
       " 'IUB_16.png',\n",
       " 'IUB_17.png',\n",
       " 'IUB_18.png',\n",
       " 'IUB_19.png',\n",
       " 'IUB_20.png',\n",
       " 'IUB_21.png',\n",
       " 'IUB_22.png',\n",
       " 'IUB_23.png',\n",
       " 'IUB_24.png',\n",
       " 'IUB_25.png',\n",
       " 'IUB_26.png',\n",
       " 'IUB_27.png',\n",
       " 'IUB_28.png',\n",
       " 'IUB_29.png',\n",
       " 'IUB_30.png',\n",
       " 'IUB_31.png',\n",
       " 'IUB_32.png']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(os.listdir('../dataTemp/IUB'), key=len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({'fileID': graphemeNames,\n",
    "                    'targetVar': np.arange(0,len(graphemeNames))})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "export_csv = df.to_csv('../dataTemp/groundTruth.csv', index = None, header=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "df = pd.read_csv('../dataTemp/groundTruth.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "def to_one_hot(value,size):\n",
    "    np_one_hot = np.zeros(shape= size)\n",
    "    np_one_hot[value]=1\n",
    "    return np_one_hot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "index 31 is out of bounds for axis 0 with size 31",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-26-582b582fe60b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m     label=to_one_hot(\n\u001b[0;32m      4\u001b[0m                 \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloc\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'fileID'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m==\u001b[0m\u001b[0mfile\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'targetVar'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m                 \u001b[1;36m31\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m     )\n",
      "\u001b[1;32m<ipython-input-25-b58b0fc281c5>\u001b[0m in \u001b[0;36mto_one_hot\u001b[1;34m(value, size)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mto_one_hot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0msize\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mnp_one_hot\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mzeros\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mshape\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0msize\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mnp_one_hot\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mnp_one_hot\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: index 31 is out of bounds for axis 0 with size 31"
     ]
    }
   ],
   "source": [
    "graphemeNames = os.listdir('../dataTemp/IUB')\n",
    "for file in graphemeNames:\n",
    "    label=to_one_hot(\n",
    "                df.loc[df['fileID']==file]['targetVar'].values,\n",
    "                31\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n",
       "       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
