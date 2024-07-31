{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOaEoUrxf1oqXX9/T4nhh2O",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Udaykiran1817/ExpenseApp/blob/master/Copy_of_Experiment_1_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QRWvKvcL_G5h",
        "outputId": "87a04037-9841-42ff-c90e-189750ce24a8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hi Dheeraj Laund\n",
            "[1, 2, 3, 4, 5, 6, 7]\n",
            "[1, 2, 3, 4, 5, 6, 7, 18]\n",
            "[1, 2, 3, 4, 5, 6, 7, 18, 12, 13, 14]\n",
            "[1, 2, 3, 4, 5, 6, 18, 12, 13, 14]\n",
            "[3, 4, 5]\n",
            "[1, 2, 3]\n",
            "[4, 5, 6, 18, 12, 13, 14]\n"
          ]
        }
      ],
      "source": [
        "print(\"Hi Dheeraj\")\n",
        "my_list =[1,2,3,4,5,6,7]\n",
        "print(my_list)\n",
        "my_list.append(18);\n",
        "print(my_list);\n",
        "my_list.extend([12,13,14]);\n",
        "print(my_list);\n",
        "\n",
        "my_list.remove(7);\n",
        "print(my_list);\n",
        "\n",
        "slice1 = my_list[2:5]\n",
        "print(slice1)\n",
        "slice2 = my_list[:3]\n",
        "print(slice2)\n",
        "slice3 = my_list[3:]\n",
        "print(slice3)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create a List and manipulate the list by adding,removing elements in the list.Slice the list.(Print them)"
      ],
      "metadata": {
        "id": "ujT6TJ3zN9B3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "new_list=[];\n",
        "other_list=[4,23,5,3,534,5];\n",
        "new_list.extend(other_list[:3]);\n",
        "print(new_list)\n",
        "\n",
        "list1 =[1,2,3];\n",
        "list2 =[5,6,7];\n",
        "\n",
        "matrix = [list1,list2]\n",
        "print(matrix);\n",
        "print(\"Matrix\" )\n",
        "for row in matrix:\n",
        "  print(row)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vdIMsewfMT6W",
        "outputId": "c2835f74-c177-45c8-ab31-dab05bf5d7dd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[4, 23, 5]\n",
            "[[1, 2, 3], [5, 6, 7]]\n",
            "Matrix\n",
            "[1, 2, 3]\n",
            "[5, 6, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "my_tuple=(2,3,4,5,6,7,8)\n",
        "slice1= my_tuple[2:6];\n",
        "slice2= my_tuple[3:];\n",
        "slice3= my_tuple[:4];\n",
        "print(\"Original Tuple: \",my_tuple)\n",
        "print(\"Sliced Tuple-1: \",slice1);\n",
        "print(\"Sliced Tuple-2: \",slice2);\n",
        "print(\"Sliced Tuple-3: \",slice3);\n",
        "\n",
        "\n",
        "print(my_tuple);"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oNk7wWDSPMm2",
        "outputId": "6c2cf209-1dc9-4a59-89be-ca0e4a364fa1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original Tuple:  (2, 3, 4, 5, 6, 7, 8)\n",
            "Sliced Tuple-1:  (4, 5, 6, 7)\n",
            "Sliced Tuple-2:  (5, 6, 7, 8)\n",
            "Sliced Tuple-3:  (2, 3, 4, 5)\n",
            "(2, 3, 4, 5, 6, 7, 8)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create an empty list and add another list to the previous list and create a matrix and show."
      ],
      "metadata": {
        "id": "fgDlyH7kQtMO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_dict = {'a':1,'b':2,'c':3}\n",
        "my_dict['d'] = 4;\n",
        "print(my_dict)\n",
        "my_dict.update({'g':5,'h':6,'i':7})\n",
        "print(my_dict);\n",
        "del my_dict['a']\n",
        "print(my_dict);\n",
        "my_dict.pop('b')\n",
        "print(my_dict);\n",
        "my_dict.popitem()\n",
        "print(my_dict);\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oF8UfPAVQV3-",
        "outputId": "cf9e3d02-ae85-46bb-c71b-d5d22b21bb22"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'a': 1, 'b': 2, 'c': 3, 'd': 4}\n",
            "{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'g': 5, 'h': 6, 'i': 7}\n",
            "{'b': 2, 'c': 3, 'd': 4, 'g': 5, 'h': 6, 'i': 7}\n",
            "{'c': 3, 'd': 4, 'g': 5, 'h': 6, 'i': 7}\n",
            "{'c': 3, 'd': 4, 'g': 5, 'h': 6}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# prompt: Write a program to update the dictionary\n",
        "\n",
        "my_dict = {'a': 1, 'b': 2, 'c': 3}\n",
        "my_dict['d'] = 4\n",
        "print(my_dict)\n",
        "my_dict.update({'g': 5, 'h': 6, 'i': 7})\n",
        "print(my_dict)\n",
        "# update the dictionary with new key-value pairs\n",
        "my_dict.update({'j': 8, 'k': 9})\n",
        "# print the updated dictionary\n",
        "print(my_dict)\n"
      ],
      "metadata": {
        "id": "3LDB7OqoR9G-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create a dictionary.\n"
      ],
      "metadata": {
        "id": "QnHWYzgIQzGN"
      }
    }
  ]
}