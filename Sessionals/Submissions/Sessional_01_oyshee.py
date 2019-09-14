{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Into Image "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: './dataTemp/IUB2/দ্বু_BRAC2_Scan_0137.png'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-d68d2e25af12>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mPIL\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mImage\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mimage_path\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'./dataTemp/IUB2/'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mimage\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mImage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mimage_path\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m'দ্বু_BRAC2_Scan_0137.png'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mIPython\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdisplay\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mdisplay\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\PIL\\Image.py\u001b[0m in \u001b[0;36mopen\u001b[1;34m(fp, mode)\u001b[0m\n\u001b[0;32m   2632\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2633\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mfilename\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2634\u001b[1;33m         \u001b[0mfp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbuiltins\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"rb\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2635\u001b[0m         \u001b[0mexclusive_fp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2636\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: './dataTemp/IUB2/দ্বু_BRAC2_Scan_0137.png'"
     ]
    }
   ],
   "source": [
    "from PIL import Image\n",
    "image_path = './dataTemp/IUB2/'   \n",
    "image = Image.open(image_path + 'দ্বু_BRAC2_Scan_0137.png')\n",
    "\n",
    "from IPython.display import display \n",
    "display(image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'image' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-4ce9a2b7f82b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mimage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msave\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mimage_path\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m'দ্বু_BRAC2_Scan_0137.png'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'image' is not defined"
     ]
    }
   ],
   "source": [
    "image.save(image_path + 'দ্বু_BRAC2_Scan_0137.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: './dataTemp/IUB2/দ্বু_BRAC2_Scan_0137.png'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-d71c96c20834>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mimage\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mImage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mimage_path\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m'দ্বু_BRAC2_Scan_0137.png'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mimage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\PIL\\Image.py\u001b[0m in \u001b[0;36mopen\u001b[1;34m(fp, mode)\u001b[0m\n\u001b[0;32m   2632\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2633\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mfilename\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2634\u001b[1;33m         \u001b[0mfp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbuiltins\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"rb\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2635\u001b[0m         \u001b[0mexclusive_fp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2636\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: './dataTemp/IUB2/দ্বু_BRAC2_Scan_0137.png'"
     ]
    }
   ],
   "source": [
    "image = Image.open(image_path + 'দ্বু_BRAC2_Scan_0137.png') \n",
    "image.mode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'image' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-76b7dc74ef5d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mimage\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mimage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconvert\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'L'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mimage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'image' is not defined"
     ]
    }
   ],
   "source": [
    "image = image.convert('L')\n",
    "image.mode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'image' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-7c621e96f664>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mimage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mimage\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mimage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconvert\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'RGB'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mimage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'image' is not defined"
     ]
    }
   ],
   "source": [
    "len(image.split())\n",
    "image = image.convert('RGB')\n",
    "image.mode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'image' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-e6fd50f5f215>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mimage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'image' is not defined"
     ]
    }
   ],
   "source": [
    "len(image.split())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Get Directory Files Name by using glob"
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
       "['./dataTemp/IUB2\\\\IUB2_1.png',\n",
       " './dataTemp/IUB2\\\\IUB2_10.png',\n",
       " './dataTemp/IUB2\\\\IUB2_11.png',\n",
       " './dataTemp/IUB2\\\\IUB2_12.png',\n",
       " './dataTemp/IUB2\\\\IUB2_13.png',\n",
       " './dataTemp/IUB2\\\\IUB2_14.png',\n",
       " './dataTemp/IUB2\\\\IUB2_15.png',\n",
       " './dataTemp/IUB2\\\\IUB2_16.png',\n",
       " './dataTemp/IUB2\\\\IUB2_2.png',\n",
       " './dataTemp/IUB2\\\\IUB2_3.png',\n",
       " './dataTemp/IUB2\\\\IUB2_4.png',\n",
       " './dataTemp/IUB2\\\\IUB2_5.png',\n",
       " './dataTemp/IUB2\\\\IUB2_6.png',\n",
       " './dataTemp/IUB2\\\\IUB2_7.png',\n",
       " './dataTemp/IUB2\\\\IUB2_8.png',\n",
       " './dataTemp/IUB2\\\\IUB2_9.png']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import glob\n",
    "fileNames = glob.glob(image_path + '*.png') #asterisk here is a wildcard character\n",
    "fileNames"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Reading bulk data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(16, 3, 224, 224)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "bulkImage = []\n",
    "for file in fileNames:  # iterate across list type fileNames, You can do importing, right?\n",
    "    image = Image.open(file)\n",
    "    image = image.resize((224, 224), Image.ANTIALIAS)\n",
    "    image = np.asarray(image)\n",
    "    image = image.reshape(3, 224, 224)\n",
    "    bulkImage.append(image)\n",
    "bulkImage = np.asarray(bulkImage)\n",
    "bulkImage.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Numpy intro"
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
       "(3, 224, 224)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "imageArray = np.array(image)\n",
    "imageArray.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'imageArray' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-3c195ffaa294>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mimageArray\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'imageArray' is not defined"
     ]
    }
   ],
   "source": [
    "imageArray"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Binarization "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import preprocessing\n",
    "import numpy as np \n",
    "\n",
    "data = bulkImage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Binarized data:\n",
      "\n",
      " [[1 1 1]\n",
      " [1 1 1]\n",
      " [1 1 1]]\n"
     ]
    }
   ],
   "source": [
    "bindata = preprocessing.Binarizer(threshold=1.5).transform(data)\n",
    "print('Binarized data:\\n\\n', bindata)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mean Removal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-16-86ebb63d0acd>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Mean (before)= '\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Standard Deviation (before)= '\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstd\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "print('Mean (before)= ', data.mean(axis=0))\n",
    "print('Standard Deviation (before)= ', data.std(axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean (after)=  [2.46099437e-15 2.46099437e-15 2.46099437e-15]\n",
      "Standard Deviation (after)=  [1. 1. 1.]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\oyshee\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:595: DataConversionWarning: Data with input dtype int32 was converted to float64 by the scale function.\n",
      "  warnings.warn(msg, DataConversionWarning)\n"
     ]
    }
   ],
   "source": [
    "scaled_data = preprocessing.scale(data)\n",
    "\n",
    "print('Mean (after)= ', scaled_data.mean(axis=0))\n",
    "print('Standard Deviation (after)= ', scaled_data.std(axis=0))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#  Scaling\n",
    "\n",
    "- StandardScaler - => features with a mean=0 and variance=1\n",
    "- MinMaxScaler - => features in a 0 to 1 range\n",
    "- Normalizer - => feature vector to a Euclidean length=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-c5d84736ba45>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdata\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'preprocessing' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-50b095fbd631>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mminmax_scaler\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpreprocessing\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mMinMaxScaler\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfeature_range\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mdata_minmax\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mminmax_scaler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit_transform\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'MinMaxScaler applied on the data:\\n'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata_minmax\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'preprocessing' is not defined"
     ]
    }
   ],
   "source": [
    "minmax_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))\n",
    "data_minmax = minmax_scaler.fit_transform(data)\n",
    "print('MinMaxScaler applied on the data:\\n', data_minmax)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " # Normalization\n",
    "\n",
    "-- bringing the values of each feature vector on a common scale\n",
    "\n",
    "- L1 - Least Absolute Deviations - sum of absolute values (on each row) = 1; it is insensitive to outliers\n",
    "- L2 - Least Squares - sum of squares (on each row) = 1; takes outliers in consideration during training"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_l1 = preprocessing.normalize(data, norm='l1')\n",
    "data_l2 = preprocessing.normalize(data, norm='l2')\n",
    "\n",
    "print('L1-normalized data:\\n', data_l1)\n",
    "print('\\nL2-normalized data:\\n', data_l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "0.33333333+0.33333333+0.33333333"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "0.57735027**2+0.57735027**2+0.57735027"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
